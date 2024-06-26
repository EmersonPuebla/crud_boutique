import os
from datetime import datetime

version = "2"

productos_file = "productos.txt"
ventas_file = "ventas.txt"

productos_db = []
ventas_db = []

def clear():
    os.system("cls")

def pause():
    os.system("pause")

def confirm_date(date):
    try:
        switch = True
        reason = ""

        # comprobar formato
        if not ((date[2] and date[5]) == "-"):
            reason = "No cuenta con el formato adecuado (dd-mm-aa)"
            switch = False

        day = int(date[0:2])
        month = int(date[3:5]) 
        year = int(date[6:10])

        # comprobar si el str de la fecha tiene 10 caracteres de largo
        if len(date) != 10:
            reason = "No cuenta con la cantidad de caracteres esperados (10)"
            switch = False

        # comprobar si el dia esta entre 1 y 31
        if not (1 <= int(day) <= 31):
            reason = "El dia no se encuentra en el rango de 1-31"
            switch = False

        # comprobar si el mes esta entre 1 y 12 
        if not (1 <= int(month) <= 12):
            reason = "El mes no se encuentra en el rango de 1-12"
            switch = False

        # comprobar si es mayor o igual al año 2000
        if not int(year) >= 2000:
            reason = "El año no es mayor o igual al 2000"
            switch = False

        # comprobar si es bisiesto
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            # bisiesto
            if month == 2 and day > 29:
                reason = "El dia no puede ser mayor a 29 en Febrero"
                switch = False
        else:
            # no bisiesto
            if month == 2 and day > 28:
                reason = "El dia no puede ser mayor a 28 en Febrero en un año bisiesto"
                switch = False
                
    except ValueError as e:
        pass

    if switch:
        return 1, reason
    else:
        return -1, reason

def confirm():
    switch = False
    while True:
        reply = input("════════¤ Confirme la operación (si/no): ¤════════\n").lower()

        if reply == "s" or reply == "si":
            switch = True
            break

        elif reply == "n" or reply == "no":
            print("\n════════¤ Operación cancelada ¤════════\n")
            pause()
            break
    
        else:
            clear()
            print("\n════════¤ ERROR: Ingrese una opción valida ¤════════\n")
            pause()

    if switch:
        return 1
    else:
        return -1

def write(archivo, lista):
    #print(f"FUNC WRITE:\nArchivo: {archivo}\nLista: {lista}\n---")

    #print("FUNC WRITE: Borrar contenido del archivo")
    with open(archivo, "w"):
        pass

    for x in range(0, len(lista)):
        #print(f"FUNC WRITE: pase por la linea {x}")
        data = lista[x]
        data = data[0]
        data = data.split(",")
        #print(f"FUNC WRITE: {data}")

        with open(archivo, "a") as file:
            #print(f"FUNC WRITE: Imprimí el contenido de la linea {data[0]}")

            if archivo == productos_file:
                try:
                    file.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]}\n")
                except IndexError as e:
                    print(f"ERROR: Write function -> if: {e}")
                
            elif archivo == ventas_file:
                try:
                    file.write(f"{data[0]},{data[1]},{data[2]},{data[3]}\n")
                except IndexError as e:
                    print(f"ERROR: Write function -> if: {e}")

    pause()

def read(archivo, lista):
    #print("FUNC READ: Lista original")
    print(lista)
    
    with open(archivo, "r") as file:
        for line in file:
            line = line.strip()
            #print(f"FUNC READ: Se hizo un strip (linea: {line[0]})")

            lista.append([line])
            #print(f"FUNC READ: Se hizo un append (linea: {line[0]})")
    
    for x in range(0, len(lista)):
        #print(f"---\nFUNC READ: Se imprimió la linea {line[0]}")
        print(lista[x])

        #print("---\nFUNC READ: Lista actualizada:")
        print(lista)

    pause()

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
            file.write(f"{str(id).zfill(4)},{str(stock).zfill(4)},{tipo},{marca},{categoria},{talla},{precio},{descuento}")
        else:
            file.write(f"\n{str(id).zfill(4)},{str(stock).zfill(4)},{tipo},{marca},{categoria},{talla},{precio},{descuento}")

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
    if not os.stat(ventas_file).st_size == 0:
        print("Nº Folio - ID - Fecha - Cantidad - Total\n")
        with open(ventas_file, "r") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")
                data = line

                print(f"{data[0]}   {data[1]}   {data[2]}   {data[3]}   ${data[4]}")
    else:
        print("No hay datos que mostrar")

def view_products():
    if not os.stat(ventas_file).st_size == 0:
        print("ID - Stock - Tipo - Marca - Categoría - Talla - Precio - %Descuento\n")
        with open(productos_file, "r") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")
                data = line
                
                print(f"{data[0]}    {data[1]}    {data[2]}    {data[3]}    {data[4]}    {data[5]}    ${data[6]}    {data[7]}")
    else:
        print("No hay datos que mostrar")

def view_date(date):
    if not os.stat(ventas_file).st_size == 0:
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
    else:
        print("No hay datos que mostrar")

def view_date_range(date_1, date_2):
    if not os.stat(ventas_file).st_size == 0:
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
    else:
        print("No hay datos que mostrar")

def sell(id, quantity):
    switch = False
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
                    modify(str(id).zfill(4), str(new_stock), str(data[2]), str(data[3]), str(data[4]), str(data[5]), str(data[6]), str(data[7]))
                    with open(ventas_file, "r") as file:
                        for line in file:
                            pass
                        line = line.strip()
                        line = line.split(",")
                        folio = int(line[0])
                        new_folio = folio + 1

                    with open(ventas_file, 'a') as file:  
                        date = datetime.now().strftime("%d-%m-%Y")

                        file.write(f"\n{str(new_folio).zfill(4)},{str(id).zfill(4)},{date},{str(quantity).zfill(4)},{round(total_price)}")
                    switch = True
                else:
                    print("ERROR: No puedes vender mas de lo que tienes")
                    switch = False
        pause()

    return switch

clear()
print(f"""
¤═════════════════════════════════════════════¤
║ ______             _   _                    ║
║ | ___ \           | | (_)                   ║
║ | |_/ / ___  _   _| |_ _  __ _ _   _  ___   ║
║ | ___ \/ _ \| | | | __| |/ _` | | | |/ _ \\  ║
║ | |_/ / (_) | |_| | |_| | (_| | |_| |  __/  ║
║ \____/ \___/ \__,_|\__|_|\__, |\__,_|\___|  ║
║ Sistema de ventas           | |             ║
║                             |_|             ║
¤═════════════════════════════════════════════¤    
║ Luis Alvarez                                ║
║ Emerson Puebla                              ║
¤═════════════════════════════════════════════¤
║ version {version}                                   ║
¤═════════════════════════════════════════════¤
""")
pause()

while True:
    try: 
        hour = str((datetime.now()).strftime("%d-%m-%Y"))
        clear()
        i_menu = int(input(f"""
        ¤═════════¤ Boutique ¤═════════¤
        ║ {hour}        version  {version} ║
        ¤══════════════════════════════¤
        ║ 1) Vender                    ║
        ║ 2) Reportes                  ║
        ║ 3) Mantenedor                ║
        ║ 4) Administración            ║
        ║ 5) Salir                     ║
        ¤══════════════════════════════¤
        ║ Ingrese un numero entre 1-5: ║ 
        ¤══════════════════════════════¤
        """))

        match i_menu:
            case 1:
                while True:
                    clear()
                    print("¤═════════¤ Venta ¤═════════¤\n")

                    id = int(input("════════¤ ID del producto: ¤════════\n"))
                    quantity = int(input("════════¤ Ingrese la cantidad: ¤════════\n"))

                    x = confirm()
                    if x:
                        if sell(id, quantity):
                            break
                        else:
                            pass    
                    else:
                        pass

            case 2:
                clear()
                i_report = int(input("""
                ¤══════════¤ Reportes ¤══════════¤
                ║ 1) General de ventas           ║
                ║ 2) Ventas por fecha especifica ║
                ║ 3) Ventas por rango de fecha   ║
                ║ 4) Salir al menu principal     ║
                ¤════════════════════════════════¤
                ║  Ingrese un numero entre 1-4:  ║ 
                ¤════════════════════════════════¤
                """))

                match i_report:
                    case 1:
                        clear()
                        view_ventas()
                        pause()                   
                        
                    case 2:
                        clear()
                        date = input("════════¤ Ingrese la fecha de ventas a buscar en formato \"DIA/MES/AÑO\": ¤════════\n")
                        view_date(date)

                        pause()

                    case 3:
                        clear()
                        date_1 = input("════════¤ Ingrese la primera fecha del rango en formato: \"DIA/MES/AÑO\": ¤════════\n")
                        date_2 = input ("════════¤ Ingrese la segunda fecha del rango en formato: \"DIA/MES/AÑO\": ¤════════\n")
                        view_date_range(date_1, date_2)

                        pause()
                    case 4:
                        pass

            case 3:
                clear()
                print("")
                i_crud = int(input("""
                ¤═════════¤ Mantenedor ¤═════════¤
                ║ 1) Agregar                     ║
                ║ 2) Eliminar                    ║
                ║ 3) Editar                      ║
                ║ 4) Buscar                      ║
                ║ 5) Listar                      ║
                ║ 6) Salir al menu principal     ║       
                ¤════════════════════════════════¤
                ║  Ingrese un numero entre 1-6:  ║ 
                ¤════════════════════════════════¤
                """))

                match i_crud:
                    case 1:
                        stock = input("════════¤ Cantidad de stock del producto: ¤════════\n").lower()
                        tipo = input("════════¤ Tipo de prenda (pantalon, polera, etc): ¤════════\n").lower()
                        marca = input("════════¤ Marca de la prenda: ¤════════ \n").lower()
                        categoria = (input("════════¤ Categoría de la prenda (niño, adulto, etc): ¤════════\n").lower()).replace("ñ", "n")
                        talla = input("════════¤ Talla del producto: ¤════════\n").lower()
                        precio = input("════════¤ Ingrese el valor: ¤════════\n").lower()
                        descuento = (input("════════¤ %Descuento del producto (si no posee ingrese 0): ¤════════\n")).lower()

                        add_producto(stock, tipo, marca, categoria, talla, precio, descuento)

                    case 2:
                        id = input("Ingrese el ID del producto a eliminar: ")
                        delete(id)

                        pause()
                    case 3:
                        clear()
                        id = input("════════¤ Ingrese el ID del producto a modificar: ¤════════\n")
                        stock = input("════════¤ Cantidad de stock del producto: ¤════════\n").lower()
                        tipo = input("════════¤ Tipo de prenda (pantalon, polera, etc): ¤════════\n").lower()
                        marca = input("════════¤ Marca de la prenda: ¤════════ \n").lower()
                        categoria = (input("════════¤ Categoría de la prenda (niño, adulto, etc): ¤════════\n").lower()).replace("ñ", "n")
                        talla = input("════════¤ Talla del producto: ¤════════\n").lower()
                        precio = input("════════¤ Ingrese el valor: ¤════════\n").lower()
                        descuento = (input("════════¤ %Descuento del producto (si no posee ingrese 0): ¤════════\n")).lower()
                        modify(id, stock, tipo, marca, categoria, talla, precio, descuento)
                        pause()

                    case 4:
                        clear()
                        id = input("════════¤ Ingrese el ID del producto a buscar: ¤════════\n")
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
                Observaciones: Debe tener presente si su lista de productos y 
                            ventas ya tienen datos entonces NO debe cargar los datos desde el txt
                
                """
                clear()
                i_report = int(input("""
                ¤═══════¤ Administración ¤═══════¤
                ║ 1) Cargar datos                ║
                ║ 2) Respaldar datos             ║
                ║ 3) Salir al menu principal     ║       
                ¤════════════════════════════════¤
                ║  Ingrese un numero entre 1-3:  ║ 
                ¤════════════════════════════════¤
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
                print("════════¤ Fin del programa ¤════════")
                break
            
            case _:
                pass

    except ValueError:
        print("Solo puede ingresar un numero entre 1-5")
        pause()
    
    except:
        pass