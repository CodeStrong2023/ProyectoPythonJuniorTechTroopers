import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from src.database.Get_info_db import Getinfo

province_id = None
departament_id = None
location_id = None
start_date = None
end_date = None


class filtrame:

    def __init__(self, username="", user_id="", db_key='1'):
        self.username = username
        self.user_id = user_id
        print(f'Username {username}, id={user_id}')
        self.interfaz_hospedaje()

    def interfaz_hospedaje(self):
        # Lista de labels para los comboboxes
        labels = ["Provincias", "Departamentos", "Localidades"]

        # Inicializar la ventana principal
        self.root = tk.Tk()
        self.root.title("Interfaz con Comboboxes")
        self.root.geometry("1300x700")  # Tamaño de la ventana ajustado (100 px menos de alto)
        # self.root.attributes("-fullscreen", True) # Famoso lo que de

        # TODO: Titulo del Panel
        titulo = tk.Label(self.root, text="CAMPOS OBLIGATORIOS", font=("Helvetica", 16))
        titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Crear y colocar los comboboxes y sus labels en la parte izquierda
        # Desplegable PROVINCIA
        label_provincias = tk.Label(self.root, text="Provincias")
        label_provincias.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.provincia_combobox = ttk.Combobox(self.root, state="readonly")
        self.provincia_combobox.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        self.provincia_combobox.bind("<<ComboboxSelected>>", self.on_provincia_selected)

        # Desplegable DEPARTAMENTO
        label_departamentos = tk.Label(self.root, text="Departamentos")
        label_departamentos.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.departamento_combobox = ttk.Combobox(self.root, state="readonly")
        self.departamento_combobox.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.departamento_combobox.bind("<<ComboboxSelected>>", self.on_departamento_selected)

        # Desplegable LOCALIDAD
        label_localidades = tk.Label(self.root, text="Localidades")
        label_localidades.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.localidad_combobox = ttk.Combobox(self.root, state="readonly")
        self.localidad_combobox.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        self.localidad_combobox.bind("<<ComboboxSelected>>", self.on_localidad_selected)

        # FECHA INICIO
        label_fecha_inicio = tk.Label(self.root, text="Fecha de Inicio - Obligatorio")
        label_fecha_inicio.grid(row=1, column=2, padx=10, pady=10, sticky='w')
        self.fecha_inicio = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2,
                                      locale='es_ES')
        self.fecha_inicio.grid(row=1, column=3, padx=10, pady=10, sticky='w')
        self.fecha_inicio.bind("<<DateEntrySelected>>", self.capturar_fecha_inicio)

        # FECHA FINAL
        label_fecha_final = tk.Label(self.root, text="Fecha Final - Obligatorio")
        label_fecha_final.grid(row=3, column=2, padx=10, pady=10, sticky='w')
        self.fecha_final = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2,
                                     locale='es_ES')
        self.fecha_final.grid(row=3, column=3, padx=10, pady=10, sticky='w')
        self.fecha_final.bind("<<DateEntrySelected>>", self.capturar_fecha_final)

        # TODO BOTONES "Volver" y "Alquilar Hospedaje" en la parte inferior
        btn_volver = tk.Button(self.root, text="Volver", command=self.volver)
        btn_volver.grid(row=6, column=0, padx=10, pady=20, sticky='e')

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
        self.provincias_ids = {
            provincia['nombre']: provincia['provincia_id']
            for provincia in provincias
        }

    def on_provincia_selected(self, event):
        global province_id
        provincia_seleccionada = self.provincia_combobox.get()
        provincia_id = self.provincias_ids.get(provincia_seleccionada)
        province_id = provincia_id
        print(f'Provincia id:{provincia_id}')

        # Implementa este método para obtener departamentos según provincia
        departamentos = Getinfo().obtener_departamentos(provincia_id)
        self.departamento_combobox['values'] = [departamento['nombre'] for departamento in departamentos]
        self.departamentos_ids = {
            departamento['nombre']: departamento['departamento_id']
            for departamento in departamentos
        }

        # TODO: ACA TENDRIAS QUE LLAMAR A LA FUNCION PARA OBTENER HOSPEDAJES
        self.buscar_hospedajes()

    def on_departamento_selected(self, event):
        global departament_id
        departamento_seleccionado = self.departamento_combobox.get()
        departamento_id = self.departamentos_ids.get(departamento_seleccionado)
        departament_id = departamento_id
        print(f'Departamento id:{departamento_id}')

        # TODO: ACA TENDRIAS QUE LLAMAR A LA FUNCION PARA OBTENER HOSPEDAJES
        # Implementa este método para obtener localidades según departamento
        localidades = Getinfo().obtener_localidades(departamento_id)
        self.localidad_combobox['values'] = [localidad['nombre'] for localidad in localidades]
        self.localidad_ids = {
            localidad['nombre']: localidad['localidad_id']
            for localidad in localidades
        }

        self.buscar_hospedajes()

    def on_localidad_selected(self, event):
        global location_id
        localidad_seleccionado = self.localidad_combobox.get()
        localidad_id = self.localidad_ids.get(localidad_seleccionado)
        print(localidad_id)
        location_id = localidad_id
        print(f'Localidad id: {localidad_id}')
        self.buscar_hospedajes()

    def volver(self):
        global province_id, departament_id, location_id, start_date, end_date
        province_id = None
        departament_id = None
        location_id = None
        start_date = None
        end_date = None
        # Llama a PanelGeneralForm con los parámetros adecuados
        print("Seleccionar botón presionado")
        self.root.destroy()
        from src.form.Panel_general_form import PanelGeneralForm
        PanelGeneralForm(username=self.username, user_id=self.user_id)

    def capturar_fecha_inicio(self, event):
        global start_date
        start_date = self.fecha_inicio.get_date()
        self.buscar_hospedajes()

    def capturar_fecha_final(self, event):
        global end_date
        end_date = self.fecha_final.get_date()
        self.buscar_hospedajes()

    def buscar_hospedajes(self):
        print('te entro')

        if (start_date and end_date) is not None:
            if start_date > end_date:
                messagebox.showerror("Error", "La FECHA DE INICIO es mayor que la FECHA FINAL ")
                return

            from src.database.Get_info_db import Getinfo
            hospedajes = Getinfo().obtener_hospedajes_disponibles(
                province_id,
                departament_id,
                location_id,
                start_date,
                end_date
            )

            # Crear el marco de datos si no existe
            if hasattr(self, 'datos_frame'):
                self.datos_frame.destroy()

            self.datos_frame = tk.Frame(self.root, bg="lightgrey", width=800, height=400)
            self.datos_frame.grid(row=5, column=0, columnspan=4, padx=10, pady=20, sticky='nsew')

            # Crear el Treeview
            columns = ['Nombre', 'Dirección', 'Capacidad', 'Precio por Noche', 'Departamento', 'Localidad', 'Dueño',
                       'Contacto']
            self.tree = ttk.Treeview(self.datos_frame, columns=columns, show='headings')
            self.tree.pack(expand=True, fill='both')

            # Definir las cabeceras
            for col in columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=100)

            # Añadir los datos
            for hospedaje in hospedajes:
                self.tree.insert('', 'end', values=hospedaje[2:])

            # Añadir botón de selección
            btn_seleccionar = tk.Button(self.datos_frame, text="Seleccionar Hospedaje",
                                        command=lambda: self.seleccionar_hospedaje(hospedajes))
            btn_seleccionar.pack(pady=10)

    def seleccionar_hospedaje(self, hospedajes_full_list):
        selected_item = self.tree.selection()
        if selected_item:
            hospedaje = self.tree.item(selected_item)['values']
            index = self.tree.index(selected_item[0])

            # Calculamos los dias y el gasto total
            diferencia = self.fecha_final.get_date() - self.fecha_inicio.get_date()
            diferencia_dias = diferencia.days

            # Llama a la función para manejar el hospedaje seleccionado
            self.manejar_hospedaje_seleccionado(hospedajes_full_list[index], diferencia_dias)

    def manejar_hospedaje_seleccionado(self, hospedaje, diferencia_dias):
        print(f'hospedaje[4]{hospedaje[4]}, hospedaje[5]{hospedaje[5]}')
        print(hospedaje)
        print(self.user_id)
        costo_por_dia = hospedaje[5]
        precio_estadia = diferencia_dias * costo_por_dia
        self.locador_id = hospedaje[1]
        self.hosting_id = hospedaje[0]
        self.ubicacion = hospedaje[10]
        self.number_of_day = diferencia_dias
        self.total_cost = precio_estadia
        print(precio_estadia)
        from src.form.Create_tarjeta import Create_tarjeta
        Create_tarjeta(username=self.username,
                       user_id=self.user_id,
                       locador_id=self.locador_id,
                       hosting_id=self.hosting_id,
                       location_id=self.ubicacion,
                       start_date=start_date,
                       end_date=end_date,
                       number_of_days=self.number_of_day,
                       total_cost=self.total_cost
                       )
