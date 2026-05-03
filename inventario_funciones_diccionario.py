# ============================================================
# Archivo nuevo: inventario_funciones_diccionario.py
# Funciones auxiliares para visualizar y buscar productos
# Tienda Gifty
# ============================================================


def formatear_precio(precio):
    """
    Recibe un precio numérico y lo devuelve como texto con formato monetario.
    """
    return f"${precio:,.0f}".replace(",", ".")


def mostrar_producto(producto, numero=None):
    """
    Muestra en pantalla la información detallada de un producto.
    El producto debe ser un diccionario con las claves:
    codigo, nombre, precio y stock.
    """
    encabezado = f"Producto {numero}" if numero is not None else "Producto encontrado"

    print("\n------------ Gifty -------------")
    print(encabezado)
    print("Código:", producto["codigo"])
    print("Nombre:", producto["nombre"])
    print("Precio:", formatear_precio(producto["precio"]))
    print("Stock disponible:", producto["stock"])
    print("--------------------------------")


def visualizar_inventario(inventario):
    """
    Muestra todos los productos registrados en el inventario.
    Si el inventario está vacío, informa al usuario.
    """
    print("\n--- Visualización del inventario ---")

    if len(inventario) == 0:
        print("No hay productos registrados en el inventario.")
    else:
        for indice, producto in enumerate(inventario, start=1):
            mostrar_producto(producto, indice)


def buscar_por_codigo(inventario, codigo):
    """
    Busca un producto por código.
    Retorna el producto si lo encuentra.
    Si no lo encuentra, retorna None.
    """
    codigo = codigo.strip().lower()

    for producto in inventario:
        if producto["codigo"].strip().lower() == codigo:
            return producto

    return None


def buscar_por_nombre(inventario, nombre):
    """
    Busca productos por nombre.
    Permite coincidencias parciales.
    Por ejemplo, si se busca 'taza', encontrará 'Taza navideña'.
    Retorna una lista con los productos encontrados.
    """
    nombre = nombre.strip().lower()
    productos_encontrados = []

    for producto in inventario:
        if nombre in producto["nombre"].strip().lower():
            productos_encontrados.append(producto)

    return productos_encontrados


def buscar_producto_menu(inventario):
    """
    Permite buscar productos desde un pequeño menú.
    El usuario puede buscar por código o por nombre.
    """
    print("\n--- Búsqueda de productos ---")
    print("1. Buscar por código")
    print("2. Buscar por nombre")

    opcion = input("Seleccione una opción de búsqueda: ")

    if opcion == "1":
        codigo = input("Ingrese el código del producto: ")
        producto = buscar_por_codigo(inventario, codigo)

        if producto is None:
            print("No se encontró un producto con ese código.")
        else:
            mostrar_producto(producto)

    elif opcion == "2":
        nombre = input("Ingrese el nombre o parte del nombre del producto: ")
        productos = buscar_por_nombre(inventario, nombre)

        if len(productos) == 0:
            print("No se encontraron productos con ese nombre.")
        else:
            print(f"\nSe encontraron {len(productos)} producto(s):")
            for indice, producto in enumerate(productos, start=1):
                mostrar_producto(producto, indice)

    else:
        print("Opción de búsqueda no válida.")
