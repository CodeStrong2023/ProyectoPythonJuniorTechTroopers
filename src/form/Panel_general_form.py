import tkinter as tk
from tkinter import ttk
from src.database.Get_info_db import Getinfo

class PanelGeneralForm:
    def __init__(self, username="", usuario_id="", db_key='1'):
        self.username = username
        self.usuario_id = usuario_id
        self.crear_interfaz_panel()

    def crear_interfaz_panel(self):
        if self.username == "":
            print("No se ha ingresado un nombre de usuario")
            return

        user_info = Getinfo().informacion_panel(self.username)

        self.root = tk.Tk()
        self.root.title('PANEL GENERAL')

        # Configurar estilo
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 15))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12), padding=5)
        style.configure('TFrame', background='#3A4F3F')

        # Crear marco principal
        main_frame = ttk.Frame(self.root, padding="10 10 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Creamos una lista vacía
        self.campos = {}
        campos_textos = ["Nombre Usuario:", "Nombre:", "Apellido:", "Saldo:", "Email:"]
        for i, text in enumerate(campos_textos):
            ttk.Label(main_frame, text=text).grid(row=i, column=0, padx=10, pady=5)
            self.campos[text] = ttk.Entry(main_frame)
            self.campos[text].grid(row=i, column=1, padx=10, pady=5)

        # Botones
        self.submit_button = ttk.Button(main_frame, text="Registrar Hospedajes", command=self.on_submit_click)
        self.submit_button.grid(row=2, column=4, pady=10)
        self.submit_button = ttk.Button(main_frame, text="Alquilar Hospedaje", command=self.on_submit_click)
        self.submit_button.grid(row=3, column=4, pady=10)
        self.submit_button = ttk.Button(main_frame, text="Mis Reservas", command=self.on_submit_click)
        self.submit_button.grid(row=7, column=1, pady=10)

        self.muestra_panel(user_info)

        self.root.mainloop()

    def on_submit_click(self):
        # Aquí se define la acción a realizar cuando se haga clic en los botones
        print("Botón presionado")

    def muestra_panel(self, username):
        campos_textos = {
            "Nombre Usuario:": username.get_username(),
            "Nombre:": username.get_nombre(),
            "Apellido:": username.get_apellido(),
            "Saldo:": f"${username.get_saldo():,.2f}",
            "Email:": username.get_email(),
        }
        for key, value in campos_textos.items():
             if key in self.campos:
                 self.campos[key].insert(0, value)