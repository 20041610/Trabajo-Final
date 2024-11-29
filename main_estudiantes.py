from clase_academia import Academia
from datetime import datetime
objeto_academia = Academia()

menu = '''
                                                    *****************************************
                                                    *             Menu Carrera              *
                                                    *****************************************
                                                    *                                       *
                                                    * 1) Insertar Estudiantes               *
                                                    * 2) Eliminar Estudiantes               *
                                                    * 3) Modificar Estudiantes              *
                                                    * 4) Ver los datos de cada estudiante   *
                                                    * 5) Ver lista de materias              *
                                                    * 6) Ver materias y sus estudiantes     *
                                                    * 7) Insertar estudiantes en materias   *
                                                    * 8) Ver estudiantes ordenados por...   *
                                                    * 9) Salir                              *
                                                    *****************************************

'''

def main():
    opcion = 0
    while(not opcion == 9):
        print(menu)
        while True:
            try:
                opcion= int(input("Ingrese una opcion del menu:"))
                break
            except ValueError:
                print("Ingrese una opcion del 1 al 9")

        if(opcion==1):
            print("Insertar Estudiantes")
            while(True):
                nombre = input("Ingrese el/los nombres: ")
                nombre_ingresado = objeto_academia.validar_nombre(nombre)
                if(nombre_ingresado):
                    print(f"El nombre {nombre} fue ingresado.")
                    break
            while(True):
                apellido = input("Ingrese el/los apellido/s de el/la estudiante: ")
                apellido_ingresado = objeto_academia.validar_apellido(apellido)
                if(apellido_ingresado):
                    print(f"El/los apellido/s {apellido} ingresado/s ")
                    break
            while(True):
                fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato DD-MM-YYYY: ")
                fecha_ingresada = objeto_academia.validar_fecha(fecha_nacimiento)
                if(fecha_ingresada):
                    print(f"La fecha {fecha_nacimiento} fue ingresada.")
                    break

            while(True):
                dni = input("Ingrese su DNI (Solo numeros): ")
                dni_ingresado = objeto_academia.validar_dni_estudiante(dni)
                if(dni_ingresado):
                    print(f"El dni {dni} fue ingresado.")
                    break

            while(True):
                telefono = input("Ingrese el  telefono de el/la estudiante: ")
                telefono_ingresado = objeto_academia.validar_telefono(telefono)
                if(telefono_ingresado):
                    print(f"El telefono {telefono} ingresado.")
                    break

            while True:
                domicilio = input("Ingrese el domicilio de el/la estudiante: ")
                domicilio_ingresado = objeto_academia.validar_domicilio(domicilio)
                if(domicilio_ingresado):
                    print(f"El domicilio {domicilio} fue ingresado.")
                    break
            objeto_academia.insertar_datos(nombre_ingresado,apellido_ingresado,fecha_ingresada,dni_ingresado,telefono_ingresado,domicilio_ingresado)

        if(opcion == 2):
            continuar = "s"
            while(continuar == "s"):
                registros = objeto_academia.lectura_datos()
                if(not registros):
                    print("No hay datos en la base de datos. Use la opcion 1 para insertar datos.")
                    input("ENTER para continuar")
                    break
                else:
                    print("Estudiantes disponibles")
                    print("-" * 40)
                    for registro in registros:
                        print(f"Id de el/la estudiante: {registro[0]} || Nombre completo: {registro[1] + ' ' + registro[2]}")
                    try:
                        id_a_borrar = int(input("Ingrese el id de el/la estudiante a eliminar: "))
                        estudiante_encontrado = objeto_academia.lectura_especifica(id_a_borrar)
                        if(estudiante_encontrado):
                            confirmar = input("Confirmar borrado ? s/n: ").lower().strip()
                            if(confirmar != "s"):
                                print("Cancelado.")
                            else:
                                objeto_academia.borrar_datos(id_a_borrar)
                                print(f"Se eliminó a {estudiante_encontrado[1] + ' ' + estudiante_encontrado[2]}")
                        else:
                            print("Error. No hay estudiante con ese id.")
                    except ValueError:
                        print("Error. Debe ingresar un numero entero.")
                    continuar = input("Seguir buscando y eliminando? s/n: ").lower().strip()

        if(opcion == 3):
            print("Modificar estudiantes")
            continuar = "s"
            while (continuar == "s"):
                registros = objeto_academia.lectura_datos()
                if(not registros):
                    print("No hay datos en la base de datos. Use la opcion 1 para insertar datos.")
                    input("ENTER para continuar.")
                    break
                else:
                    print("Estudiantes disponibles")
                    print("ID del/la estudiante || Nombre/s || Apellido/s ||  Fecha de Nacimiento || DNI || Telefono || Domicilio")
                    print("-" * 100)
                    for registro in registros:
                        print(f"{registro[0]}  || {registro[1]} || {registro[2]} || {registro[3]} || {registro[4]} || {registro[5]} || {registro[6]}")
                        print("-" * 100)
                    
                    try:
                        id_a_modificar = int(input("Ingrese el id de el/la estudiante a modificar: "))    

                        estudiante_encontrado = objeto_academia.lectura_especifica(id_a_modificar)
                        if( not estudiante_encontrado):
                            print("Error. No hay estudiante con ese id")
                        else:
                            print(f"La persona con ese id es: {estudiante_encontrado}") 
                            modificar = input("Modificar nombre? s/n: ").lower().strip()
                            if(modificar != "s"):
                                nombre_ingresado = estudiante_encontrado[1]
                            else:
                                while(True):
                                    nombre = input("Ingrese el/los nuevo/s nombre/s: ")
                                    nombre_ingresado = objeto_academia.validar_apellido(nombre)
                                    if(nombre_ingresado):
                                        break
                                    
                            modificar = input("Modificar apellido? s/n: ")
                            if(modificar !="s"):
                                apellido_ingresado = estudiante_encontrado[2]
                            else:
                                while(True):
                                    apellido = input("Ingrese el/los nuevo/s apellido/s de el/la estudiante: ")
                                    apellido_ingresado = objeto_academia.validar_nombre(apellido)
                                    if(apellido_ingresado):
                                        break

                            modificar = input("Modificar fecha de nacimiento? s/n: ").lower().strip()
                            if(modificar != "s"):
                                fecha_ingresada = estudiante_encontrado[3]
                            else:
                                while (True):
                                    fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento en formato DD-MM-YYYY: ")
                                    fecha_ingresada = objeto_academia.validar_fecha(fecha_nacimiento)
                                    if(fecha_ingresada):
                                        break

                            modificar = input("Modificar dni? s/n: ").lower().strip()
                            if(modificar != "s"):
                                dni_ingresado = estudiante_encontrado[4]
                            else:
                                while (True):
                                    dni = input("Ingrese el nuevo DNI (Solo numeros): ")
                                    dni_ingresado = objeto_academia.validar_dni_estudiante(dni)
                                    if(dni_ingresado):
                                        break

                            modificar = input("Modificar Telefono? s/n: ").lower().strip()
                            if(modificar != "s"):
                                telefono_ingresado = estudiante_encontrado[5]
                            else:
                                while(True):
                                    telefono = input("Inserte el nuevo telefono de el/la estudiante: ")
                                    telefono_ingresado = objeto_academia.validar_telefono(telefono)
                                    if(telefono_ingresado):
                                        print(f"Telefono modificado correctamente.")
                                        break

                            modificar = input("Modificar domicilio? s/n: ").lower().strip()
                            if(modificar != "s"):
                                domicilio_ingresado = estudiante_encontrado[6]
                            else:
                                while(True):
                                    domicilio = input("Inserte el nuevo domicilio de el/la estudiante: ")
                                    domicilio_ingresado = objeto_academia.validar_domicilio(domicilio)
                                    if(domicilio_ingresado):
                                        print(f"Domicilio modificado correctamente.")
                                        break
                            objeto_academia.modificar_datos(id_a_modificar,nombre_ingresado,apellido_ingresado,fecha_ingresada,dni_ingresado,telefono_ingresado,domicilio_ingresado)
                    except ValueError:
                        print("Error. Debe ingresar un numero entero.")
                        
                    continuar = input("Seguir buscando y modificando? s/n: ").lower().strip()

        if (opcion == 4):
            registros = objeto_academia.lectura_datos()
            if(not registros):
                print("No hay datos en la base de datos. Use la opcion 1 para insertar datos.")
                input("ENTER para continuar")
            else:
                print("Tabla de estudiantes")
                print(f"ID de el/la estudiante || Nombre/s || Apellido/s || Fecha de Nacimiento || DNI || Telefono || Domicilio")
                print("-" * 100)
                for registro in registros:
                    print(f"{registro[0]}  || {registro[1]} || {registro[2]} || {registro[3]} || {registro[4]} || {registro[5]} || {registro[6]}")
                    print("-" * 100)
                input("ENTER para continuar")
        
        if(opcion ==5):
            registros = objeto_academia.ver_materias()
            if(not registros):
                print("No hay materias cargadas. Use el menú de materias para cargarlas al sistema.")
                input("ENTER para continuar")
            else:
                print("Lista de materias")
                print("ID de la materia || Nombre de la materia")
                print("-" * 40) 
                for registro in registros:
                    print(f"     {registro[0]}  ||  {registro[1]}")
                    print("-" * 40) 
            input("ENTER para continuar")
        
        if(opcion==6):
            print("Materias y sus alumnos")
            registros = objeto_academia.ver_materias_con_estudiantes()
            if(not registros):
                print("Error. No se han cargado alumnos a materias")
                input("ENTER para continuar")
                break
            # Agrupar estudiantes por materia
            materias_dict = {}
            for registro in registros:
                materia = registro[4]  # Nombre de la materia
                estudiante_info = f"{registro[1] + ' ' + registro[2]} (DNI: {registro[3]})"  # Información del estudiante
                
                if materia not in materias_dict:
                    materias_dict[materia] = []  # Crear una nueva lista para la materia
                materias_dict[materia].append(estudiante_info)  # Agregar el estudiante
            
            # Imprimir materias y sus estudiantes
            for materia, estudiantes in materias_dict.items():
                print(f"Materia: {materia}")
                print("Estudiantes:")
                for estudiante in estudiantes:
                    print(f" - {estudiante}")
                print("-" * 40)
            
            input("ENTER para continuar")
            
        if(opcion ==7):
            print("Insertar estudiante en materia")
            continuar = "s"
            while(continuar == "s"):
                registros = objeto_academia.lectura_datos()
                materias = objeto_academia.ver_materias()
                if(not registros or not materias):
                    print("No hay datos en la base de datos. Use la opcion 1 para insertar datos.")
                    input("ENTER para continuar")
                    break
                else:
                    print("Estudiantes disponibles")
                    for registro in registros:
                        print(f"ID de el/la estudiante: {registro[0]}||Estudiante: {registro[1] + ' ' + registro[2]}")
                    
                    try:
                        id_estudiante = int(input("Ingrese el id de el/la estudiante: "))
                        estudiante_encontrado = objeto_academia.lectura_especifica(id_estudiante)
                        if(not estudiante_encontrado):
                            print("No hay estudiante con ese id")
                            input("ENTER para continuar")
                        else:
                            for materia in materias:
                                print(f"ID de la materia: {materia[0]} || Nombre de la materia: {materia[1]}")
                            
                            id_materia = int(input("Ingrese el id de la materia: "))
                            materia_encontrada = objeto_academia.ver_materia_especifica(id_materia)
                            if(not materia_encontrada):
                                print("No hay materia con ese id.")
                                input("ENTER para continuar")
                            if(objeto_academia.ver_materia_y_estudiante_especifico(id_estudiante,id_materia)):
                                print("Error. Ya se encuentra inscripto/a en la materia.")
                                input("ENTER para continuar.")
                            else:
                                confirmar = input("Confirmar? s/n: ").lower().strip()
                                if(confirmar != "s"):
                                    print("Cancelado.")
                                else:
                                    objeto_academia.insertar_estudiantes_en_materias(id_estudiante,id_materia)
                                    print(f"{estudiante_encontrado[1] + ' '+ estudiante_encontrado[2]} inscripto/a en {materia_encontrada[1]}")
                                    input("ENTER para continuar")
                    except ValueError:
                            print("Error. Inserte un numero entero como id.")

                        

                continuar = input("Seguir insertando alumnos a materias? s/n: ").lower().strip()
    
        if(opcion == 8):
            menu2 = '''
                                                    ******************************************
                                                    *          Menu de Ordenamiento          *
                                                    ******************************************
                                                    *                                        *
                                                    * 1) Ordenamiento por apellido (Alfabeticamente)*
                                                    * 2) Ordenamiento por edad (Descendente) *
                                                    * 3) Ordenamiento por edad (Ascendente)  *
                                                    * 4) Salir                               *
                                                    ******************************************
                                                    
                    '''
            opcion = 0
            while(not opcion == 4):
                print(menu2)
                while True:
                    try:
                        opcion= int(input("Ingrese una opcion del menu:"))
                        break
                    except ValueError:
                        print("Ingrese numeros")
                if(opcion == 1):
                    print("Ordenamiento por apellido")
                    registros = objeto_academia.ordenamiento_por_apellido()
                    for registro in registros:
                        print(f"Nombre completo: {registro[1] + ' ' + registro[0]}")
                    input("ENTER para continuar")

                if(opcion ==2):
                    print("Ordenamiento por edad (Descendente)")
                    registros = objeto_academia.ordenamiento_por_edad()
                    for registro in registros:
                        print(f"Nombre completo: {registro[0] + ' ' + registro[1]} || Edad: { ((datetime.now() - datetime.strptime(registro[2], '%Y-%m-%d')).days // 365)}")
                    input("ENTER para continuar")

                if(opcion == 3):
                    print("Ordenamiento por edad (Ascendente)")
                    registros = objeto_academia.ordenamiento_por_edad()
                    for registro in reversed(registros):
                        print(f"Nombre completo: {registro[0] + ' ' + registro[1]} || Edad: { ((datetime.now() - datetime.strptime(registro[2], '%Y-%m-%d')).days // 365)}")
                    input("ENTER para continuar")

        if(opcion == 9):
            print("Saliendo del programa.")

            
            

main()