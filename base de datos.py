import tkinter as tk
from tkinter import messagebox, ttk
from db_unified import guardar_residuo, obtener_todos_registros
import os

nombre_archivo = 'registros_ewaste.xlsx'  # Usar el mismo archivo

def guardar_datos():
    aparato = entry_aparato.get()
    cantidad_peso = entry_cantidad_peso.get()
    categoria = entry_categoria.get()
    estado = entry_estado.get()
    comentario = entry_comentario.get()

    if not aparato or not cantidad_peso or not categoria or not estado:
        messagebox.showwarning("Advertencia", "Los campos Aparato, Cantidad/Peso, Categoría y Estado son obligatorios")
        return
    
    try:
        cantidad_peso = float(cantidad_peso)
    except ValueError:
        messagebox.showwarning("Advertencia", "La cantidad/peso debe ser un número")
        return
    
    # Guardar usando la función unificada
    guardar_residuo(aparato, cantidad_peso, categoria, estado, comentario)
    
    messagebox.showinfo("Información", "Datos guardados con éxito en registros_ewaste.xlsx")
    
    # Limpiar campos
    entry_aparato.delete(0, tk.END)
    entry_cantidad_peso.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    entry_comentario.delete(0, tk.END)
    
    actualizar_lista()  # Actualizar la lista de registros

def actualizar_lista():
    """Actualiza el Treeview con los registros actuales"""
    for item in tree.get_children():
        tree.delete(item)
    
    registros = obtener_todos_registros()
    for r in registros[-20:]:  # Mostrar últimos 20
        tree.insert("", tk.END, values=(
            r['id'], r['fecha'], r['aparato'], 
            r['cantidad_peso'], r['categoria'], r['estado'], r['destino']
        ))

# Configurar interfaz
root = tk.Tk()
root.title("EcoRecycle - Gestión de Residuos Electrónicos")
root.geometry("1200x600")
root.configure(bg='#003B71')

# Frame para el formulario
frame_form = tk.Frame(root, bg='#003B71')
frame_form.pack(pady=10, padx=10, fill=tk.X)

label_style = {"bg": '#003B71', "fg": "white"}
entry_style = {"bg": '#39A935', "fg": "white"}

# Campos del formulario
campos = [
    ("Aparato", 0), ("Cantidad/Peso (kg)", 1), 
    ("Categoría", 2), ("Estado", 3), ("Comentario", 4)
]

entries = {}
for texto, fila in campos:
    label = tk.Label(frame_form, text=texto, **label_style)
    label.grid(row=fila, column=0, padx=10, pady=5, sticky='e')
    entry = tk.Entry(frame_form, **entry_style, width=30)
    entry.grid(row=fila, column=1, padx=10, pady=5)
    entries[texto] = entry

entry_aparato = entries["Aparato"]
entry_cantidad_peso = entries["Cantidad/Peso (kg)"]
entry_categoria = entries["Categoría"]
entry_estado = entries["Estado"]
entry_comentario = entries["Comentario"]

boton_guardar = tk.Button(frame_form, text="Guardar en Base de Datos", 
                          command=guardar_datos, bg='#BD1C2C', fg='white', width=20)
boton_guardar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Frame para la lista de registros
frame_lista = tk.Frame(root, bg='#003B71')
frame_lista.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

label_lista = tk.Label(frame_lista, text="Registros en Base de Datos", 
                       bg='#003B71', fg='white', font=('Arial', 12, 'bold'))
label_lista.pack(pady=5)

# Treeview para mostrar registros
columns = ('ID', 'Fecha', 'Aparato', 'Peso', 'Categoría', 'Estado', 'Destino')
tree = ttk.Treeview(frame_lista, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

# Botón para refrescar
boton_refrescar = tk.Button(frame_lista, text="Refrescar Lista", 
                            command=actualizar_lista, bg='#2d6a4f', fg='white')
boton_refrescar.pack(pady=5)

# Cargar datos iniciales
actualizar_lista()

root.mainloop()