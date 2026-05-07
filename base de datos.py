import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook, load_workbook
import re
import os

nombre_archivo ='datos.xls'
#comprobar si  el archivo ya existe 
if os.path.exists(nombre_archivo):
    wb = load_workbook(nombre_archivo)
    ws = wb.active
else:
    #crear el libro de excel
    wb = Workbook ()
    ws = wb.active
    ws.append(["Nombre", "edad", "email", "telefono", "dirección"])


def guardar_datos():
    nombre =entry_nombre.get()
    edad =entry_edad.get()
    email =entry_email.get()
    telefono =entry_telefono.get()
    direccion =entry_direcccion.get()

    if not nombre or not edad or not email or not telefono or not direccion: 
        messagebox.showwarning( "Advertencia", " Todos los campos son obligatorios ")
        return
    try:
        edad = int(edad)
        telefono = int(telefono)
    except ValueError:
        messagebox.showwarning( "Advertencia", " edad y telefono deben de ser numeros ")
        return
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showwarning( "Advertencia", "el correo no es valido  ")
        return
    
    ws.append([nombre, edad, email, telefono, direccion])
    wb.save(nombre_archivo)
    messagebox.showwarning( "Información", " Datos guardados con exito ")

    entry_nombre.delete (0, tk.END)
    entry_edad.delete (0, tk.END)
    entry_email.delete (0, tk.END)
    entry_telefono.delete (0, tk.END)
    entry_direcccion.delete (0, tk.END)
    
      

root = tk.Tk()
root.title ("Formulario de entrada de datos")

root.configure (bg='#003B71')
label_style = {"bg": '#003B71' , "fg": "white" }
entry_style = {"bg": '#39A935' , "fg": "white" }


label_nombre = tk.Label(root, text="Nombre", **label_style)
label_nombre.grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root, **entry_style)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_edad = tk.Label(root, text="edad", **label_style)
label_edad.grid(row=1, column=0, padx=10, pady=5)
entry_edad = tk.Entry(root, **entry_style)
entry_edad.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="email", **label_style)
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root, **entry_style)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_telefono = tk.Label(root, text="Telefono", **label_style)
label_telefono.grid(row=3, column=0, padx=10, pady=5)
entry_telefono = tk.Entry(root, **entry_style)
entry_telefono.grid(row=3, column=1, padx=10, pady=5)

label_direccion = tk.Label(root, text="Direccion", **label_style)
label_direccion.grid(row=4, column=0, padx=10, pady=5)
entry_direcccion = tk.Entry(root, **entry_style)
entry_direcccion.grid(row=4,column=1, padx=10, pady=5)

boton_guardar = tk.Button(root,text="Guardar", command=guardar_datos, bg='#BD1C2C', fg='white', width=20 )
boton_guardar.grid(row=5,column=0, columnspan=2, padx=10, pady=5)







root.mainloop()