# Trabajo en equipo,curso 2: Gestión de inventario - Tienda Gifty
#Grupo 3: Rodrigo, Miguel, Emilio
#Fecha entrega: 3 de mayo 2026

# Inventario inicial vacío 
inventario = []


def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO GIFTY =====")
    print("Bienvenido")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")


def agregar_producto():
    print("\n--- Agregar nuevo producto ---")
    
    codigo = input("Ingrese código del producto: ")
    nombre = input("Ingrese nombre del producto: ")
    precio = float(input("Ingrese precio del producto: "))
    stock = int(input("Ingrese cantidad en stock: "))
    
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    
    inventario.append(producto)
    print("Producto agregado correctamente.")


def ver_inventario():
    print("\n--- Inventario actual ---")
    
    if len(inventario) == 0:
        print("No hay productos registrados.")
    else:
        for producto in inventario:
            print("------------Gifty---------------")
            print("Código:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Precio: $", producto["precio"])
            print("Stock:", producto["stock"])
            print("------------Gifty---------------")


def buscar_producto(codigo):
    for producto in inventario:
        if producto["codigo"] == codigo:
            return producto
    return None


def actualizar_producto():
    print("\n--- Actualizar producto ---")
    
    codigo = input("Ingrese el código del producto a actualizar: ")
    producto = buscar_producto(codigo)
    
    if producto is None:
        print("Producto no encontrado.")
    else:
        print("Producto encontrado:", producto["nombre"])
        
        nuevo_nombre = input("Ingrese nuevo nombre: ")
        nuevo_precio = float(input("Ingrese nuevo precio: "))
        nuevo_stock = int(input("Ingrese nuevo stock: "))
        
        producto["nombre"] = nuevo_nombre
        producto["precio"] = nuevo_precio
        producto["stock"] = nuevo_stock
        
        print("Producto actualizado correctamente.")


def eliminar_producto():
    print("\n--- Eliminar producto ---")
    
    codigo = input("Ingrese el código del producto a eliminar: ")
    producto = buscar_producto(codigo)
    
    if producto is None:
        print("Producto no encontrado.")
    else:
        inventario.remove(producto)
        print("Producto eliminado correctamente.")


#Menu
opcion = ""

while opcion != "5":
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_inventario()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("Gracias por usar el sistema de inventario Gifty.")
    else:
        print("Opción no válida. Intente nuevamente.")