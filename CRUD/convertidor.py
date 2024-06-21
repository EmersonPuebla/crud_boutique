"""
1,1,pantalon,fashion park,adulto,s,13990,0
2,10,pantalon,h&m,adulto,xxl,9990,0
3,25,chaqueta,adidas,infantil,12,16990,0

"""
import os

def clear():
    os.system("cls")

def pause():
    os.system("pause")

productos_db = []
ventas_db = []

productos_file = "productos.txt"
ventas_file = "ventas.txt"


def write(archivo, lista):
    print(f"FUNC WRITE:\nArchivo: {archivo}\nLista: {lista}\n---")

    print("FUNC WRITE: Borrar contenido del archivo")
    with open(archivo, "w"):
         pass

    for x in range(0, len(lista)):
        print(f"FUNC WRITE: pase por la linea {x}")
        data = lista[x]
        data = data[0]
        data = data.split(",")
        print(f"FUNC WRITE: {data}")

        with open(archivo, "a") as file:
            print(f"FUNC WRITE: Imprimi el contenido de la linea {data[0]}")

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
    print("FUNC READ: Lista original")
    print(lista)
    
    with open(archivo, "r") as file:
        for line in file:
            line = line.strip()
            print(f"FUNC READ: Se hizo un strip (linea: {line[0]})")

            lista.append([line])
            print(f"FUNC READ: Se hizo un append (linea: {line[0]})")
    
    for x in range(0, len(lista)):
        print(f"---\nFUNC READ: Se imprimio la linea {line[0]}")
        print(lista[x])

        print("---\nFUNC READ: Lista actualizada:")
        print(lista)

    pause()


while True:
    clear()
    i_menu = int(input("""
    1) Cargar
    2) Guardar
    3) Imprimir lista productos 
    4) Imprimir lista ventas
    5) Añadir algo a la lista
    6) Salir

    """))

    match i_menu:
        case 1:
            read(productos_file, productos_db)

        case 2:
            write(productos_file, productos_db)

        case 3:
            print(productos_db)
            pause()

        case 4:
            print(ventas_db)
            pause()

        case 5:
            productos_db.append(["1,2,3,4,5,6,7,8"])

        case 6:
            clear()
            break