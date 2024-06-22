import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

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
        self.root.geometry("1000x700")  # Tamaño de la ventana ajustado (100 px menos de alto)

        # Agregar título en la parte superior
        titulo = tk.Label(self.root, text="Complete los campos para una buena estadía", font=("Helvetica", 16))
        titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        # Lista de opciones para los comboboxes
        opciones = ["A", "B", "C", "D", "E"]

        # Crear y colocar los comboboxes y sus labels en la parte izquierda

        # label = tk.Label(self.root, text="Provincias")
        # label.grid(row= 1, column=0, padx=10, pady=10, sticky='w')
        # combobox = ttk.Combobox(self.root, state="readonly")
        # combobox.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        # combobox.bind("<<ComboxSelected>>",self.Provincias())
        #
        # label = tk.Label(self.root, text="Departamentos")
        # label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        # combobox = ttk.Combobox(self.root, state="readonly")
        # combobox.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        #
        # label = tk.Label(self.root, text="Localidades")
        # label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        # combobox = ttk.Combobox(self.root, state="readonly")
        # combobox.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        # Lista de opciones para los comboboxes
        opciones = ["A", "B", "C", "D", "E"]

        # Crear y colocar los comboboxes y sus labels en la parte izquierda
        for i, label_text in enumerate(labels):
            label = tk.Label(self.root, text=label_text)
            label.grid(row=i + 1, column=0, padx=10, pady=10, sticky='w')

            combobox = ttk.Combobox(self.root, values=opciones)
            combobox.grid(row=i + 1, column=1, padx=10, pady=10, sticky='w')

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
        btn_alquilar.grid(row=6, column=3, padx=10, pady=20, sticky='w')

        # Ajustar la fila y columna para que el panel de datos ocupe el espacio disponible
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Ejecutar el bucle principal de Tkinter
        self.root.mainloop()

    def Provincias(self):
        from src.database.Get_info_db import Getinfo
        provincias = Getinfo().obtener_provincias()  # Implementa este método para obtener provincias de DB_STAYS
        self.provincia_combobox['values'] = [provincia['nombre'] for provincia in provincias]
        self.provincias_ids = {provincia['nombre']: provincia['provincia_id'] for provincia in provincias}
    def Localidades(self):
        opciones = ["A", "B", "C", "D", "E"]
        return opciones
    def volver(self):
        # Llama a PanelGeneralForm con los parámetros adecuados
        print("Seleccionar botón presionado")
        self.root.destroy()
        from src.form.Panel_general_form import PanelGeneralForm
        PanelGeneralForm(username=self.username,user_id=self.user_id)

    def seleccionar(self):
        print("Seleccionar botón presionado")

    # def seleccionar(self):
    #     # Obtener las fechas seleccionadas
    #     fecha_inicio = fecha_inicio.get_date()
    #     fecha_final = fecha_final.get_date()
    #
    #     # Verificar que ambas fechas estén seleccionadas
    #     if fecha_inicio is None or fecha_final is None:
    #         messagebox.showerror("Error", "Por favor seleccione ambas fechas.")
    #         return
    #
    #     # Verificar que la fecha final no sea menor que la fecha inicial
    #     if fecha_final < fecha_inicio:
    #         messagebox.showerror("Error", "La fecha final no puede ser anterior a la fecha inicial.")
    #         return
    #
    #     # Si las validaciones pasan, puedes proceder con tu lógica
    #     print("Selección válida. Proceder con la acción deseada.")
    #
    #     # Ejemplo de lo que podrías hacer después de la validación:
    #     # Guardar las fechas seleccionadas o realizar alguna acción adicional