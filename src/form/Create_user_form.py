import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from src.service.Session_manager_service import SessionManager
from src.utils.validation import EmailVerification
from datetime import datetime, date
import re


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
        intentos_codigo (int): Contador de intentos de verificación del código.
    """

    def __init__(self):
        """
        Constructor de la clase.
        """
        # Inicializa los objetos de sesión y verificación de correo
        self.session_manager = SessionManager()
        self.email_verification = EmailVerification()
        self.intentos_codigo = 0  # Inicializa el contador de intentos de código
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

        # Campos de entrada con traducciones
        campos = {
            "nombre de usuario": "username",
            "contraseña": "password",
            "confirmar contraseña": "confirm_password",
            "nombre": "firstname",
            "apellido": "lastname",
            "fecha de nacimiento": "birthdate",
            "edad": "age",
            "teléfono": "phone",
            "email": "email"
        }
        self.entradas = {}

        for idx, (etiqueta, campo) in enumerate(campos.items()):
            # Crear etiquetas y campos de entrada
            ttk.Label(main_frame, text=etiqueta.capitalize()).grid(row=idx, column=0, padx=10, pady=5)
            if campo == "birthdate":
                entry = DateEntry(main_frame, date_pattern='dd/mm/yyyy', locale='es_ES', width=12)
                entry.bind("<<DateEntrySelected>>", self.calcular_edad)
            else:
                entry = ttk.Entry(main_frame, show="*" if "password" in campo else "")
                if campo == "age":
                    entry.config(state='readonly')
                if campo == "email":
                    entry.insert(0, "example@correo.com")
            entry.grid(row=idx, column=1, padx=10, pady=5)
            self.entradas[campo] = entry

        # Botones de Registrar y Volver
        ttk.Button(main_frame, text="Registrar", command=self.registrar_usuario).grid(row=len(campos), column=1,
                                                                                      pady=10)
        ttk.Button(main_frame, text="Volver", command=self.volver_login).grid(row=len(campos) + 1, column=1, pady=10)

        self.root.mainloop()

    def calcular_edad(self, event):
        """
        Calcula la edad a partir de la fecha de nacimiento ingresada y la muestra en el campo de edad.
        """
        birthdate_str = self.entradas['birthdate'].get()
        try:
            birthdate = datetime.strptime(birthdate_str, '%d/%m/%Y').date()
            hoy = date.today()
            edad = hoy.year - birthdate.year - ((hoy.month, hoy.day) < (birthdate.month, birthdate.day))
            self.entradas['age'].config(state='normal')
            self.entradas['age'].delete(0, tk.END)
            self.entradas['age'].insert(0, str(edad))
            self.entradas['age'].config(state='readonly')
        except ValueError:
            self.entradas['age'].config(state='normal')
            self.entradas['age'].delete(0, tk.END)
            self.entradas['age'].insert(0, "")
            self.entradas['age'].config(state='readonly')

    def validar_campos(self, datos_usuario):
        """
        Valida los campos del formulario.

        Args:
            datos_usuario (dict): Datos del usuario a registrar.

        Returns:
            bool: True si los campos son válidos, False en caso contrario.
        """
        for campo, valor in datos_usuario.items():
            if not valor.strip():
                messagebox.showerror("Error", f"El campo '{campo}' no puede estar vacío.")
                return False

        if not re.match(r"^\d{10,14}$", datos_usuario["phone"]):
            messagebox.showerror("Error", "El formato del teléfono es incorrecto. Debe contener entre 10 y 14 dígitos.")
            return False

        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", datos_usuario["email"]):
            messagebox.showerror("Error", "El formato del correo electrónico es incorrecto. Debe contener '@' y '.com'.")
            return False

        return True

    def registrar_usuario(self):
        """
        Registra un nuevo usuario.
        """
        # Recopilar datos del formulario y convertir a mayúsculas
        datos_usuario = {campo: self.entradas[campo].get().upper() for campo in self.entradas}
        email = datos_usuario.get("email")
        password = datos_usuario.get("password")
        confirm_password = datos_usuario.get("confirm_password")

        # Validar campos
        if not self.validar_campos(datos_usuario):
            return

        # Validar que las contraseñas coincidan
        if password != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        # Convertir la fecha al formato YYYY-MM-DD y validar la edad
        try:
            birthdate = datetime.strptime(datos_usuario['birthdate'], '%d/%m/%Y').date()
            datos_usuario['birthdate'] = birthdate.strftime('%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha de nacimiento no válido.")
            return

        hoy = date.today()
        age = hoy.year - birthdate.year - ((hoy.month, hoy.day) < (birthdate.month, birthdate.day))

        if age < 18:
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
        ttk.Label(self.verificacion_window, text="Ingrese el código de verificación").grid(row=0, column=0, padx=10,
                                                                                           pady=5)
        self.codigo_entrada = ttk.Entry(self.verificacion_window)
        self.codigo_entrada.grid(row=0, column=1, padx=10, pady=5)

        ttk.Button(self.verificacion_window, text="Verificar",
                   command=lambda: self.verificar_codigo(datos_usuario)).grid(row=1, column=1, pady=10)

    def verificar_codigo(self, datos_usuario):
        """
        Verifica el código de verificación.

        Args:
            datos_usuario (dict): Datos del usuario a registrar.
        """
        self.intentos_codigo += 1  # Incrementa el contador de intentos
        if self.intentos_codigo > 3:
            messagebox.showerror("Error", "Número máximo de intentos alcanzado.")
            self.verificacion_window.destroy()
            self.volver_login()
            return

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
