Nelson
exodier
Inactivo

Nelson — 12/06/2024 18:43
Ejemplo de encarpetado
TroopersStayPython (nombre del proyecto)
|-- src (carpeta principal)
|   |-- main.py (archivo principal)
|   |-- database (paquete)
|   |   |-- init.py
|   |   |-- updateinfo.py
|   |   |-- deleteinfo.py
|   |   |-- connection.py
|   |   |-- insertinfo.py
|   |   |-- getinfo.py
|   |-- form (paquete)
|   |   |-- init.py
|   |   |-- createaccommodation.py
|   |   |-- login.py
|   |   |-- menu.py
|   |   |-- panel.py
|   |   |-- register.py
|   |   |-- viewaccommodation.py
|   |-- model (paquete)
|   |   |-- init.py
|   |   |-- accommodation.py
|   |   |-- error_correction.py
|   |   |-- provinces.py
|   |   |-- user.py
|   |-- utils (paquete)
|   |   |-- init.py
|   |   |-- validation.py
|   |   |-- encryption.py
|   |-- tests (carpeta)
|   |   |-- __init.py
|   |   |-- test_database.py
|   |   |-- test_form.py
|   |   |-- test_model.py
|   |   |-- test_utils.py
Joaquín — 12/06/2024 18:46
Correo Proyecto Python: Juniorstechtroopers.frsr@gmail.com
Contraseña: Juniors2024

Key: c n o v b c g x w e o g o d r j
Nelson — 12/06/2024 18:47
main
develop
test
rama por tarea
Orden de encarpetado
Nelson — 18/06/2024 18:27
https://www.python.org/downloads/release/python-3124/

Version de python para trabajar en el proyecto 
Python.org
Python Release Python 3.12.4
The official home of the Python Programming Language
Imagen
Nelson — ayer a las 15:59
modelo de tarjeta o cargo saldo o money
Imagen
form crear la platilla
Maujj — ayer a las 17:09
nelson
Nelson — ayer a las 22:52
    def obtener_hospedajes_disponibles(self, province_id=None, departament_id=None, location_id=None, start_date=None, end_date=None):
        consulta = """
            SELECT *
            FROM DB_STAYS.Hosting AS _hosting 
            WHERE 
                (
                    _hosting.province_id = %s
                    OR _hosting.depart_id = %s
                    OR _hosting.location_id = %s
                )
                AND _hosting.state = 1
                AND (
                    SELECT 
                        COUNT(*)
                    FROM DB_STAYS.Rental_Register AS _rental 
                    WHERE _rental.hosting_id = _hosting.hosting_id
                        AND (
                            (_rental.start_date <= %s AND _rental.end_date >= %s)
                )
                
                )=0
            ;
        """
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta, (province_id, departament_id, location_id, end_date, start_date))
                resultado = cursor.fetchall()

                orden = ''




        except Error as e:
            print(f"Error al obtener los hospedajes disponibles: {e}")
            return []
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from src.database.Get_info_db import Getinfo


class filtrame:
    def __init__(self, username="", user_id="", db_key='1'):
        self.username = username
        self.user_id = user_id
        print(f'Username {username}, id={user_id}')
        self.interfaz_hospedaje()

        self.province_id = None
        self.departament_id = None
        self.location_id = None
        self.start_date = None
        self.end_date = None

    def interfaz_hospedaje(self):
        # Lista de labels para los comboboxes
        labels = ["Provincias", "Departamentos", "Localidades"]

        # Inicializar la ventana principal
        self.root = tk.Tk()
        self.root.title("Interfaz con Comboboxes")
        self.root.geometry("1000x700")  # Tamaño de la ventana ajustado (100 px menos de alto)

        # Agregar título en la parte superior
        titulo = tk.Label(self.root, text="Complete los campos para una buena estadía", font=("Helvetica", 16))
        titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Crear y colocar los comboboxes y sus labels en la parte izquierda
        label_provincias = tk.Label(self.root, text="Provincias")
        label_provincias.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.provincia_combobox = ttk.Combobox(self.root, state="readonly")
        self.provincia_combobox.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        self.provincia_combobox.bind("<<ComboboxSelected>>", self.on_provincia_selected)

        label_departamentos = tk.Label(self.root, text="Departamentos")
        label_departamentos.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.departamento_combobox = ttk.Combobox(self.root, state="readonly")
        self.departamento_combobox.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.departamento_combobox.bind("<<ComboboxSelected>>", self.on_departamento_selected)

        label_localidades = tk.Label(self.root, text="Localidades")
        label_localidades.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.localidad_combobox = ttk.Combobox(self.root, state="readonly")
        self.localidad_combobox.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        # Agregar campos para fecha de inicio y fecha final en la parte derecha
        label_fecha_inicio = tk.Label(self.root, text="Fecha de Inicio")
        label_fecha_inicio.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        fecha_inicio = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2,
                                 locale='es_ES')
        fecha_inicio.grid(row=1, column=3, padx=10, pady=10, sticky='w')

        label_fecha_final = tk.Label(self.root, text="Fecha Final")
        label_fecha_final.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        fecha_final = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2,
                                locale='es_ES')
        fecha_final.grid(row=2, column=3, padx=10, pady=10, sticky='w')

        # Panel para mostrar datos filtrados en el medio
        datos_frame = tk.Frame(self.root, bg="lightgrey", width=600, height=400)
        datos_frame.grid(row=5, column=0, columnspan=4, padx=10, pady=20, sticky='nsew')

        datos_label = tk.Label(datos_frame, text="Datos Filtrados", bg="lightgrey")
        datos_label.pack(padx=10, pady=10)

        # Agregar botones "Volver" y "Alquilar Hospedaje" en la parte inferior
        btn_volver = tk.Button(self.root, text="Volver", command=self.volver)
        btn_volver.grid(row=6, column=0, padx=10, pady=20, sticky='e')

        btn_alquilar = tk.Button(self.root, text="Alquilar Hospedaje", command=self.seleccionar)
        btn_alquilar.grid(row=6, column=4, padx=10, pady=20, sticky='w')

        # Ajustar la fila y columna para que el panel de datos ocupe el espacio disponible
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Cargar provincias al inicializar la interfaz
        self.cargar_provincias()

        # Ejecutar el bucle principal de Tkinter
        self.root.mainloop()

    def cargar_provincias(self):
        provincias = Getinfo().obtener_provincias()  # Implementa este método para obtener provincias de DB_STAYS
        self.provincia_combobox['values'] = [provincia['nombre'] for provincia in provincias]
        self.provincias_ids = {provincia['nombre']: provincia['provincia_id'] for provincia in provincias}

    def on_provincia_selected(self, event):
        provincia_seleccionada = self.provincia_combobox.get()
        provincia_id = self.provincias_ids.get(provincia_seleccionada)
        self.province_id = provincia_id
        departamentos = Getinfo().obtener_departamentos(
... (Quedan 39 líneas)
Minimizar
message.txt
7 KB
﻿
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from src.database.Get_info_db import Getinfo


class filtrame:
    def __init__(self, username="", user_id="", db_key='1'):
        self.username = username
        self.user_id = user_id
        print(f'Username {username}, id={user_id}')
        self.interfaz_hospedaje()

        self.province_id = None
        self.departament_id = None
        self.location_id = None
        self.start_date = None
        self.end_date = None

    def interfaz_hospedaje(self):
        # Lista de labels para los comboboxes
        labels = ["Provincias", "Departamentos", "Localidades"]

        # Inicializar la ventana principal
        self.root = tk.Tk()
        self.root.title("Interfaz con Comboboxes")
        self.root.geometry("1000x700")  # Tamaño de la ventana ajustado (100 px menos de alto)

        # Agregar título en la parte superior
        titulo = tk.Label(self.root, text="Complete los campos para una buena estadía", font=("Helvetica", 16))
        titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Crear y colocar los comboboxes y sus labels en la parte izquierda
        label_provincias = tk.Label(self.root, text="Provincias")
        label_provincias.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.provincia_combobox = ttk.Combobox(self.root, state="readonly")
        self.provincia_combobox.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        self.provincia_combobox.bind("<<ComboboxSelected>>", self.on_provincia_selected)

        label_departamentos = tk.Label(self.root, text="Departamentos")
        label_departamentos.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.departamento_combobox = ttk.Combobox(self.root, state="readonly")
        self.departamento_combobox.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.departamento_combobox.bind("<<ComboboxSelected>>", self.on_departamento_selected)

        label_localidades = tk.Label(self.root, text="Localidades")
        label_localidades.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.localidad_combobox = ttk.Combobox(self.root, state="readonly")
        self.localidad_combobox.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        # Agregar campos para fecha de inicio y fecha final en la parte derecha
        label_fecha_inicio = tk.Label(self.root, text="Fecha de Inicio")
        label_fecha_inicio.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        fecha_inicio = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2,
                                 locale='es_ES')
        fecha_inicio.grid(row=1, column=3, padx=10, pady=10, sticky='w')

        label_fecha_final = tk.Label(self.root, text="Fecha Final")
        label_fecha_final.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        fecha_final = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2,
                                locale='es_ES')
        fecha_final.grid(row=2, column=3, padx=10, pady=10, sticky='w')

        # Panel para mostrar datos filtrados en el medio
        datos_frame = tk.Frame(self.root, bg="lightgrey", width=600, height=400)
        datos_frame.grid(row=5, column=0, columnspan=4, padx=10, pady=20, sticky='nsew')

        datos_label = tk.Label(datos_frame, text="Datos Filtrados", bg="lightgrey")
        datos_label.pack(padx=10, pady=10)

        # Agregar botones "Volver" y "Alquilar Hospedaje" en la parte inferior
        btn_volver = tk.Button(self.root, text="Volver", command=self.volver)
        btn_volver.grid(row=6, column=0, padx=10, pady=20, sticky='e')

        btn_alquilar = tk.Button(self.root, text="Alquilar Hospedaje", command=self.seleccionar)
        btn_alquilar.grid(row=6, column=4, padx=10, pady=20, sticky='w')

        # Ajustar la fila y columna para que el panel de datos ocupe el espacio disponible
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Cargar provincias al inicializar la interfaz
        self.cargar_provincias()

        # Ejecutar el bucle principal de Tkinter
        self.root.mainloop()

    def cargar_provincias(self):
        provincias = Getinfo().obtener_provincias()  # Implementa este método para obtener provincias de DB_STAYS
        self.provincia_combobox['values'] = [provincia['nombre'] for provincia in provincias]
        self.provincias_ids = {provincia['nombre']: provincia['provincia_id'] for provincia in provincias}

    def on_provincia_selected(self, event):
        provincia_seleccionada = self.provincia_combobox.get()
        provincia_id = self.provincias_ids.get(provincia_seleccionada)
        self.province_id = provincia_id
        departamentos = Getinfo().obtener_departamentos(
            provincia_id)  # Implementa este método para obtener departamentos según provincia
        self.departamento_combobox['values'] = [departamento['nombre'] for departamento in departamentos]
        self.departamentos_ids = {departamento['nombre']: departamento['departamento_id'] for departamento in
                                  departamentos}

    def on_departamento_selected(self, event):
        departamento_seleccionado = self.departamento_combobox.get()
        departamento_id = self.departamentos_ids.get(departamento_seleccionado)
        self.departament_id = departamento_id
        localidades = Getinfo().obtener_localidades(
            departamento_id)  # Implementa este método para obtener localidades según departamento
        self.localidad_combobox['values'] = [localidad['nombre'] for localidad in localidades]
        self.localidad_id = {localidad['nombre']: localidad['localidad_id'] for localidad in localidades}

    def volver(self):
        # Llama a PanelGeneralForm con los parámetros adecuados
        print("Seleccionar botón presionado")
        self.root.destroy()
        from src.form.Panel_general_form import PanelGeneralForm
        PanelGeneralForm(username=self.username, user_id=self.user_id)

    def seleccionar(self):
        print("Seleccionar botón presionado")

    def buscar_hospedajes(self):

        from src.database.Get_info_db import Getinfo
        hospedajes = Getinfo.obtener_hospedajes_disponibles(
            self.province_id,
            self.departament_id,
            self.location_id,
            self.start_date,
            self.end_date
        )




message.txt
7 KB