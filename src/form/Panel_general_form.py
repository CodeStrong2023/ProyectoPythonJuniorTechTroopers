import tkinter as tk
from tkinter import ttk
from src.database.Get_info_db import Getinfo
from src.form.Administrar_Hospedaje import AdministrarHospedaje
from src.form.Cargar_Hospedaje import cargarHospedaje
from src.form.Flitro_hospedaje import filtrame
from src.form.Ver_Hospedajes import HospCarAlq

class PanelGeneralForm:
    def __init__(self, username="", user_id="", db_key='1'):
        self.username = username
        self.user_id = user_id
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
            self.muestra_panel(user_info)
            self.campos[text].config(state='readonly')

        # Botones
        self.submit_button = ttk.Button(main_frame, text="Registrar Hospedajes", command=self.registrar_hospedajes)
        self.submit_button.grid(row=2, column=4, pady=10)
        self.submit_button = ttk.Button(main_frame, text="Alquilar Hospedaje", command=self.filtro)
        self.submit_button.grid(row=3, column=4, pady=10)
        self.submit_button = ttk.Button(main_frame, text="Mis Reservas", command=self.on_hospedajes_click)
        self.submit_button.grid(row=7, column=1, pady=10)



        self.root.mainloop()

    def registrar_hospedajes(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title('Registrar o Administrar Hospedaje')

        # Configurar estilo
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), padding=5)

        # Crear marco principal
        main_frame = ttk.Frame(self.new_window, padding="10 10 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Botones
        self.button_cargar = ttk.Button(main_frame, text="Cargar", command=self.cargar)
        self.button_cargar.grid(row=2, column=1, pady=10)

        self.button_administrar = ttk.Button(main_frame, text="Administrar", command=self.administrar)
        self.button_administrar.grid(row=3, column=1, pady=10)

    def cargar(self):
        # Acción a realizar cuando se haga clic en el botón "Cargar"
        print("Botón 'Cargar' presionado")
        self.root.destroy()
        cargarHospedaje(username=self.username, user_id=self.user_id)
        # Aquí puedes agregar la lógica para la funcionalidad de "Cargar"

    def administrar(self):
        # Acción a realizar cuando se haga clic en el botón "Administrar"
        print("Botón 'Administrar' presionado")
        self.root.destroy()
        AdministrarHospedaje(username=self.username, user_id=self.user_id)

    def filtro(self):
        # Aquí se define la acción a realizar cuando se haga clic en los botones
        print("Botón Filtro")
        self.root.destroy()
        filtrame(username=self.username, user_id=self.user_id)

    def on_hospedajes_click(self):
        # Aquí se define la acción a realizar cuando se haga clic en los botones
        print("Botón presionado")
        self.root.destroy()
        HospCarAlq(username=self.username, user_id=self.user_id)

    def muestra_panel(self, username):
        campos_textos = {
            "Nombre Usuario:": username.get_username(),
            "Nombre:": username.get_firstname(),
            "Apellido:": username.get_lastname(),
            "Saldo:": f"${username.get_money():,.2f}",
            "Email:": username.get_email(),
        }
        for key, value in campos_textos.items():
             if key in self.campos:
                 self.campos[key].insert(0, value)
