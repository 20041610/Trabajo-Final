from clase_academia import Academia
objeto_academia2 = Academia()


menu = '''
                                                    *****************************************
                                                    *             Menu Materias             *
                                                    *****************************************
                                                    *                                       *
                                                    * 1) Insertar Materias                  *
                                                    * 2) Eliminar Materias                  *
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
            print("Insertar materias")
            continuar = "s"
            while(continuar == "s"):
                materia = input("Inserte el nombre de la materia: ").strip().title()
                materia_ingresada = objeto_academia2.validar_materia(materia)
                if(materia_ingresada):
                    print(f"Materia {materia} fue ingresada correctamente. ")
                    objeto_academia2.insertar_materias(materia_ingresada)
                    input("ENTER para continuar")
                    break

                continuar = input("¿Desea continuar insertando una materia? (s/n): ").strip().lower()
                    
        if (opcion == 2):
            continuar = "s"
            while(continuar == "s"):
                registros = objeto_academia2.ver_materias()
                if(not registros):
                    print("No hay datos en la base de datos. Use la opcion 1 para insertar datos.")
                    input("ENTER para continuar")
                    break
                else:
                    print("Mterias disponibles")
                    print("-" * 40)
                    for registro in registros:
                        print(f"Id de la materia: {registro[0]} || Nombre de la materia: {registro[1]}")
                    try:
                        id_a_borrar = int(input("Ingrese el id de la materia a eliminar: "))
                        materia_encontrada = objeto_academia2.ver_materia_especifica(id_a_borrar)
                        if(materia_encontrada):
                            confirmar = input("Confirmar borrado ? s/n: ").lower().strip()
                            if(confirmar != "s"):
                                print("Cancelado.")
                            else:
                                objeto_academia2.borrar_materia(id_a_borrar)
                                print(f"Se eliminó la materia {materia_encontrada[1]}")
                        else:
                            print("Error. No hay materia con ese id.")
                    except ValueError:
                        print("Error. Debe ingresar un numero entero.")
                    continuar = input("Seguir buscando y eliminando? s/n: ").lower().strip()
        
        if(opcion == 3):
            print("Modificar materias")
            continuar = "s"
            while (continuar == "s"):
                registros = objeto_academia2.ver_materias()
                if(not registros):
                    print("No hay datos en la base de datos. Use la opcion 1 para insertar datos.")
                    input("ENTER para continuar.")
                    break
                else:
                    print("Materias disponibles")
                    print("ID de la materia || Nombre de la materia")
                    print("-" * 40)
                    for registro in registros:
                        print(f"{registro[0]} || {registro[1]}")
                        print("-" * 40)
                    try:
                        id_a_modificar = int(input("Ingrese el id de la materia a modificar: "))    
                        materia_encontrada = objeto_academia2.ver_materia_especifica(id_a_modificar)
                        if( not materia_encontrada):
                            print("Error. No hay materia con ese id")
                        else:
                            print(f"La materia con ese id es: {materia_encontrada}") 
                            modificar = input("Modificar materia? s/n: ").lower().strip()
                            if(modificar != "s"):
                                materia_ingresada = materia_encontrada[1]
                            else:
                                while(True):
                                    materia = input("Ingrese la nueva materia:  ")
                                    materia_ingresada = objeto_academia2.validar_materia(materia)
                                    if(materia_ingresada):
                                        break
                                    

                            objeto_academia2.modificar_materia(id_a_modificar,materia_ingresada)
                    except ValueError:
                        print("Error. Debe ingresar un numero entero.")
                        
                    continuar = input("Seguir buscando y modificando? s/n: ").lower().strip()

        if(opcion ==4):
            registros = objeto_academia2.ver_materias()
            if(not registros):
                print("No hay materias cargadas. Use el menú de materias para cargarlas al sistema.")
                input("ENTER para continuar")
            else:
                print("Lista de materias")
                print("ID de la materia || Nombre de la materia")
                print("-" * 40) 
                for registro in registros:
                    print(f"  {registro[0]}  ||  {registro[1]}")
                    print("-" * 40) 
            input("ENTER para continuar")


main()
