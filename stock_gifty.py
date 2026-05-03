# ============================================================
# Control de stock y reportes - Tienda Gifty


def revisar_stock_bajo(inventario):
    print("\n--- Productos con stock bajo ---")

    hay_stock_bajo = False

    for producto in inventario:
        if producto["stock"] < 5:
            print("Producto:", producto["nombre"])
            print("Código:", producto["codigo"])
            print("Stock actual:", producto["stock"])
            print("-----------------------------")
            hay_stock_bajo = True

    if hay_stock_bajo == False:
        print("No hay productos con stock bajo.")


def registrar_venta(inventario):
    print("\n--- Registrar venta ---")

    codigo = input("Ingrese el código del producto vendido: ")

    producto_encontrado = None

    for producto in inventario:
        if producto["codigo"] == codigo:
            producto_encontrado = producto

    if producto_encontrado is None:
        print("Producto no encontrado.")
    else:
        cantidad = int(input("Ingrese cantidad vendida: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")

        elif cantidad > producto_encontrado["stock"]:
            print("No hay stock suficiente para realizar la venta.")
            print("Stock disponible:", producto_encontrado["stock"])

        else:
            producto_encontrado["stock"] = producto_encontrado["stock"] - cantidad
            producto_encontrado["vendidos"] = producto_encontrado["vendidos"] + cantidad

            print("Venta registrada correctamente.")
            print("Nuevo stock:", producto_encontrado["stock"])

            if producto_encontrado["stock"] < 5:
                print("ALERTA: Este producto quedó con stock bajo.")


def generar_reporte(inventario):
    print("\n========== REPORTE DE INVENTARIO GIFTY ==========")

    total_productos = len(inventario)
    print("Total de productos registrados:", total_productos)

    if total_productos == 0:
        print("No hay productos para reportar.")
    else:
        total_unidades = 0

        for producto in inventario:
            total_unidades = total_unidades + producto["stock"]

        print("Total de unidades disponibles:", total_unidades)

        print("\n--- Productos con stock bajo ---")

        hay_stock_bajo = False

        for producto in inventario:
            if producto["stock"] < 5:
                print(producto["nombre"], "- Stock:", producto["stock"])
                hay_stock_bajo = True

        if hay_stock_bajo == False:
            print("No hay productos con stock bajo.")

        print("\n--- Producto más vendido ---")

        producto_mas_vendido = inventario[0]

        for producto in inventario:
            if producto["vendidos"] > producto_mas_vendido["vendidos"]:
                producto_mas_vendido = producto

        print("Producto:", producto_mas_vendido["nombre"])
        print("Unidades vendidas:", producto_mas_vendido["vendidos"])

    print("=================================================")