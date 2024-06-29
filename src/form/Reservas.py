import tkinter as tk
from tkinter import ttk


class Reservas:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservas Disponibles")

        # Crear y configurar los widgets
        self.label = ttk.Label(self.root, text="Alquileres Disponibles")
        self.label.pack(pady=10)

        self.lista_alquileres = ttk.Treeview(self.root, columns=("id", "nombre", "precio"))
        self.lista_alquileres.heading("#0", text="ID")
        self.lista_alquileres.heading("id", text="ID")
        self.lista_alquileres.heading("nombre", text="Nombre")
        self.lista_alquileres.heading("precio", text="Precio")

        self.lista_alquileres.column("#0", width=50)
        self.lista_alquileres.column("id", width=50)
        self.lista_alquileres.column("nombre", width=150)
        self.lista_alquileres.column("precio", width=100)

        self.lista_alquileres.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Ejemplo de datos (esto debería ser reemplazado por datos reales de tu base de datos)
        self.cargar_alquileres([
            {"id": 1, "nombre": "Departamento en Mendoza", "precio": "$200"},
            {"id": 2, "nombre": "Departamento en San Rafael", "precio": "$150"},
            {"id": 3, "nombre": "Departamento en BsAs", "precio": "$180"}
        ])

    def cargar_alquileres(self, alquileres):
        # Limpiar la tabla antes de cargar nuevos datos
        for row in self.lista_alquileres.get_children():
            self.lista_alquileres.delete(row)

        # Cargar los nuevos datos en la tabla
        for alquiler in alquileres:
            self.lista_alquileres.insert("", "end", values=(alquiler["id"], alquiler["nombre"], alquiler["precio"]))

#Prueba de panel, hay que eliminarlo cuando se conecte a el boton de origen
if __name__ == "__main__":
    root = tk.Tk()
    app = Reservas(root)
    root.mainloop()
