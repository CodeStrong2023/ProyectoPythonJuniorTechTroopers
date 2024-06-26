import tkinter as tk
from tkinter import ttk
from src.database.Get_info_db import Getinfo
import src.form.Panel_general_form as panel_general

class HospCarAlq:
    def __init__(self, username="", user_id="", db_key='1'):
        self.username = username
        self.user_id = user_id
        self.crear_interfaz_hospedaje()

    def crear_interfaz_hospedaje(self):
        self.root = tk.Tk()
        self.root.title("HOSPEDAJES")
        self.root.geometry('1400x400')  # Ajusta el tamaño de la ventana

        # Configurar estilo
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 15))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12), padding=5)
        style.configure('TFrame', background='#FFFFFF')  # Fondo blanco
        style.configure('Usuario.TFrame', background='#FFFFFF')  # Blanco para datos de usuario
        style.configure('Dueno.TFrame', background='#FFFFFF')  # Blanco para datos de dueño
        style.configure('Volver.TButton', font=('Arial', 12), padding=5, background='#D3D3D3')

        # Crear marco principal
        self.main_frame = ttk.Frame(self.root, padding="20 20 40 40", style='TFrame')
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crear notebook (pestañas)
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

        # Crear pestañas para usuario y dueño
        self.crear_pestaña_usuario()
        self.crear_pestaña_dueno()

        # Crear botón "Volver"
        self.boton_volver = ttk.Button(self.main_frame, text="Volver", style='Volver.TButton', command=self.volver)
        self.boton_volver.grid(row=1, column=0, pady=20)

        self.actualizar_datos_alquiler()
        self.root.mainloop()

    def crear_pestaña_usuario(self):
        # Crear una pestaña para los datos del usuario que alquila
        self.usuario_frame = ttk.Frame(self.notebook, padding="10 10 10 10", style='Usuario.TFrame')
        self.notebook.add(self.usuario_frame, text='MIS RESERVAS')

        # Crear tabla de datos de usuario
        columns = ('nombre_hospedaje', 'direccion', 'ubicacion', 'nombre_completo', 'email', 'fecha_inicio', 'fecha_fin')
        self.tree_usuario = ttk.Treeview(self.usuario_frame, columns=columns, show='headings', height=10)
        self.tree_usuario.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar encabezados de tabla
        self.tree_usuario.heading('nombre_hospedaje', text='Nombre del Hospedaje')
        self.tree_usuario.heading('direccion', text='Dirección')
        self.tree_usuario.heading('ubicacion', text='Ubicación')
        self.tree_usuario.heading('nombre_completo', text='Nombre Completo')
        self.tree_usuario.heading('email', text='Email')
        self.tree_usuario.heading('fecha_inicio', text='Fecha de Inicio')
        self.tree_usuario.heading('fecha_fin', text='Fecha de Fin')

    def crear_pestaña_dueno(self):
        # Crear una pestaña para los datos del dueño del hospedaje
        self.dueno_frame = ttk.Frame(self.notebook, padding="10 10 10 10", style='Dueno.TFrame')
        self.notebook.add(self.dueno_frame, text='HOSPEDAJES ALQUILADOS')

        # Crear tabla de datos de dueño
        columns = ('nombre_hospedaje', 'nombre_completo', 'email', 'fecha_inicio', 'fecha_fin')
        self.tree_dueno = ttk.Treeview(self.dueno_frame, columns=columns, show='headings', height=10)
        self.tree_dueno.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar encabezados de tabla
        self.tree_dueno.heading('nombre_hospedaje', text='Nombre del Hospedaje del Dueño')
        self.tree_dueno.heading('nombre_completo', text='Nombre Completo')
        self.tree_dueno.heading('email', text='Email')
        self.tree_dueno.heading('fecha_inicio', text='Fecha de Inicio')
        self.tree_dueno.heading('fecha_fin', text='Fecha de Fin')

    def on_tab_change(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")

        if tab_text == 'Datos de Usuario':
            self.usuario_frame.configure(style='Usuario.TFrame')
            self.dueno_frame.configure(style='TFrame')
        elif tab_text == 'Datos de Dueño':
            self.dueno_frame.configure(style='Dueno.TFrame')
            self.usuario_frame.configure(style='TFrame')

    def volver(self):
        self.root.destroy()
        print("Botón Volver presionado")
        panel_general.PanelGeneralForm(username=self.username,
                                       user_id=self.user_id)

    def actualizar_datos_alquiler(self):
        getinfo = Getinfo()  # Instancia de la clase Getinfo para acceder a las funciones
        alquileres = getinfo.informacion_alquiler(self.user_id)
        hospedajes = getinfo.informacion_dueño(self.user_id)

        # Limpiar datos actuales en las tablas
        for item in self.tree_usuario.get_children():
            self.tree_usuario.delete(item)
        for item in self.tree_dueno.get_children():
            self.tree_dueno.delete(item)

        # Actualizar datos en la tabla de usuario y de dueño
        for alquiler in alquileres:
            # Insertar datos del usuario que alquila
            self.tree_usuario.insert('', tk.END, values=(
                alquiler['name_hosting'], alquiler['address'], alquiler['ubicacion'],
                alquiler['nombre_completo'], alquiler['email'], alquiler['start_date'], alquiler['end_date']))

        for hospedaje in hospedajes:
            # Insertar datos del usuario que alquila
            self.tree_dueno.insert('', tk.END, values=(
                hospedaje['name_hosting'], hospedaje['nombre_completo'], hospedaje['email'],
                hospedaje['start_date'], hospedaje['end_date']))

        # Actualizar la interfaz gráfica
        self.root.update_idletasks()
