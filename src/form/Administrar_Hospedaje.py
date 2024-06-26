import tkinter as tk
from tkinter import ttk, messagebox
from src.database.Get_info_db import Getinfo
import src.form.Panel_general_form as panel_general
from src.form.Editar_Hospedaje import EditarHospedaje

class AdministrarHospedaje:

    def __init__(self, username="", user_id=""):
        self.username = username
        self.user_id = user_id
        self.hospedajes_ids = {}
        self.crear_interfaz_administrar()

    def crear_interfaz_administrar(self):
        """
        Crea la interfaz gráfica para el registro de administrar.
        """
        self.root = tk.Tk()
        self.root.title("Seleccionar Hospedaje")

        # Configurar estilo
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12), padding=10)
        style.configure('TFrame', background='#3A4F3F')

        # Crear marco principal
        main_frame = ttk.Frame(self.root, padding="10 10 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(main_frame, text="Hospedajes:").grid(row=6, column=0, padx=10, pady=5)
        self.hospedaje_combobox = ttk.Combobox(main_frame, state="readonly", width=25)
        self.hospedaje_combobox.grid(row=6, column=1, padx=10, pady=5)
        self.hospedaje_combobox.bind("<<ComboboxSelected>>", self.on_hospedaje_selected)

        self.editar_button = ttk.Button(main_frame, text="Editar", command=self.on_editar_click)
        self.editar_button.grid(row=10, column=1, pady=10)

        self.volver_button = ttk.Button(main_frame, text="Volver", command=self.on_volver_click)
        self.volver_button.grid(row=10, column=2, pady=10)

        self.cargar_hospedaje()

        self.root.mainloop()

    def cargar_hospedaje(self):
        hospedajes = Getinfo().informacion_hospedaje(
            self.user_id)  # Implementa este método para obtener provincias de DB_STAYS
        if not hospedajes:
            messagebox.showerror("Error", "No tiene hospedajes cargados.")
            self.root.destroy()
            panel_general.PanelGeneralForm(username=self.username, user_id=self.user_id)
        else:
            self.hospedaje_combobox['values'] = [hospedaje['name_hosting'] for hospedaje in hospedajes]
            self.hospedajes_ids = {hospedaje['name_hosting']: hospedaje['hosting_id'] for hospedaje in hospedajes}
            print(f"Hospedajes: {self.hospedaje_combobox['values']}")

    def on_volver_click(self):
        print("Volver")
        self.root.destroy()
        panel_general.PanelGeneralForm(username=self.username,user_id=self.user_id)


    def on_hospedaje_selected(self, event):
        self.hospedaje_seleccionada = self.hospedaje_combobox.get()

    def on_editar_click(self):
        try:
            print("Editar")
            hospedaje_id = self.hospedajes_ids.get(self.hospedaje_seleccionada)
            hospedaje_activo = Getinfo().obtener_registros_activos(hospedaje_id)

            if hospedaje_activo == 0:
                self.root.destroy()
                EditarHospedaje(username=self.username, user_id=self.user_id, hospedaje_id=hospedaje_id)
            else:
                messagebox.showerror("Error", f"El hospedaje no se puede editar, por estar en periodo de renta")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al procesar la acción de editar el hospedaje: {e}")



