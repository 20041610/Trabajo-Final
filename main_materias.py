from academia import BaseDeDatos
from academia import Materias
base_de_datos = BaseDeDatos()
objeto_academia2 = Materias(base_de_datos)


menu = '''
                                                    *****************************************
                                                    *             Menu Materias             *
                                                    *****************************************
                                                    *                                       *
                                                    * 1) Insertar Materias                  *
                                                    * 2) Deshabilitar Materias              *
                                                    * 3) Modificar Materias                 *
                                                    * 4) Ver lista de Materias              *
                                                    * 5) Salir                              *
                                                    *****************************************

'''

def main():
    opcion = 0
    while(not opcion ==5 ):
        print(menu)
        while True:
            try:
                opcion= int(input("Ingrese una opcion del menu:"))
                break
            except ValueError:
                print("Ingrese una opcion del 1 al 5")

        if(opcion == 1):
            insertar_materias()
        if (opcion == 2):
            dar_baja_materias()
        if(opcion == 3):
            modificar_materias()
        if(opcion ==4):
            ver_materias()
            input("ENTER para continuar")
        if(opcion == 5):
            print("Saliendo del programa")
def insertar_materias():
    print("Insertar materias")
    continuar = "s"
    while(continuar == "s"):
        materia = input("Inserte el nombre de la materia: ").strip().title()
        materia_ingresada = objeto_academia2.validar_materia(materia)
        if(materia_ingresada):
            print(f"Materia {materia} fue ingresada correctamente. ")
            objeto_academia2.insertar_materias(materia)
            input("ENTER para continuar")
            break

        continuar = input("Seguir insertando materias? s/n: ").strip().lower()

def dar_baja_materias():
    continuar = "s"
    while(continuar == "s"):
        registros = objeto_academia2.ver_materias()
        if(not registros):
            print("No hay datos en la base de datos. Use la opcion 1 para insertar datos.")
            input("ENTER para continuar")
            break
        else:
            ver_materias()
            try:
                id_a_borrar = int(input("\nIngrese el id de la materia a deshabilitar: "))
                materia_encontrada = objeto_academia2.ver_materia_especifica(id_a_borrar)
                if(materia_encontrada and materia_encontrada[2] == 'Habilitada'):
                    confirmar = input(f"Deshabilitar {materia_encontrada[1]} ? s/n: ").lower().strip()
                    if(confirmar != "s"):
                        print("Cancelado.")
                    else:
                        objeto_academia2.deshabilitar_materia(id_a_borrar)
                        print(f"Se deshabilitó la materia {materia_encontrada[1]}")
                else:
                    print("Error. No hay materia con ese id o ya esta inhabilitada.")
            except ValueError:
                print("Error. Debe ingresar un numero entero.")
            continuar = input("Seguir buscando y deshabilitando materias? s/n: ").lower().strip()

def modificar_materias():
    print("Modificar materias")
    continuar = "s"
    while (continuar == "s"):
        registros = objeto_academia2.ver_materias()
        if(not registros):
            print("No hay datos en la base de datos. Use la opcion 1 para insertar datos.")
            input("ENTER para continuar.")
            break
        else:
            ver_materias()
            try:
                id_a_modificar = int(input("Ingrese el id de la materia a modificar: "))    
                materia_encontrada = objeto_academia2.ver_materia_especifica(id_a_modificar)
                if(materia_encontrada and materia_encontrada[2] == 'Deshabilitada'):
                    print("Error. Esa materia está deshabilitada.")
                if(not materia_encontrada):
                    print("Error. No hay materia con ese id")
                if(materia_encontrada and materia_encontrada[2] == 'Habilitada'):
                    print(f"La materia con ese id es: {materia_encontrada}") 
                    modificar = input("Modificar materia? s/n: ").lower().strip()
                    if(modificar != "s"):
                        materia_ingresada = materia_encontrada[1]
                    else:
                        while(True):
                            materia = input("Ingrese la nueva materia:  ").strip().title()
                            materia_ingresada = objeto_academia2.validar_materia(materia)
                            if(materia_ingresada):
                                break
                            

                    objeto_academia2.modificar_materia(id_a_modificar,materia)
            except ValueError:
                print("Error. Debe ingresar un numero entero.")
                
            continuar = input("Seguir buscando y modificando? s/n: ").lower().strip()

def ver_materias():
    registros = objeto_academia2.ver_materias()
    if(not registros):
        print("No hay materias cargadas. Use el menú de materias para cargarlas al sistema.")
    else:
        print("Lista de materias")
        print("ID de la materia || Nombre de la materia || Estado de la materia")
        print("-" * 40) 
        for registro in registros:
            print(f"  {registro[0]}  ||  {registro[1]} || {registro[2]}")
            print("-" * 40) 


main()
