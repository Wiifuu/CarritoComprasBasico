# Leer README.md si estas aprendiendo y quieres interiorizar en el codigo.

def comprobar(dato, flag):
    while True:
        try:
            if flag == 1 and dato.strip() != "": return dato.title()
            elif flag == 2 and int(dato) > 0: return int(dato)
            elif flag in (3, 5) and dato.lower() in ("si", "no"): return dato.lower()
            elif flag == 4 and int(dato) in (1, 2, 3): return int(dato)
            else: raise ValueError
        except ValueError:
            print (f"Ingresa un valor valido.")
            if flag == 1: dato = str(input("Ingresa el nombre del producto: "))
            elif flag == 2: dato = int(input("Ingresa el valor del producto: "))
            elif flag == 3: dato = str(input("¿Desea seguir agregando productos al carrito? (si/no): "))
            elif flag == 4: dato = int(input("Ingrese una opción: "))
            elif flag == 5: dato = str(input("¿Desea salir? (si/no): "))

def agregar_producto(carrito):
    while True:
        producto = comprobar(str(input("Ingresa el nombre del producto: ")), 1)
        precio = comprobar(str(input("Ingresa el valor del producto: ")), 2)
        carrito.append((producto, precio))
        pregunta = comprobar(str(input("¿Desea seguir agregando productos al carrito? (si/no): ")), 3)
        if pregunta == "no": return carrito

def calcular_precio(carrito):
    return sum(precio for nombre, precio in carrito)

def aplicar_descuento(total):
    if total >= 100000: return total * 0.2
    elif total >= 50000: return total * 0.1
    else: return 0

def total_compra(carrito):
    sub_total = float(calcular_precio(carrito))
    descuento = float(aplicar_descuento(sub_total))
    total_final = float(sub_total - descuento)
    return (sub_total, descuento, total_final)

def detalle_compra(carrito):
    print("\n--- Detalle Compra ---\n")
    if not carrito: 
        print ("No hay productos comprados aun.")
        return
    for nombre, precio in carrito: print(f"{nombre} = ${float(precio):,.2f}", end="\n")
    sub_total, descuento, total_final = total_compra(carrito)
    if descuento == 0: acortar_cadena_decuento = f"{"No aplica descuento":>17}"
    else: acortar_cadena_decuento = f"{"$":>17}{descuento:,.2f}"
    print(f"""
Total de la Compra (Sin Descuento): ${sub_total:,.2f}
Descuento Aplicado: {acortar_cadena_decuento}
Total con Descuento Aplicado: {"$":>7}{total_final:,.2f}
    """)

def salir_menu(): 
    return comprobar(str(input("\n¿Desea salir? (si/no): ")), 5) == "si"

def mostrar_menu():
    print ("""
--- MENU ---

1. Agregar producto.
2. Ver detalle boleta.
3. Salir
    """)
    
def menu_compra():
    carrito = []
    while True:
        mostrar_menu()
        opcion = comprobar(str(input("Ingrese una opción: ")), 4)
        if opcion == 1: 
            producto = agregar_producto(carrito)
            if salir_menu(): continue
        elif opcion == 2: 
            detalle = detalle_compra(carrito)
            if salir_menu(): continue
        elif opcion == 3:
            print("¡Gracias por elegirnos!\nSaliendo...")
            return
            
# Main
menu_compra()
