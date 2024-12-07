from datetime import datetime
from  academia import BaseDeDatos
from academia import Estudiantes
from academia import Materias
base_de_datos = BaseDeDatos() #Instancia de la clase BaseDeDatos
Estudiantes = Estudiantes(base_de_datos) #Instancia de la clase Estudiantes
Materias = Materias(base_de_datos) #Instancia de la clase Materias
menu = '''
                                                    *********************************************
                                                    *              Menu de inscripción          *
                                                    *********************************************
                                                    *                                           *
                                                    * 1) Insertar Estudiantes                   *
                                                    * 2) Dar de baja de la carrera a Estudiantes*
                                                    * 3) Modificar Estudiantes                  *
                                                    * 4) Ver los datos de cada estudiante       *
                                                    * 5) Insertar estudiantes en materias       *
                                                    * 6) Ver materias y sus estudiantes         *
                                                    * 7) Dar de baja estudiantes en materias   *
                                                    * 8) Ver estudiantes ordenados por...       *
                                                    * 9) Estudiantes dados de baja              *
                                                    * 10) Salir                                 *
                                                    *********************************************

'''

def main():
    opcion = 0
    while(not opcion == 10):
        print(menu)
        while True:
            try:
                opcion= int(input("Ingrese una opcion del menu:"))
                break
            except ValueError:
                print("Ingrese una opcion del 1 al 10")

        if(opcion==1):
            insertar_estudiantes()
        if(opcion == 2):
            dar_baja_estudiantes()
        if(opcion == 3):
            modificar_estudiantes()
        if  (opcion == 4):
            ver_estudiantes()
            input("ENTER para continuar")
        if(opcion==5):
            insertar_estudiantes_en_materias()
        if(opcion ==6):
            ver_materias_con_estudiantes()
            input("ENTER para continuar")        
        if(opcion == 7):
            dar_baja_estudiante_en_materia()
        if(opcion == 8):
            menu_ordenamiento()
        if(opcion == 9):
            lectura_estudiantes_de_baja()
            input("ENTER para continuar")
        if(opcion == 10):
            print("Saliendo del programa.")

def insertar_estudiantes():
    # Función general para captura de datos
    def insertar_datos(mensaje, metodo_validacion):
        while (True):
            dato = input(mensaje).strip().lower()
            dato_validado = metodo_validacion(dato)
            if(dato_validado):
                return dato_validado
                

    nombre = insertar_datos("Ingrese el/los nombres de el/la estudiante: ", Estudiantes.validar_string)
    apellido = insertar_datos("Ingrese el/los apellido/s de el/la estudiante: ", Estudiantes.validar_string)
    fecha_nacimiento = insertar_datos("Ingrese su fecha de nacimiento en formato AAAA-MM-DD: ", Estudiantes.validar_fecha)
    dni = insertar_datos("Ingrese su DNI (Solo numeros): ", Estudiantes.validar_dni_estudiante)
    telefono = insertar_datos("Ingrese el telefono de el/la estudiante: ", Estudiantes.validar_telefono)
    domicilio = insertar_datos("Ingrese el nombre del domicilio de el/la estudiante: ", Estudiantes.validar_domicilio).strip()
    numero_domicilio = "S/N"
    insertar = input("Ingresar numero de domicilio? s/n: ").strip().lower()
    if(insertar == "s"):
        numero_domicilio = insertar_datos("Ingrese el numero del domicilio de el/la estudiante: ", Estudiantes.validar_numero_domicilio)

    print("Datos ingresados")
    print(f"Nombre/s: {nombre}")
    print(f"Apellido/s: {apellido}")
    print(f"Fecha de nacimiento: {fecha_nacimiento}")
    print(f"Dni: {dni}")
    print(f"Telefono: {telefono}")
    print(f"Domicilio: {domicilio} {numero_domicilio}")
    input("ENTER para continuar")
    Estudiantes.insertar_estudiantes(nombre,apellido,fecha_nacimiento,dni,telefono,domicilio,numero_domicilio)

def dar_baja_estudiantes():
    continuar = "s"
    while(continuar == "s"):
        registros = Estudiantes.lectura_datos_estudiante()
        if(not registros):
            print("Error.No hay estudiantes cargados en el sistema. Use la opcion 1 para insertarlos.")
            input("ENTER para continuar")
            break
        else:
            ver_estudiantes()
            try:
                id_a_borrar = int(input("Ingrese el id de el/la estudiante a dar de baja: "))
                estudiante_encontrado = Estudiantes.lectura_estudiante_especifico(id_a_borrar)
                if(not estudiante_encontrado):
                    print("Error. No hay estudiante con ese id.")

                if(estudiante_encontrado and estudiante_encontrado[8] == 'Activo/a'):
                    confirmar = input("Dar de baja ? s/n: ").lower().strip()
                    if(confirmar != "s"):
                        print("Cancelado.")
                    else:
                        Estudiantes.dar_baja_estudiantes(id_a_borrar)
                        print(f"Se dió de baja a {estudiante_encontrado[1] + ' ' + estudiante_encontrado[2]}")

                if(estudiante_encontrado and estudiante_encontrado[8] == 'Inactivo/a'):
                    print("Error. Ya esta dado/a de baja.")
                    
            except ValueError:
                print("Error. Debe ingresar un numero entero.")
            continuar = input("Seguir buscando y dando de baja? s/n: ").lower().strip()

def modificar_estudiantes():
    print("Modificar estudiantes")
    continuar = "s"
    while (continuar == "s"):
        registros = Estudiantes.lectura_datos_estudiante()
        if(not registros):
            print("Error.No hay estudiantes cargados en el sistema. Use la opcion 1 para insertarlos.")
            input("ENTER para continuar.")
            break
        else:
            ver_estudiantes()
            try:
                id_a_modificar = int(input("Ingrese el id de el/la estudiante a modificar: "))    
                estudiante_encontrado = Estudiantes.lectura_estudiante_especifico(id_a_modificar)
                if(estudiante_encontrado and estudiante_encontrado[8] == 'Inactivo/a'):
                    print("Error. Ya esta dado/a de baja de la carrera.")

                if(not estudiante_encontrado):
                    print("Error. No hay estudiante con ese id")

                if(estudiante_encontrado and estudiante_encontrado[8] == 'Activo/a'):
                    print(f"Datos de la persona con ese id es: {estudiante_encontrado}")

                    def modificar_datos(mensaje, metodo_validacion):
                        while(True):
                            dato = input(mensaje)
                            dato_validado = metodo_validacion(dato)
                            if(dato_validado):
                                return dato_validado
                            
                    modificar = input("Modificar nombre? s/n: ").lower().strip()
                    if(modificar != "s"):
                        nombre = estudiante_encontrado[1]
                    else:
                        nombre = modificar_datos("Ingrese los nuevos nombres de el/la estudiante: ", Estudiantes.validar_string)

                    modificar = input("Modificar apellidos? s/n: ").lower().strip()
                    if(modificar != "s"):
                        apellido = estudiante_encontrado[2]
                    else:
                        apellido = modificar_datos("Ingrese el/los nuevo/s apellido/s de el/la estudiante: ", Estudiantes.validar_string)

                    modificar = input("Modificar fecha de nacimiento? s/n: ").lower().strip()
                    if(modificar != "s"):
                        fecha_nacimiento = estudiante_encontrado[3]
                    else:
                        fecha_nacimiento = modificar_datos("Ingrese la nueva fecha de nacimiento de el/la estudiante: ", Estudiantes.validar_fecha)

                    modificar = input("Modificar dni? s/n: ").lower().strip()
                    if(modificar != "s"):
                        dni = estudiante_encontrado[4]
                    else:
                        dni = modificar_datos("Ingrese el nuevo dni de el/la estudiante: ", Estudiantes.validar_dni_estudiante)

                    modificar = input("Modificar telefono? s/n: ").lower().strip()
                    if(modificar != "s"):
                        telefono = estudiante_encontrado[5]
                    else:
                        telefono = modificar_datos("Ingrese el nuevo telefono de el/la estudiante: ", Estudiantes.validar_telefono)

                    modificar = input("Modificar nombre del domicilio? s/n: ").lower().strip()
                    if(modificar != "s"):
                        domicilio = estudiante_encontrado[6]
                    else:
                        domicilio = modificar_datos("Ingrese el nuevo nombre de domicilio de el/la estudiante: ", Estudiantes.validar_domicilio)

                    modificar = input("Modificar numero de domicilio? s/n: ").lower().strip()
                    if(modificar != "s"):
                        numero_domicilio = estudiante_encontrado[7]
                    else:
                        numero_domicilio = modificar_datos("Ingrese el nuevo numero de domicilio de el/la estudiante: ", Estudiantes.validar_numero_domicilio)

                    

                    print("Datos ingresados")
                    print(f"Nombre/s: {nombre}")
                    print(f"Apellido/s: {apellido}")
                    print(f"Fecha de nacimiento: {fecha_nacimiento}")
                    print(f"Dni: {dni}")
                    print(f"Telefono: {telefono}")
                    print(f"Domicilio: {domicilio + ' ' + numero_domicilio}")
                    input("ENTER para continuar")
                    Estudiantes.modificar_estudiante(id_a_modificar,nombre,apellido,fecha_nacimiento,dni,telefono,domicilio,numero_domicilio)
            except ValueError:
                print("Error. Debe ingresar un numero entero.")
                
            continuar = input("Seguir buscando y modificando? s/n: ").lower().strip()

def ver_estudiantes():
    registros = Estudiantes.lectura_datos_estudiante()
    if(not registros):
        print("Error.No hay estudiantes cargados en el sistema. Use la opcion 1 para insertarlos.")
    else:
        print("Tabla de estudiantes")
        print(f"ID de el/la estudiante || Nombre/s || Apellido/s || Fecha de Nacimiento || DNI || Telefono || Domicilio || Estado")
        print("-" * 100)
        for registro in registros:
            print(f"{registro[0]}  ||  {registro[1]}  ||  {registro[2]}  ||  {registro[3]}  ||  {registro[4]}  ||  {registro[5]}  ||  {registro[6] + ' '+ registro[7]}  ||  {registro[8]}")
            print("-" * 100)

def lectura_estudiantes_de_baja():
    registros = Estudiantes.lectura_estudiantes_de_baja()
    if(not registros):
        print("Error.No hay estudiantes cargados en el sistema. Use la opcion 1 para insertarlos.")
    else:
        print("Tabla de estudiantes")
        print(f"ID de el/la estudiante || Nombre/s || Apellido/s || Fecha de Nacimiento || DNI || Telefono || Domicilio || Estado")
        print("-" * 100)
        for registro in registros:
            print(f"{registro[0]}  ||  {registro[1]}  ||  {registro[2]}  ||  {registro[3]}  ||  {registro[4]}  ||  {registro[5]}  ||  {registro[6] + ' '+ registro[7]}  ||  {registro[8]}")
            print("-" * 100)

def ver_materias_con_estudiantes():
    print("Materias y sus alumnos\n")
    registros = Materias.ver_materias_con_estudiantes()
    if(not registros):
        print("Error.No hay estudiantes cargados en ninguna materia. Use la opcion 7 para cargarlos.")
        
    
    materias_con_estudiantes = {}
    for registro in registros:
        materia = f"{registro[5]} ({registro[7]})" 
        estudiante_info = f"{registro[0]} || {registro[1] + ' ' + registro[2]} ||  {registro[6]}"
        
        if materia not in materias_con_estudiantes:
            materias_con_estudiantes[materia] = [] 
        materias_con_estudiantes[materia].append(estudiante_info)
    
    for materia, estudiantes in materias_con_estudiantes.items():
        print(f'''
Materia: {materia}
**********************************************************************************************************************************
Id de la relacion ||  Nombre completo ||  Estado actual en la materia     
**********************************************************************************************************************************''')   
        for estudiante in estudiantes:
            print(f"- {estudiante}")

def insertar_estudiantes_en_materias():
    print("Insertar estudiante en materia")
    continuar = "s"
    while(continuar == "s"):
        estudiantes = Estudiantes.lectura_datos_estudiante()
        materias = Materias.ver_materias()
        if(not estudiantes or not materias):
            print("Error.No hay estudiantes cargados en ninguna materia. Use la opcion 6 para insertarlos.")
            input("ENTER para continuar")
            break
        else:
            print("\nEstudiantes disponibles")
            for estudiante in estudiantes:
                print(f"ID de el/la estudiante: {estudiante[0]}||Estudiante: {estudiante[1] + ' ' + estudiante[2]}")
            
            try:
                id_estudiante = int(input("Ingrese el id de el/la estudiante: "))
                estudiante_encontrado = Estudiantes.lectura_estudiante_especifico(id_estudiante)
                if(not estudiante_encontrado or estudiante_encontrado[8] == 'Inactivo/a'):
                    print("No hay estudiante con ese id o esta inactivo")
                else:
                    print("\nMaterias disponibles")
                    for materia in materias:
                        print(f"ID de la materia: {materia[0]} || Nombre de la materia: {materia[1]} || Estado actual de la materia: {materia[2]}")
                    
                    id_materia = int(input("Ingrese el id de la materia: "))
                    materia_encontrada = Materias.ver_materia_especifica(id_materia)
                    if(not materia_encontrada):
                        print("Error. No hay materia con ese id o está deshabilitada.")

                    if(Materias.ver_materia_y_estudiante_especifico(None,id_estudiante,id_materia)):
                        print("Error. Ya esta inscripto/a en esa materia.")

                    if(materia_encontrada and not Materias.ver_materia_y_estudiante_especifico(None,id_estudiante,id_materia)):
                        confirmar = input(f"Insertar a {estudiante_encontrado[1] + ' ' + estudiante_encontrado[2]} en la materia {materia_encontrada[1]}? s/n: ").lower().strip()
                        if (confirmar != "s"):
                            print("Cancelado.")
                        else:
                            Materias.insertar_estudiantes_en_materias(id_estudiante, id_materia)
                            print(f"Inserción exitosa.")

            except ValueError:
                    print("Error. Inserte un numero entero como id.")
            continuar = input("\nSeguir insertando alumnos a materias? s/n: ").lower().strip()

def dar_baja_estudiante_en_materia():
    print("Dar de baja estudiante \n")
    continuar = "s"
    while(continuar == "s"):
        registros = Materias.ver_materias_con_estudiantes()
        if(not registros):
            print("Error.No hay estudiantes cargados en ninguna materia. Use la opcion 6 para insertarlos.")
            input("ENTER para continuar.")
            break
        else:
            ver_materias_con_estudiantes()

            try:
                id_a_borrar = int(input("\nIngrese el id de la relacion a dar de baja: "))
                id_encontrado = Materias.ver_materia_y_estudiante_especifico(id_a_borrar,None,None)
                if(not id_encontrado):
                    print("Error. No hay relacion con ese id o ya ha sido dada de baja.")
                if(id_encontrado):
                    estudiante_encontrado = Estudiantes.lectura_estudiante_especifico(id_encontrado[1])
                    materia_encontrada = Materias.ver_materia_especifica(id_encontrado[2])
                    confirmar = input(f"Dar de baja a {estudiante_encontrado[1] + ' ' + estudiante_encontrado[2]} de la materia {materia_encontrada[1]}? s/n: ")
                    if(confirmar != "s"):
                        print("Cancelado")
                    else:
                        Materias.dar_baja_estudiante_en_materia(id_a_borrar)
                        print("Se ha dado de baja exitosamente")                    
            except ValueError:
                print("Error. Debe ingresar un numero entero.")
            continuar = input("Seguir buscando y dando de baja? s/n: ").lower().strip()

def menu_ordenamiento():
    menu2 = '''
                                                    *************************************************
                                                    *             Menu de Ordenamiento              *
                                                    *************************************************
                                                    *                                               *
                                                    * 1) Ordenamiento por apellido (Alfabeticamente)*
                                                    * 2) Ordenamiento por edad (Descendente)        *
                                                    * 3) Ordenamiento por edad (Ascendente)         *
                                                    * 4) Salir                                      *
                                                    *************************************************
                                                    
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
            registros = Estudiantes.lectura_datos_estudiante()
            if(not registros):
                print("Error.No hay estudiantes cargados en el sistema. Use la opcion 1 para insertarlos.")
                input("ENTER para continuar")
                break
            else:       
                print("Ordenamiento por apellido")
                print('''
**********************************************************************************************************
ID de el/la estudiante || Nombre completo || Fecha de Nacimiento || DNI || Telefono || Domicilio || Estado                 
**********************************************************************************************************''')
                estudiantes = Estudiantes.ordenamiento_por_apellido()
                for estudiante in estudiantes:
                    print(f"{estudiante[0]} ||  {estudiante[2] + ' ' + estudiante[1]}  ||  {estudiante[3]}  ||  {estudiante[4]}  ||  {estudiante[5]}  ||  {estudiante[6] + ' ' + estudiante[7]}  ||  {estudiante[8]}")
                    print("-" * 100)
                input("ENTER para continuar")

        if(opcion ==2):
            registros = Estudiantes.lectura_datos_estudiante()
            if(not registros):
                print("Error.No hay estudiantes cargados en el sistema. Use la opcion 1 para insertarlos.")
                input("ENTER para continuar")
                break
            else:       
                print("Ordenamiento por edad (Descendente)")
                print('''
**********************************************************************************************************
ID de el/la estudiante || Nombre completo || Fecha de nacimiento || Edad || DNI || Telefono || Domicilio || Estado                 
**********************************************************************************************************''')
                estudiantes = Estudiantes.ordenamiento_por_edad()
                for estudiante in estudiantes:
                    fecha_nacimiento = datetime.strptime(estudiante[3], "%Y-%m-%d")
                    print(f"{estudiante[0]} ||  {estudiante[2] + ' ' + estudiante[1]}  ||  {estudiante[3]}  ||  {datetime.now().year - fecha_nacimiento.year - ((datetime.now().month, datetime.now().day) < (fecha_nacimiento.month, fecha_nacimiento.day))}||  {estudiante[4]}  ||  {estudiante[5]}  ||  {estudiante[6] + ' ' + estudiante[7]}  ||  {estudiante[8]}")
                    print("-" * 100)
                input("ENTER para continuar")

        if(opcion == 3):
            registros = Estudiantes.lectura_datos_estudiante()
            if(not registros):
                print("Error.No hay estudiantes cargados en el sistema. Use la opcion 1 para insertarlos.")
                input("ENTER para continuar")
                break
            else:       
                print("Ordenamiento por edad (Ascendente)")
                print('''
**********************************************************************************************************
ID de el/la estudiante || Nombre completo || Fecha de nacimiento || Edad || DNI || Telefono || Domicilio || Estado                 
**********************************************************************************************************''')
                estudiantes = Estudiantes.ordenamiento_por_edad()
                for estudiante in reversed(estudiantes):
                    fecha_nacimiento = datetime.strptime(estudiante[3], "%Y-%m-%d")
                    print(f"{estudiante[0]} ||  {estudiante[2] + ' ' + estudiante[1]}  ||  {estudiante[3]}  ||  {datetime.now().year - fecha_nacimiento.year - ((datetime.now().month, datetime.now().day) < (fecha_nacimiento.month, fecha_nacimiento.day))}||  {estudiante[4]}  ||  {estudiante[5]}  ||  {estudiante[6] + ' ' + estudiante[7]}  ||  {estudiante[8]}")
                    print("-" * 100)
                input("ENTER para continuar")


main()