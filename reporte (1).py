datos_recibidos = [
    ["Laptop HP", "Teclado funcional", "Laboratorio"],
    ["Cargador", "Cables pelados", "Basurero Especial"],
    ["Mouse Pro", "Sensor OK", "Laboratorio"],
    ["Tablet", "Pantalla quebrada", "Basurero Especial"]
]

import os
os.system('cls' if os.name == 'nt' else 'clear')


print("--- SISTEMA DE RECOLECCIÓN DE E-WASTE ---")
print("Reporte de Clasificación Final:")
print("---------------------------------------")


para_lab = 0
para_basura = 0


for equipo in datos_recibidos:
    nombre = equipo[0]
    estado = equipo[1]
    destino = equipo[2]
    
 
    print(f"Producto: {nombre} | Piezas: {estado} | Destino: {destino}")
    

    if destino == "Laboratorio":
        para_lab = para_lab + 1
    else:
        para_basura = para_basura + 1


print("---------------------------------------")
print(f"Resumen para los Laboratorios: {para_lab} piezas.")
print(f"Resumen para Reciclaje Seguro: {para_basura} piezas.")
print("---------------------------------------")