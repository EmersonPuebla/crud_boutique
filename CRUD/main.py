import os
from datetime import datetime

version = "2"

productos_file = "productos.txt"
ventas_file = "ventas.txt"

def clear():
    os.system("cls")

def pause():
    os.system("pause")

def add_producto(stock, tipo, marca, categoria, talla, precio, descuento):
    with open(productos_file, "r") as file:
        for line in file:
            pass

        try:
            line = line.split(",")
            id = int(line[0])
            id = id + 1
        except UnboundLocalError:
            id = 1

    with open(productos_file, 'a') as file:  
        if id == 1:
            file.write(f"{id},{stock},{tipo},{marca},{categoria},{talla},{precio},{descuento}")
        else:
            file.write(f"\n{id},{stock},{tipo},{marca},{categoria},{talla},{precio},{descuento}")

def search(id):
    found_id = False
    with open(productos_file, "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")
            data = line

            if id in data[0]:
                found_id = True
                print(f"ID: {data[0]}\nSTOCK: {data[1]}\nTIPO: {data[2]}\nMARCA: {data[3]}\nCATEGORÍA: {data[4]}\nTALLA: {data[5]}\nPRECIO: ${data[6]}\n%DESCUENTO: {data[7]}")
                break
    if found_id:
        return True
    
    if not found_id:
        print("No se ha encontrado un producto con el ID especificado")

def delete(id):
    new_data = []
    exist = search(id)

    if exist:
        with open(productos_file, 'r') as file:
            for line in file:
                line = line.strip()
                data = line.split(',')
                if data[0] != id:
                    new_data.append(line)

        with open(productos_file, 'w') as file:
            for line in new_data:
                file.write(line + '\n')

def modify(id, stock, tipo, marca, categoria, talla, precio, descuento):
    new_data = []
    found_id = False
    
    # Abrimos el archivo en modo lectura
    with open(productos_file, 'r') as file:
        for line in file:
            line = line.strip()
            data = line.split(',')

            if data[0] == id:
                data[1] = stock
                data[2] = tipo
                data[3] = marca
                data[4] = categoria
                data[5] = talla
                data[6] = precio
                data[7] = descuento
                
                found_id = True
            new_data.append(','.join(data))
    
    if not found_id:
        return False
    
    with open(productos_file, 'w') as file:
        for line in new_data:
            file.write(line + '\n')

def view_ventas():
    print("Nº Folio - ID - Fecha - Cantidad - Total\n")
    with open(ventas_file, "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")
            data = line

            print(f"{data[0]}   {data[1]}   {data[2]}   {data[3]}   ${data[4]}")

def view_products():
    print("ID - Stock - Tipo - Marca - Categoría - Talla - Precio - %Descuento\n")
    with open(productos_file, "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")
            data = line
            
            print(f"{data[0]}    {data[1]}    {data[2]}    {data[3]}    {data[4]}    {data[5]}    ${data[6]}    {data[7]}")

def view_date(date):
    found_date = False
    print("Nº Folio - ID - Fecha - Cantidad - Total\n")
    with open(ventas_file, "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")
            data = line

            if date in data[2]:
                print(f"{data[0]}   {data[1]}   {data[2]}   {data[3]}   ${data[4]}")
                found_date = True
        
        if not found_date:
            print(f"No se registraron ventas en la fecha {date}")

def view_date_range(date_1, date_2):
    found_date = False
    print("Nº Folio - ID - Fecha - Cantidad - Total\n")
    with open(ventas_file, "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")
            data = line

            if date_1 in data[2]:
                print(f"{data[0]}   {data[1]}   {data[2]}   {data[3]}   ${data[4]}")
                found_date = True

            if date_2 in data[2]:
                print(f"{data[0]}   {data[1]}   {data[2]}   {data[3]}   ${data[4]}")
                found_date = True

        if not found_date:
            print(f"No se registraron ventas en la fecha {date}")

def sell(id, quantity):
    with open(productos_file, "r") as file:
        for line in file:
            line = line.strip()
            data = line.split(",")

            if int(data[0]) == id:
                stock = int(data[1])
                new_stock = stock - quantity
                data[1] = new_stock
                price = int(data[6])
                discount = int(data[7])

                total_price = (((100 - discount) / 100) * price) * quantity
                
                if new_stock >= 0:
                    modify(str(id), str(new_stock), str(data[2]), str(data[3]), str(data[4]), str(data[5]), str(data[6]), str(data[7]))
                    with open(ventas_file, "r") as file:
                        for line in file:
                            pass
                        line = line.strip()
                        line = line.split(",")
                        folio = int(line[0])
                        new_folio = folio + 1

                    with open(ventas_file, 'a') as file:  
                        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                        file.write(f"\n{new_folio},{id},{date},{quantity},{round(total_price)}")
                else:
                    print("ERROR: No puedes vender mas de lo que tienes")
        pause()

while True:
    hour = str((datetime.now()).strftime("%d/%m/%Y"))
    clear()
    i_menu = int(input(f"""
    {hour} 
    version: {version}
    -------------- << "Boutique" >> --------------
    1) Vender
    2) Reportes
    3) Mantenedor
    4) Administración
    5) Salir 

    Ingrese un numero entre 1-5:                    
    """))
    # Falta terminar administración 
    
    match i_menu:
        case 1:
            clear()
            print("-------------- << \"Venta\" >> --------------\n")

            id = int(input("ID del producto: "))
            quantity = int(input("Ingrese la cantidad: "))

            sell(id, quantity)      

        case 2:
            clear()
            i_report = int(input("""
    -------------- << \"Reportes\" >> --------------
    1) General de ventas
    2) Ventas por fecha especifica
    3) Ventas por rango de fecha
    4) Salir al menu principal

    Ingrese un numero entre 1-4: 
            """))

            match i_report:
                case 1:
                    clear()
                    view_ventas()
                    pause()                   
                    
                case 2:
                    clear()
                    date = input("Ingrese la fecha de ventas a buscar en formato \"DIA/MES/AÑO\": ")
                    view_date(date)

                    pause()

                case 3:
                    clear()
                    date_1 = input("Ingrese la primera fecha del rango en formato: \"DIA/MES/AÑO\": ")
                    date_2 = input ("Ingrese la segunda fecha del rango en formato: \"DIA/MES/AÑO\": ")
                    view_date_range(date_1, date_2)

                    pause()
                case 4:
                    pass

        case 3:
            clear()
            print("")
            i_crud = int(input("""
    -------------- << \"Mantenedor\" >> --------------
    1) Agregar
    2) Eliminar
    3) Editar
    4) Buscar
    5) Listar
    6) Salir al menu principal

    Ingrese un numero entre 1-6: 
            """))

            match i_crud:
                case 1:
                    stock = input("Cantidad de stock del producto: \n").lower()
                    tipo = input("Tipo de prenda (pantalon, polera, etc): \n").lower()
                    marca = input("Marca de la prenda: \n").lower()
                    categoria = (input("Categoría de la prenda (niño, adulto, etc): \n").lower()).replace("ñ", "n")
                    talla = input("que talla es el producto: \n").lower()
                    precio = input("Ingrese el valor: \n").lower()
                    descuento = (input("%Descuento del producto (si no posee ingrese 0): \n")).lower()

                    add_producto(stock, tipo, marca, categoria, talla, precio, descuento)

                case 2:
                    id = input("Ingrese el ID del producto a eliminar: ")
                    delete(id)

                    pause()
                case 3:
                    clear()
                    id = input("Ingrese el ID del producto a modificar: ")
                    stock = input("Cantidad de stock del producto: \n").lower()
                    tipo = input("Tipo de prenda (pantalon, polera, etc): \n").lower()
                    marca = input("Marca de la prenda: \n").lower()
                    categoria = (input("Categoría de la prenda (niño, adulto, etc): \n").lower()).replace("ñ", "n")
                    talla = input("que talla es el producto: \n").lower()
                    precio = input("Ingrese el valor: \n").lower()
                    descuento = (input("%Descuento del producto (si no posee ingrese 0): \n")).lower()
                    modify(id, stock, tipo, marca, categoria, talla, precio, descuento)
                    pause()

                case 4:
                    clear()
                    id = input("Ingrese el ID del producto a buscar: ")
                    search(id)
                    pause()

                case 5:
                    clear()
                    view_products()
                    pause()
                case 6:
                    pass
        
        case 4:
            """         
            1. Cargar datos
            2. Respaldar datos
            3. Salir

            Cargar datos: Esto lee todo lo que contienen los archivos productos.txt y ventas.txt y carga las listas y ventas.

            Respaldar datos: Esta opción actualiza todo lo contenido 

            Observaciones: Debe tener presente si su lista de productos y 
                        ventas ya tienen datos entonces NO debe cargar los datos desde el txt
            
            """
            clear()
            print("-------------- << \"Administración\" >> --------------  ")
            i_report = int(input("""
            1) Cargar datos
            2) Respaldar datos
            3) Salir al menu principal
                    
            Ingrese un numero entre 1-3: 
            """))

            match i_report:
                case 1:
                    pass
                case 2:
                    pass
                case 3: 
                    pass

        case 5:
            clear()
            print("Fin del programa")
            break
        
        case _:
            pass