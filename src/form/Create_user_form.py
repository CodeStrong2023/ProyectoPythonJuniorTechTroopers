import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from src.service.Session_manager_service import SessionManager
from src.utils.validation import EmailVerification
from datetime import datetime, date

class Create_user:
    """
    Clase para gestionar la ventana de creación de usuario.

    Attributes:
        session_manager (SessionManager): Objeto para gestionar la sesión.
        email_verification (EmailVerification): Objeto para la verificación de correo electrónico.
        entradas (dict): Diccionario para almacenar los campos de entrada del formulario.
        root (tk.Tk): Ventana principal de la aplicación.
        verificacion_window (tk.Toplevel): Ventana secundaria para la verificación del correo.
        codigo_entrada (ttk.Entry): Campo de entrada para el código de verificación.
    """

    def __init__(self):
        """
        Constructor de la clase.
        """
        # Inicializa los objetos de sesión y verificación de correo
        self.session_manager = SessionManager()
        self.email_verification = EmailVerification()
        # Crea la interfaz gráfica de registro
        self.crear_interfaz_registro()

    def crear_interfaz_registro(self):
        """
        Crea la interfaz gráfica para el registro de usuario.
        """
        self.root = tk.Tk()
        self.root.title("Registro de Usuario")

        # Configurar estilo
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12), padding=10)
        style.configure('TFrame', background='#3A4F3F')

        # Crear marco principal
        main_frame = ttk.Frame(self.root, padding="10 10 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Campos de entrada
        campos = ["username", "password", "confirm_password", "nombre", "apellido", "documento", "fecha_nacimiento", "edad", "telefono", "email"]
        self.entradas = {}

        for idx, campo in enumerate(campos):
            # Crear etiquetas y campos de entrada
            ttk.Label(main_frame, text=campo.capitalize().replace("_", " ")).grid(row=idx, column=0, padx=10, pady=5)
            if campo == "fecha_nacimiento":
                entry = DateEntry(main_frame, date_pattern='dd/mm/yyyy', locale='es_ES', width=12)
                entry.bind("<<DateEntrySelected>>", self.calcular_edad)
            else:
                entry = ttk.Entry(main_frame, show="*" if "password" in campo else "")
                if campo == "edad":
                    entry.config(state='readonly')
            entry.grid(row=idx, column=1, padx=10, pady=5)
            self.entradas[campo] = entry

        # Botones de Registrar y Volver
        ttk.Button(main_frame, text="Registrar", command=self.registrar_usuario).grid(row=len(campos), column=1, pady=10)
        ttk.Button(main_frame, text="Volver", command=self.volver_login).grid(row=len(campos) + 1, column=1, pady=10)

        self.root.mainloop()

    def calcular_edad(self, event):
        """
        Calcula la edad a partir de la fecha de nacimiento ingresada y la muestra en el campo de edad.
        """
        fecha_nacimiento_str = self.entradas['fecha_nacimiento'].get()
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%d/%m/%Y').date()
            hoy = date.today()
            edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            self.entradas['edad'].config(state='normal')
            self.entradas['edad'].delete(0, tk.END)
            self.entradas['edad'].insert(0, str(edad))
            self.entradas['edad'].config(state='readonly')
        except ValueError:
            self.entradas['edad'].config(state='normal')
            self.entradas['edad'].delete(0, tk.END)
            self.entradas['edad'].insert(0, "")
            self.entradas['edad'].config(state='readonly')

    def registrar_usuario(self):
        """
        Registra un nuevo usuario.
        """
        # Recopilar datos del formulario
        datos_usuario = {campo: self.entradas[campo].get() for campo in self.entradas}
        email = datos_usuario.get("email")
        password = datos_usuario.get("password")
        confirm_password = datos_usuario.get("confirm_password")

        # Validar el correo electrónico
        if not email:
            messagebox.showerror("Error", "El campo de correo electrónico es obligatorio.")
            return

        if not self.email_verification.es_correo_valido(email):
            messagebox.showerror("Error", "El formato del correo electrónico no es válido.")
            return

        # Validar que las contraseñas coincidan
        if password != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        # Convertir la fecha al formato YYYY-MM-DD y validar la edad
        try:
            fecha_nacimiento = datetime.strptime(datos_usuario['fecha_nacimiento'], '%d/%m/%Y').date()
            datos_usuario['fecha_nacimiento'] = fecha_nacimiento.strftime('%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha de nacimiento no válido.")
            return

        hoy = date.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

        if edad < 18:
            messagebox.showerror("Error", "Debes ser mayor de 18 años para registrarte.")
            return

        # Enviar correo de verificación
        try:
            self.email_verification.conectar_smtp()
            self.email_verification.enviar_correo(email)
            self.email_verification.cerrar_conexion()
        except Exception as e:
            messagebox.showerror("Error", f"Error al enviar el correo electrónico: {e}")
            return

        # Mostrar mensaje de éxito y ventana de verificación
        messagebox.showinfo("Éxito", "Código de verificación enviado al correo electrónico.")
        self.mostrar_ventana_verificacion(datos_usuario)

    def mostrar_ventana_verificacion(self, datos_usuario):
        """
        Muestra la ventana de verificación del correo electrónico.

        Args:
            datos_usuario (dict): Datos del usuario a registrar.
        """
        self.verificacion_window = tk.Toplevel(self.root)
        self.verificacion_window.title("Verificación de Correo")

        # Crear campo de entrada y botón para el código de verificación
        ttk.Label(self.verificacion_window, text="Ingrese el código de verificación").grid(row=0, column=0, padx=10, pady=5)
        self.codigo_entrada = ttk.Entry(self.verificacion_window)
        self.codigo_entrada.grid(row=0, column=1, padx=10, pady=5)

        ttk.Button(self.verificacion_window, text="Verificar", command=lambda: self.verificar_codigo(datos_usuario)).grid(row=1, column=1, pady=10)

    def verificar_codigo(self, datos_usuario):
        """
        Verifica el código de verificación.

        Args:
            datos_usuario (dict): Datos del usuario a registrar.
        """
        codigo_ingresado = self.codigo_entrada.get()

        # Verificar el código ingresado
        if self.email_verification.verificar_codigo(codigo_ingresado):
            messagebox.showinfo("Éxito", "Código de verificación correcto.")
            self.session_manager.registrar_usuario(datos_usuario)
            self.verificacion_window.destroy()
            self.volver_login()
        else:
            messagebox.showerror("Error", "Código de verificación incorrecto. Inténtelo de nuevo.")

    def volver_login(self):
        """
        Vuelve a la ventana de inicio de sesión.
        """
        self.root.destroy()
        from src.form.Login_form import Login
        Login()

# Iniciar la aplicación
if __name__ == "__main__":
    create_user_app = Create_user()
