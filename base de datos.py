import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook, load_workbook
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
    ws.append(["Aparato", "Cantidad/peso", "Categoria", "Estado", "Algún comentario "])


def guardar_datos():
    aparato =entry_aparato.get()
    cantidad_peso =entry_cantidad_peso.get()
    categoria =entry_categoria.get()
    estado =entry_estado.get()
    comentario =entry_comentario.get()

    if not aparato or not cantidad_peso or not categoria or not estado or not comentario: 
        messagebox.showwarning( "Advertencia", " Todos los campos son obligatorios ")
        return
    try:
        cantidad_peso = int(cantidad_peso)
    except ValueError:
        messagebox.showwarning( "Advertencia", " La cantidad o peso deben ser cantidades enteras")
        return

    
    ws.append([aparato, cantidad_peso, categoria, estado, comentario])
    wb.save(nombre_archivo)
    messagebox.showwarning( "Información", " Datos guardados con exito ")

    entry_aparato.delete (0, tk.END)
    entry_cantidad_peso.delete (0, tk.END)
    entry_categoria.delete (0, tk.END)
    entry_estado.delete (0, tk.END)
    entry_comentario.delete (0, tk.END)
    
      

root = tk.Tk()
root.title ("Formulario")

root.configure (bg='#003B71')
label_style = {"bg": '#003B71' , "fg": "white" }
entry_style = {"bg": '#39A935' , "fg": "white" }


label_aparato = tk.Label(root, text="aparato", **label_style)
label_aparato.grid(row=0, column=0, padx=10, pady=5)
entry_aparato = tk.Entry(root, **entry_style)
entry_aparato.grid(row=0, column=1, padx=10, pady=5)

label_cantidad_peso = tk.Label(root, text="cantidad o peso", **label_style)
label_cantidad_peso.grid(row=1, column=0, padx=10, pady=5)
entry_cantidad_peso = tk.Entry(root, **entry_style)
entry_cantidad_peso.grid(row=1, column=1, padx=10, pady=5)

label_categoria = tk.Label(root, text="Categoria (plastico, metal, Vidrio)", **label_style)
label_categoria.grid(row=2, column=0, padx=10, pady=5)
entry_categoria = tk.Entry(root, **entry_style)
entry_categoria.grid(row=2, column=1, padx=10, pady=5)

label_estado = tk.Label(root, text="Categoría (Plastico, Metal, Vidrio)", **label_style)
label_estado.grid(row=3, column=0, padx=10, pady=5)
entry_estado = tk.Entry(root, **entry_style)
entry_estado.grid(row=3, column=1, padx=10, pady=5)

label_comentario = tk.Label(root, text="Estado (Funciona, Dañado, Para piezas)", **label_style)
label_comentario.grid(row=4, column=0, padx=10, pady=5)
entry_comentario = tk.Entry(root, **entry_style)
entry_comentario.grid(row=4,column=1, padx=10, pady=5)

boton_guardar = tk.Button(root,text="Guardar", command=guardar_datos, bg='#BD1C2C', fg='white', width=20 )
boton_guardar.grid(row=5,column=0, columnspan=2, padx=10, pady=5)







root.mainloop()