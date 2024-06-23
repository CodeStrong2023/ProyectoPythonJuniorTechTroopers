import tkinter as tk
from tkinter import ttk, messagebox
import re

class Create_tarjeta:
    # Parámetros
    def __init__(self, username="", user_id="", money="", hosting_id="", location_id="", db_key='1'):
        self.root = tk.Tk()
        self.root.title("Datos del medio de pago")

        # Guarda los parámetros como atributos de instancia
        self.username = username
        self.user_id = user_id
        self.money = money
        self.hosting_id = hosting_id
        self.location_id = location_id

        # Variables de control para los widgets de entrada
        self.card_type_var = tk.StringVar(value="Crédito")
        self.expiration_month_var = tk.StringVar(value="01")
        self.expiration_year_var = tk.StringVar(value="0000")

        self.create_widgets()
        self.root.mainloop()

    # Crea y configura los widgets de la ventana principal
    def create_widgets(self):

        # Etiquetas
        ttk.Label(self.root, text="Tipo de tarjeta:").grid(column=0, row=0, padx=10, pady=5)
        ttk.Radiobutton(self.root, text="Crédito", variable=self.card_type_var, value="Crédito").grid(column=1, row=0, padx=10, pady=5)
        ttk.Radiobutton(self.root, text="Débito", variable=self.card_type_var, value="Débito").grid(column=2, row=0, padx=10, pady=5)

        ttk.Label(self.root, text="Número de tarjeta de 16 dígitos:").grid(column=0, row=1, padx=10, pady=5)
        self.card_number_entry = ttk.Entry(self.root)
        self.card_number_entry.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        ttk.Label(self.root, text="Fecha de vencimiento:").grid(column=0, row=2, padx=10, pady=5)
        expiration_month_combobox = ttk.Combobox(self.root, textvariable=self.expiration_month_var, values=[f"{i:02d}" for i in range(1, 13)], state="readonly")
        expiration_month_combobox.grid(column=1, row=2, padx=10, pady=5)
        expiration_month_combobox.set("MM")

        current_year = 2024
        expiration_year_combobox = ttk.Combobox(self.root, textvariable=self.expiration_year_var, values=[str(year) for year in range(current_year, current_year + 11)], state="readonly")
        expiration_year_combobox.grid(column=2, row=2, padx=10, pady=5)
        expiration_year_combobox.set("YYYY")

        ttk.Label(self.root, text="Nombre del titular como figura en la tarjeta:").grid(column=0, row=3, padx=10, pady=5)
        self.cardholder_name_entry = ttk.Entry(self.root)
        self.cardholder_name_entry.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        ttk.Label(self.root, text="Código de seguridad:").grid(column=0, row=4, padx=10, pady=5)
        self.security_code_entry = ttk.Entry(self.root, show='*')
        self.security_code_entry.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        # Botones
        submit_button = ttk.Button(self.root, text="Pagar", command=self.submit)
        submit_button.grid(column=1, row=5, padx=10, pady=10, columnspan=2)

        back_button = ttk.Button(self.root, text="Volver", command=self.go_back)
        back_button.grid(column=0, row=5, padx=10, pady=10)

    def submit(self):

        # Validación de los datos y procesamiento
        card_type = self.card_type_var.get()
        card_number = self.card_number_entry.get()
        expiration_month = self.expiration_month_var.get()
        expiration_year = self.expiration_year_var.get()
        cardholder_name = self.cardholder_name_entry.get()
        security_code = self.security_code_entry.get()

        # Validación del número de la tarjeta
        if not re.fullmatch(r"\d{16}", card_number):
            messagebox.showwarning("Input Error", "El número de tarjeta debe contener 16 dígitos numéricos")
            return

        # Validación de los campos obligatorios
        if expiration_month == "MM":
            messagebox.showwarning("Input Error", "Seleccione un mes de vencimiento válido")
            return

        if expiration_year == "YYYY":
            messagebox.showwarning("Input Error", "Seleccione un año de vencimiento válido")
            return

        if not cardholder_name:
            messagebox.showwarning("Input Error", "El nombre del titular es obligatorio")
            return

        if not re.fullmatch(r"\d{3,4}", security_code):
            messagebox.showwarning("Input Error", "El código de seguridad debe contener 3 o 4 dígitos numéricos")
            return

        # Confirmación del pago
        confirm = messagebox.askyesno("Confirmar Pago", "¿Está seguro que desea realizar el pago?")
        if confirm:
            # Aquí podemos usar los datos guardados en self.username, self.user_id, self.money, etc.
            messagebox.showinfo("Pago Exitoso", "Su pago se finalizó con éxito")
            # Cerrar la ventana de datos del medio de pago después de confirmar el pago
            self.root.destroy()
    def go_back(self):
        messagebox.showinfo("Volver", "Volviendo al panel anterior..")
        self.root.destroy()