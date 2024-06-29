import tkinter as tk
from tkinter import ttk, messagebox
from src.database.Get_info_db import Getinfo
from src.database.Actualizar_info_db import ActualizarInfo
import src.form.Panel_general_form as panel_general

class EditarHospedaje:

    def __init__(self, username="", user_id="", hospedaje_id=""):
        self.username = username
        self.user_id = user_id
        self.hospedaje_id = hospedaje_id
        self.crear_interfaz_editar()

    def crear_interfaz_editar(self):
        self.root = tk.Tk()
        self.root.title('EDITAR HOSPEDAJE')
        hospedaje_info = Getinfo().informacion_hospedaje_completa(self.hospedaje_id)

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
        campos_textos = ["Nombre del Hospedaje:", "Dirección:", "Capacidad:", "Costo Diario:", "Estado:"]
        for i, text in enumerate(campos_textos):
            ttk.Label(main_frame, text=text).grid(row=i, column=0, padx=10, pady=5)
            if text == "Estado:":
                # Si es el campo de estado, crear un Combobox en lugar de una entrada
                self.estado_combobox = ttk.Combobox(main_frame, values=["Habilitado", "Des-habilitado"])
                self.estado_combobox.grid(row=i, column=1, padx=10, pady=5)
                self.estado_combobox.bind("<<ComboboxSelected>>", self.on_estado_selected)
            else:
                self.campos[text] = ttk.Entry(main_frame)
                self.campos[text].grid(row=i, column=1, padx=10, pady=5)

        # Llenar campos con la información del hospedaje
        self.muestra_hospedaje_info(hospedaje_info)

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
        self.submit_button = ttk.Button(main_frame, text="Editar", command=self.on_editar_click)
        self.submit_button.grid(row=10, column=1, pady=10)

        self.submit_button = ttk.Button(main_frame, text="Volver", command=self.on_volver_click)
        self.submit_button.grid(row=10, column=2, pady=10)

        # Cargar provincias desde la base de datos
        self.cargar_provincias()

        self.root.mainloop()

    def muestra_hospedaje_info(self, hospedaje_info):
        # Accede al primer elemento de la lista
        primer_hospedaje = hospedaje_info[0]

        campos_textos = {
            "Nombre del Hospedaje:": primer_hospedaje['name_hosting'],
            "Dirección:": primer_hospedaje['address'],
            "Capacidad:": str(primer_hospedaje['capacity']),
            "Costo Diario:": str(primer_hospedaje['daily_cost']),
            "Estado:": str(primer_hospedaje['state'])
        }
        for key, value in campos_textos.items():
            if key in self.campos:
                self.campos[key].insert(0, value)

    def on_estado_selected(self, event):
        estado_seleccionado = self.estado_combobox.get()
        # Asignar el valor numérico correspondiente
        if estado_seleccionado == "Habilitado":
            self.estado = 1
        else:
            self.estado = 0
    def cargar_provincias(self):
        provincias = Getinfo().obtener_provincias()  # Implementa este método para obtener provincias de DB_STAYS
        self.provincia_combobox['values'] = [provincia['nombre'] for provincia in provincias]
        self.provincias_ids = {provincia['nombre']: provincia['provincia_id'] for provincia in provincias}

    def on_provincia_selected(self, event):
        provincia_seleccionada = self.provincia_combobox.get()
        provincia_id = self.provincias_ids.get(provincia_seleccionada)
        departamentos = Getinfo().obtener_departamentos(provincia_id)
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

    def on_volver_click(self):
        self.root.destroy()
        print("Botòn Volver presionado")
        panel_general.PanelGeneralForm(username=self.username, user_id=self.user_id)

    def validar_datos(self):
        # Verificar si alguna casilla está vacía
        for key, entry in self.campos.items():
            if entry.get() == "":
                messagebox.showerror("Error", f"El campo '{key}' no puede estar vacío.")
                return False

        # Verificar si los IDs de provincia, departamento y localidad están seleccionados correctamente
        if (self.provincia_combobox.get() not in self.provincias_ids or
                self.departamento_combobox.get() not in self.departamentos_ids or
                self.localidad_combobox.get() not in self.localidades_ids):
            messagebox.showerror("Error",
                                 "Por favor selecciona una provincia, un departamento y una localidad válidos.")
            return False

        return True

    def on_editar_click(self):
        if not self.validar_datos():
            return

        # Obtener valores de los campos
        nombre_hospedaje = self.campos["Nombre del Hospedaje:"].get()
        direccion = self.campos["Dirección:"].get()
        capacidad = self.campos["Capacidad:"].get()
        precio = self.campos["Costo Diario:"].get()

        # Obtener IDs de provincia, departamento y localidad
        provincia = self.provincia_combobox.get()
        departamento = self.departamento_combobox.get()
        localidad = self.localidad_combobox.get()

        # Verificar si los IDs son válidos
        try:
            localidad_id = int(self.localidades_ids.get(localidad))
            provincia_id = int(self.provincias_ids.get(provincia))
            departamento_id = int(self.departamentos_ids.get(departamento))
            capacidad = int(capacidad)
            precio = int(precio)
        except ValueError:
            messagebox.showerror("Error", "Capacidad, precio y localidad deben ser números válidos.")
            return

        # Crear el diccionario de datos del hospedaje
        datos_hospedaje = {
            "hosting_id": self.hospedaje_id,
            'owner_id': int(self.user_id),
            'name_hosting': nombre_hospedaje,
            'address': direccion,
            'location_id': localidad_id,
            'capacity': capacidad,
            'daily_cost': precio,
            'depart_id': departamento_id,
            'province_id': provincia_id,
            'state' : self.estado
        }

        try:
            # Intentar actualizar el hospedaje en la base de datos
            ActualizarInfo().actualizar_hospedaje(datos_hospedaje)
            messagebox.showinfo("Éxito", "Hospedaje editado correctamente.")
            self.root.destroy()
            panel_general.PanelGeneralForm(username=self.username, user_id=self.user_id)
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al editar el hospedaje: {e}")
            print(datos_hospedaje)
