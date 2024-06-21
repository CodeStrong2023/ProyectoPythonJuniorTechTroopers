# src/form/Login_form.py

import tkinter as tk
from tkinter import ttk, messagebox
from src.service.Session_manager_service import SessionManager
import src.form.Create_user_form
import src.form.Panel_general_form


class Login:
    """
    Clase para gestionar la ventana de inicio de sesión.

    Attributes:
        session_manager (SessionManager): Objeto para gestionar la sesión.
    """

    def __init__(self, db_key='1'):
        """
        Constructor de la clase.

        Args:
            db_key (str): Clave de la base de datos. Por defecto, '1'.
        """
        self.session_manager = SessionManager(db_key)
        self.crear_interfaz_inicio_sesion()

    def crear_interfaz_inicio_sesion(self):
        """
        Crea la interfaz gráfica para el inicio de sesión.
        """
        self.root = tk.Tk()
        self.root.title("Inicio de Sesión")

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
        ttk.Label(main_frame, text="Nombre de usuario").grid(row=0, column=0, padx=10, pady=5)
        ttk.Label(main_frame, text="Contraseña").grid(row=1, column=0, padx=10, pady=5)

        self.entrada_usuario = ttk.Entry(main_frame)
        self.entrada_contraseña = ttk.Entry(main_frame, show="*")

        self.entrada_usuario.grid(row=0, column=1, padx=10, pady=5)
        self.entrada_contraseña.grid(row=1, column=1, padx=10, pady=5)

        # Botones
        ttk.Button(main_frame, text="Iniciar Sesión", command=self.verificar_inicio_sesion).grid(row=2, column=1,
                                                                                                 pady=10)
        ttk.Button(main_frame, text="Registrar", command=self.abrir_registro).grid(row=3, column=1, pady=10)
        ttk.Button(main_frame, text="Salir", command=lambda: self.session_manager.salir_aplicacion(self.root)).grid(
            row=4, column=1, pady=10)

        self.root.mainloop()

    def verificar_inicio_sesion(self):
        """
        Verifica las credenciales de inicio de sesión.
        """
        usuario = self.entrada_usuario.get()
        contrasenia = self.entrada_contraseña.get()
        success, mensaje, usuario_info = self.session_manager.verificar_inicio_sesion(usuario, contrasenia)
        if success:
            # Si el inicio de sesión fue exitoso
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")  # Muestra un mensaje de éxito
            self.root.destroy()  # Cerrar la ventana de inicio de sesión
            # Realizar la acción que deseas, como abrir el siguiente menú, etc.
            src.form.PanelGeneralForm.PanelGeneralForm()
        else:
            # Si el inicio de sesión falló, mostrar un mensaje de error
            messagebox.showerror("Error", mensaje)

    def abrir_registro(self):
        """
        Abre la ventana de registro de usuario.
        """
        self.root.destroy()
        src.form.Create_user.Create_user()  # Abrir la ventana de registro


if __name__ == "__main__":
    login_app = Login(db_key='1')
