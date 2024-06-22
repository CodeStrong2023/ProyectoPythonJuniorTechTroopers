import tkinter as tk
from tkinter import ttk, messagebox

from src.database.Get_info_db import Getinfo
import src.form.Panel_general_form as panel_general
from src.database.Insert_info_db import InsertInfo


class cargarHospedaje:
    def __init__(self, username="", user_id=""):
        self.username = username
        self.user_id = user_id
        self.crear_interfaz_cargar()

    def crear_interfaz_cargar(self):
        self.root = tk.Tk()
        self.root.title('Cargar Hospedaje')

        # Configurar estilo
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 15))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12), padding=5)
        style.configure('TFrame', background='#3A4F3F')

        # Crear marco principal
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crear campos
        self.campos = {}
        campos_textos = ["Usuario:", "Nombre:", "Capacidad:", "Precio por noche:", "Direccion:"]
        for i, text in enumerate(campos_textos):
            ttk.Label(main_frame, text=text).grid(row=i, column=0, padx=10, pady=5)
            self.campos[text] = ttk.Entry(main_frame)
            self.campos[text].grid(row=i, column=1, padx=10, pady=5)

            if text == "Usuario:":
                self.campos[text].insert(0, self.username)
                self.campos[text].config(state='readonly')

        # Crear barra desplegable para provincias
        ttk.Label(main_frame, text="Provincia:").grid(row=6, column=0, padx=10, pady=5)
        self.provincia_combobox = ttk.Combobox(main_frame, state="readonly", width=25)
        self.provincia_combobox.grid(row=6, column=1, padx=10, pady=5)
        self.provincia_combobox.bind("<<ComboboxSelected>>", self.on_provincia_selected)

        # Crear barra desplegable para departamentos
        ttk.Label(main_frame, text="Departamento:").grid(row=7, column=0, padx=10, pady=5)
        self.departamento_combobox = ttk.Combobox(main_frame, state="readonly", width=25)
        self.departamento_combobox.grid(row=7, column=1, padx=10, pady=5)
        self.departamento_combobox.bind("<<ComboboxSelected>>", self.on_departamento_selected)

        # Crear barra desplegable para localidades
        ttk.Label(main_frame, text="Localidad:").grid(row=8, column=0, padx=10, pady=5)
        self.localidad_combobox = ttk.Combobox(main_frame, state="readonly", width=25)
        self.localidad_combobox.grid(row=8, column=1, padx=10, pady=5)

        # Botón para cargar hospedaje
        self.submit_button = ttk.Button(main_frame, text="Cargar Hospedaje", command=self.on_submit_click)
        self.submit_button.grid(row=10, column=1, pady=10)

        self.submit_button = ttk.Button(main_frame, text="Volver", command=self.volver)
        self.submit_button.grid(row=10, column=2, pady=10)

        # Cargar provincias desde la base de datos
        self.cargar_provincias()

        self.root.mainloop()
    def volver(self):
        self.root.destroy()
        print("Botòn Volver presionado")
        panel_general.PanelGeneralForm(username=self.username,
                                       user_id=self.user_id
                                       )
    def cargar_provincias(self):
        provincias = Getinfo().obtener_provincias()  # Implementa este método para obtener provincias de DB_STAYS
        self.provincia_combobox['values'] = [provincia['nombre'] for provincia in provincias]
        self.provincias_ids = {provincia['nombre']: provincia['provincia_id'] for provincia in provincias}

    def on_provincia_selected(self, event):
        provincia_seleccionada = self.provincia_combobox.get()
        provincia_id = self.provincias_ids.get(provincia_seleccionada)
        departamentos = Getinfo().obtener_departamentos(provincia_id)  # Implementa este método para obtener departamentos según provincia
        self.departamento_combobox['values'] = [departamento['nombre'] for departamento in departamentos]
        self.departamentos_ids = {departamento['nombre']: departamento['departamento_id'] for departamento in departamentos}

    def on_departamento_selected(self, event):
        departamento_seleccionado = self.departamento_combobox.get()
        departamento_id = self.departamentos_ids.get(departamento_seleccionado)
        localidades = Getinfo().obtener_localidades(departamento_id)

        # Crear un diccionario de localidades con nombre como clave y ID como valor
        localidades_dict = {localidad['nombre']: localidad['localidad_id'] for localidad in localidades}

        # Actualizar el Combobox con los nombres de las localidades
        self.localidad_combobox['values'] = list(localidades_dict.keys())

        # Almacenar el diccionario de localidades en el atributo self.localidades_ids
        self.localidades_ids = localidades_dict

    def on_submit_click(self):
        nombre = self.campos["Nombre:"].get()
        direccion = self.campos["Direccion:"].get()
        capacidad = self.campos["Capacidad:"].get()
        precio = self.campos["Precio por noche:"].get()
        provincia = self.provincia_combobox.get()
        departamento = self.departamento_combobox.get()
        localidad = self.localidad_combobox.get()


        if not nombre or not direccion or not capacidad or not precio or not provincia or not departamento or not localidad:
            # Si alguno de los campos está vacío, muestra un mensaje de error
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return


        try:
            localidad_id = int(self.localidades_ids.get(localidad))
            provincia_id = int(self.provincias_ids.get(provincia))
            departamento_id = int(self.departamentos_ids.get(departamento))
            capacidad = int(capacidad)
            precio = int(precio)
        except ValueError:
            messagebox.showerror("Error", "Capacidad, precio y localidad deben ser números válidos.")
            return

        datos_hospedaje = {
            'owner_id': int(self.user_id),
            'name_hosting': nombre,
            'address': direccion,
            'location_id': localidad_id,
            'capacity': capacidad,
            'daily_cost': precio,
            'depart_id': departamento_id,
            'province_id': provincia_id
        }

        try:
            InsertInfo().insertar_hospedaje(datos_hospedaje)  # Cambiado para instanciar InsertInfo
            messagebox.showinfo("Éxito", "Hospedaje cargado correctamente.")
            self.root.destroy()
            panel_general.PanelGeneralForm(username=self.username,
                                           user_id=self.user_id
                                           )
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al insertar el hospedaje: {e}")
            print(datos_hospedaje)
