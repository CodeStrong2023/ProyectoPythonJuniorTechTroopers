# src/form/Login.py

import tkinter as tk
from tkinter import messagebox
from src.database.Connection import Connection  # Importamos la clase Connection desde el paquete database
from src.database.Getinfo import validar_credenciales  # Importamos las funciones desde Getinfo

class Login:
    def __init__(self, db_key):
        self.conexion = Connection(db_key).connect()
        self.crear_interfaz_inicio_sesion()

    def crear_interfaz_inicio_sesion(self):
        self.root = tk.Tk()
        self.root.title("Inicio de Sesión")

        tk.Label(self.root, text="Nombre de usuario").grid(row=0, column=0)
        tk.Label(self.root, text="Contraseña").grid(row=1, column=0)

        self.entrada_usuario = tk.Entry(self.root)
        self.entrada_contraseña = tk.Entry(self.root, show="*")

        self.entrada_usuario.grid(row=0, column=1)
        self.entrada_contraseña.grid(row=1, column=1)

        tk.Button(self.root, text="Iniciar Sesión", command=self.verificar_inicio_sesion).grid(row=2, column=1)
        tk.Button(self.root, text="Registrarse", command=self.registrarse).grid(row=3, column=1)
        tk.Button(self.root, text="Salir", command=self.salir_aplicacion).grid(row=4, column=1)

        self.root.mainloop()

    def verificar_inicio_sesion(self):
        usuario = self.entrada_usuario.get()
        contraseña = self.entrada_contraseña.get()

        if validar_credenciales(self.conexion, usuario, contraseña):
            messagebox.showinfo("Éxito en el Inicio de Sesión", "¡Bienvenido a Trooper Stay!")
        else:
            messagebox.showerror("Fallo en el Inicio de Sesión", "Usuario o contraseña incorrectos")

    def registrarse(self):

         messagebox.showinfo("Registro Proximamente", "¡Esta función todavía no esta implementada!")

    def salir_aplicacion(self):
        self.root.quit()
        self.cerrar_conexion()

    def cerrar_conexion(self):
        self.conexion.close()

if __name__ == "__main__":
    app_inicio_sesion = Login(db_key='1')  # Usa la clave de la base de datos apropiada