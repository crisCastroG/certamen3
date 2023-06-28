import os
os.system("cls")

listaCod = []
listaNom = []
listaCat = []
listaPrec = []
listaStk = []
nomUsuario = "Cristian"


def registrarProduc():
    while True:
        try:
            cod = int(input("Ingrese el código: "))
            if len(str(cod)) < 6 or len(str(cod)) > 6:
                print("El código debe ser de 6 digitos, intente nuevamente")
                input()
                os.system("cls")
            else:
                listaCod.append(cod)
                os.system("cls")
                break
        except:
            print("EXCEPCION CODIGO")
            input()
            os.system("cls")
    while True:
        nom = input("Ingrese el nombre: ")
        if len(nom) < 2 or len(nom) > 50:
            print("El nombre debe tener entre 2 y 50 caracteres, intente nuevamente")
            input()
            os.system("cls")
        else:
            listaNom.append(nom)
            os.system("cls")
            break
    while True:
        cat = input("Ingrese categoría: ")
        if cat.lower() != "paquete" and cat.lower() != "sobre":
            print("La categoria debe ser Sobre o Paquete, intente nuevamente")
            input()
            os.system("cls")
        else:
            listaCat.append(cat)
            os.system("cls")
            break
    while True:
        try:
            prec = int(input("Ingrese precio: "))
            if prec <= 0:
                print("El precio debe ser mayor a 0 , intente nuevamente")
                input()
                os.system("cls")
            else:
                listaPrec.append(prec)
                os.system("cls")
                break
        except:
            print("EXCEPCION PRECIO")
            input()
            os.system("cls")
    while True:
        try:
            stck = int(input("Ingrese stock disponible: "))
            if stck <= 0:
                print("El stock debe ser mayor a 0, intente nuevamente")
                input()
                os.system("cls")
            else:
                listaStk.append(stck)
                os.system("cls")
                break
        except:
            print("EXCEPCION STOCK, DEBE INGRESAR NUMERO ENTERO")
            input()
            os.system("cls")    


def buscarProduc():
    cat = input("Ingrese categoría para buscar: ")
    os.system("cls")
    print("""
                RESULTADO BUSQUEDA
-------------------------------------------------------
COD    NOMBRE               CATEGORIA  PRECIO     STOCK  """)
    for i in range(len(listaCat)):
        if listaCat[i].upper() == cat.upper():
            print(f"{listaCod[i]:6d} {listaNom[i]:20s} {listaCat[i]:10s} {format(listaPrec[i]):10s} {format(listaStk[i])}")
    input("")
    os.system("cls")

def listarProduc():
    stockBajo = ""
    contBajo = 0
    print("""
                    LISTADO DE PRODUCTOS
-----------------------------------------------------------------
COD    NOMBRE               CATEGORIA  PRECIO     STOCK  STOCKBAJO""")
    for i in range(len(listaCod)):
        if listaStk[i] < 5:
            stockBajo = "SI"
            contBajo += 1
        else:
            stockBajo = "NO"
        print(f"{listaCod[i]:6d} {listaNom[i]:20s} {listaCat[i]:10s} {format(listaPrec[i]):10s} {format(listaStk[i]):6s} {stockBajo}")
    print(f"PRODUCTOS CON STOCK BAJO: {contBajo}")
    input("")
    os.system("cls")


print(f"Bienvenido al programa de registro, {nomUsuario}")
while True:
    print("""
    MENU
1) Registrar producto
2) Buscar productos
3) Listar productos
4) Salir""")
    try:
        opc = int(input("Seleccione una opción: "))
        if opc < 1 or opc > 4:
            print("Opción inválida, elija nuevamente")
            input("")
            os.system("cls")
        elif opc == 1:
            os.system("cls")
            registrarProduc()
        elif opc == 2:
            os.system("cls")
            buscarProduc()
        elif opc == 3:
            os.system("cls")
            listarProduc()
        elif opc == 4:
            break
    except:
        print("EXCEPCION OPCION")
        input("")
        os.system("cls")
print(f"Cerrando programa... Hasta luego, {nomUsuario}")
input("")

    


