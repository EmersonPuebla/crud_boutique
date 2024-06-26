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

def confirm_uid(id, lista):
    """
        Confirma si el ID especificado existe o no en un archivo
    """

    x = search(id, lista)

    if x:
        False
    else:
        True

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
    with open(archivo, "w"):
        pass

    for line in range(len(lista)):
        data = lista[line]

        with open(archivo, "a") as file:
            if archivo == productos_file:
                file.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]}\n")
                
            elif archivo == ventas_file:
                file.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}\n")

def read(archivo, lista):
    if not len(lista) > 0:
        with open(archivo, "r") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")

                lista.extend([line])

        print(f"Se ha cargado la información del archivo '{archivo}' exitosamente")
    else:
        print(f"No se han cargado los datos del archivo '{archivo}' ya que la lista local ya contiene información")

def add_producto(stock, tipo, marca, categoria, talla, precio, descuento):
    id = productos_db[-1]
    id = int(id[0])

    # comprueba sí el id existe y en caso de existir le suma uno para evitar conflictos
    if confirm_uid(id, productos_db):
        pass
    else:
        id = id + 1

    productos_db.append([(str(id).zfill(4)),(str(stock).zfill(4)),tipo,marca,categoria,talla,precio,descuento])

def add_venta(id, date, quantity, total_price):
    folio = ventas_db[-1]
    folio = folio[0]
    folio = int(folio) + 1

    ventas_db.append([str(folio).zfill(4),id,date,quantity,total_price])
    
def search(id, lista):
    found_id = False
    for line in range(len(lista)):
        data = lista[line]
        id = str(id).zfill(4)

        if lista == productos_db:
            if id == data[0]:
                found_id = True
                print(f"ID: {data[0]}\nSTOCK: {data[1]}\nTIPO: {data[2]}\nMARCA: {data[3]}\nCATEGORÍA: {data[4]}\nTALLA: {data[5]}\nPRECIO: ${data[6]}\n%DESCUENTO: {data[7]}")
                break
        elif lista == ventas_db:
            if id == data[1]:
                found_id = True
                print(f"FOLIO: {data[0]}\nID: {data[1]}\nFECHA: {data[2]}\CANTIDAD: {data[3]}\nTOTAL: {data[4]}")
                break

    if found_id:
        return True
    
    if not found_id:
        print("No se ha encontrado un producto con el ID especificado")
        return False

def delete(id):
    for line in range(len(productos_db)):
        data = productos_db[line]
        id = str(id).zfill(4)

        if id == data[0]:
            productos_db.pop(line)

def modify(id, stock, tipo, marca, categoria, talla, precio, descuento):
    for line in range(len(productos_db)):
        data = productos_db[line]
        id = str(id).zfill(4)

        if id == data[0]:
            
            data[0] = (str(id).zfill(4))
            data[1] = (str(stock).zfill(4))
            data[2] = tipo
            data[3] = marca
            data[4] = categoria
            data[5] = talla
            data[6] = precio
            data[7] = descuento

            print("Se han modificado exitosamente los datos")
            break


def view_ventas():
    if len(ventas_db) > 0:
        print("Nº Folio - ID - Fecha - Cantidad - Total\n")
        for line in range(len(ventas_db)):
            data = ventas_db[line]

            print(f"{data[0]}   {data[1]}   {data[2]}   {data[3]}   ${data[4]}")
    else:
        print("No hay datos que mostrar")

def view_products():
    if len(productos_db) > 0:
        print("ID - Stock - Tipo - Marca - Categoría - Talla - Precio - %Descuento\n")
        for line in range(len(productos_db)):
            data = productos_db[line]

            print(f"{data[0]}    {data[1]}    {data[2]}    {data[3]}    {data[4]}    {data[5]}    ${data[6]}    {data[7]}")
    else:
        print("No hay datos que mostrar")

def view_date(date):
    if len(ventas_db) > 0:
        found_date = False
        print("Nº Folio - ID - Fecha - Cantidad - Total\n")
        for line in range(len(ventas_db)):
            data = ventas_db[line]


            if date == data[2]:
                print(f"{data[0]}   {data[1]}   {data[2]}   {data[3]}   ${data[4]}")
                found_date = True
        
        if not found_date:
            print(f"No se registraron ventas en la fecha {date}")
    else:
        print("No hay datos que mostrar")

def view_date_range(date_1, date_2):
    if len(ventas_db) > 0:
        found_date = False
        print("Nº Folio - ID - Fecha - Cantidad - Total\n")
        
        date_1 = date_1.split("-")
        date_1 = int(date_1[0])

        date_2 = date_2.split("-")
        date_2 = int(date_2[0])

        for line in range(len(ventas_db)):
            data = ventas_db[line]

            date = data[2]
            date = date.split("-")
            date = int(date[0])

            if range(date_1, date_2) == date:
                print(f"{data[0]}   {data[1]}   {data[2]}   {data[3]}   ${data[4]}")
                found_date = True
        
        if not found_date:
            print(f"No se registraron ventas en la fecha {date}")
    else:
        print("No hay datos que mostrar")

def sell(id, quantity):
    switch = False

    for line in range(len(productos_db)):
        data = productos_db[line]
        id = str(id).zfill(4)

        if str(data[0]) == id:
            
            stock = int(data[1])
            new_stock = stock - quantity
            data[1] = new_stock
            price = int(data[6])
            discount = int(data[7]) 
            total_price = round((((100 - discount) / 100) * price) * quantity)
            quantity = str(quantity).zfill(4)
            
            # hasta aquí good

            if new_stock >= 0:

                modify(id, str(new_stock), str(data[2]), str(data[3]), str(data[4]), str(data[5]), str(data[6]), str(data[7]))

                date = datetime.now().strftime("%d-%m-%Y")

                add_venta(id, date, quantity, total_price)

                switch = True

            else:
                print("ERROR: No puedes vender mas de lo que tienes")
                switch = False


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
                clear()
                print("¤═════════¤ Venta ¤═════════¤\n")
                id = int(input("════════¤ ID del producto: ¤════════\n"))
                quantity = int(input("════════¤ Ingrese la cantidad: ¤════════\n"))

                if confirm():
                    if sell(id, quantity):
                        pause()                

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
                        date = input("════════¤ Ingrese la fecha de ventas a buscar en formato \"dd-mm-aa\": ¤════════\n")
                        x, reason = confirm_date(date)
                        if x == 1:
                            view_date(date)
                        elif x == -1:
                            print(reason)
                            
                        pause()

                    case 3:

                        switch_1 = False
                        switch_2 = False
                        
                        clear()
                        date_1 = input("════════¤ Ingrese la primera fecha del rango en formato: \"dd-mm-aa\": ¤════════\n")

                        x, reason = confirm_date(date_1)
                        if x == 1:
                            view_date(date_1)
                            switch_1 = True
                        elif x == -1:
                            print(reason)

                        date_2 = input ("════════¤ Ingrese la segunda fecha del rango en formato: \"dd-mm-aa\": ¤════════\n")
                        
                        x, reason = confirm_date(date_2)
                        if x == 1:
                            view_date(date_2)
                            switch_2 = True
                        elif x == -1:
                            print(reason)
                        
                        if switch_1 and switch_2:
                            view_date_range(date_1, date_2)
                        else:
                            pass

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
                        search(id, productos_db)
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
                        read(productos_file, productos_db)
                        read(ventas_file, ventas_db)
                        pause()

                    case 2:
                        write(productos_file, productos_db)
                        write(ventas_file, ventas_db)
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