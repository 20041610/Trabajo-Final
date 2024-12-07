import sqlite3
from datetime import datetime
import re

class BaseDeDatos:
    def __init__(self, nombre_bd='ProyectoFinal.db'):
        self.nombre_bd = nombre_bd
        self.conexion = None

    def abrir_conexion(self):
        try:
            self.conexion = sqlite3.connect(self.nombre_bd)
            cursor = self.conexion.cursor()

            # Habilitar claves foráneas
            cursor.execute("PRAGMA foreign_keys = ON")

            # Crear tablas
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tabla_estudiantes (
                    id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_estudiante VARCHAR(50) NOT NULL,
                    apellido_estudiante VARCHAR(50) NOT NULL,
                    fecha_nacimiento DATE NOT NULL,
                    dni_estudiante VARCHAR(8) NOT NULL,
                    telefono_estudiante VARCHAR(20) NOT NULL,
                    domicilio_estudiante VARCHAR(50) NOT NULL,
                    numero_domicilio VARCHAR(5),
                    estado_actual_estudiante VARCHAR(15) DEFAULT "Activo/a"
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tabla_materias (
                    id_materia INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_materia VARCHAR(50) NOT NULL,
                    estado_materia VARCHAR(15) DEFAULT 'Habilitada'
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS estudiantes_materias (
                    id_relacion INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_estudiante INTEGER NOT NULL,
                    id_materia INTEGER NOT NULL,
                    estado_estudiante_en_materia VARCHAR(50) DEFAULT "Activo/a",
                    FOREIGN KEY (id_estudiante) REFERENCES tabla_estudiantes (id_estudiante)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (id_materia) REFERENCES tabla_materias (id_materia)
                    ON DELETE CASCADE ON UPDATE CASCADE,
                    UNIQUE (id_estudiante, id_materia)
                )
            ''')
            return self.conexion
        except sqlite3.Error as e:
            print(f"Error al abrir la conexión: {e}")

    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
            self.conexion = None

class Estudiantes:
    def __init__(self, base_de_datos):
        self.base_de_datos = base_de_datos #Con este atributo recibo la clase BaseDeDatos y sus atributos y metodos

    def validar_string(self, string):
        if (not string):
            print("Error. No puede estar vacio.")
            return False
        elif (not re.match(r"^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]+$", string)):
            print("Error. Ha ingresado caracteres invalidos")                        
            return False
        elif ("  " in string):
            print("Error. No pueden haber espacios consecutivos.")
            return False
        elif (len(string) < 2 or len(string) > 50):
            print("Error. La longitud debe estar entre 2 y 50.")
            return False
        else:
            return string.strip().title()

    def validar_fecha(self, fecha_nacimiento):
        try:
            fecha_actual = datetime.now()
            fecha_ingresada = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
            if (fecha_ingresada > fecha_actual):
                print("La fecha no puede ser en el futuro.")
                return False 
            edad = fecha_actual.year - fecha_ingresada.year - ((fecha_actual.month, fecha_actual.day) < (fecha_ingresada.month, fecha_ingresada.day))            
            if (edad < 18 or edad > 100):
                print(f"La edad ({edad} años) no es válida.")
                return False
            
            return fecha_ingresada.strftime("%Y-%m-%d")
        except ValueError:
            print("Error. Debe ingresar una fecha válida en formato AAAA-MM-DD.")
            return False

    def validar_dni_estudiante(self , dni_estudiante):
        if (not dni_estudiante):
            print("Error. El dni no puede estar vacio.")
            return False
        if(not dni_estudiante.isdigit()):
            print("Error. El dni solo debe contener numeros.")
            return False
        if (len(dni_estudiante) != 8):
            print("Error. El dni debe tener 8 digitos.")
            return False
        
        return dni_estudiante.strip()

    def validar_telefono(self, telefono_estudiante):
        if(not telefono_estudiante):
            print("Error. El telefono no puede estar vacio.")
            return False
        if(not telefono_estudiante.isdigit()):
            print("Error. El telefono solo debe contener numeros.")
            return False
        if(len(telefono_estudiante) != 10):
            print("Error.El numero de telefono debe tener 10 digitos.")
            return False
        else:
            return telefono_estudiante.strip()
    
    def validar_domicilio(self,domicilio):
        if (not domicilio):
            print("Error. No puede estar vacio.")
            return False
        if (not re.match(r"^[-.a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]+$", domicilio)):
            print("Error. Ha ingresado caracteres invalidos")                        
            return False
        if ("  " in domicilio):
            print("Error. No pueden haber espacios consecutivos.")
            return False
        if (len(domicilio) < 2 or len(domicilio) > 50):
            print("Error. La longitud debe estar entre 2 y 50.")
            return False
        
        return domicilio.strip().title()
    
    def validar_numero_domicilio(self,numero_domicilio):
        if(not numero_domicilio.isdigit()):
            print("Error. Debe ingresar solo numeros enteros sin puntos ni espacios.")
            return False

        if(len(numero_domicilio) > 5):
            print("Error. No pueden haber mas de 5 digitos.")
            return False
        return numero_domicilio.strip()

    def insertar_estudiantes(self, nombre_estudiante, apellido_estudiante, fecha_nacimiento, dni_estudiante, telefono_estudiante, domicilio_estudiante, numero_domicilio):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
                        INSERT INTO tabla_estudiantes(nombre_estudiante,apellido_estudiante,fecha_nacimiento, dni_estudiante, telefono_estudiante, domicilio_estudiante,numero_domicilio) 
                        VALUES(?,?,?,?,?,?,?)''',(nombre_estudiante,apellido_estudiante,fecha_nacimiento,dni_estudiante,telefono_estudiante,domicilio_estudiante,numero_domicilio))
        conexion.commit()
        self.base_de_datos.cerrar_conexion()

    def lectura_datos_estudiante(self):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_estudiantes WHERE estado_actual_estudiante = 'Activo/a'")
        datos = cursor.fetchall()
        self.base_de_datos.cerrar_conexion()
        return datos

    def lectura_estudiantes_de_baja(self):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_estudiantes WHERE estado_actual_estudiante = 'Inactivo/a'")
        datos = cursor.fetchall()
        self.base_de_datos.cerrar_conexion()
        return datos
    
    def lectura_estudiante_especifico(self, id_estudiante):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_estudiantes WHERE id_estudiante = (?) AND estado_actual_estudiante = 'Activo/a'", (id_estudiante,))
        if(cursor.rowcount ==0):
            self.base_de_datos.cerrar_conexion()
            return False
        else:
            datos = cursor.fetchone()
            self.base_de_datos.cerrar_conexion()
            return datos

    def dar_baja_estudiantes(self, id_a_borrar):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE tabla_estudiantes SET estado_actual_estudiante = 'Inactivo/a' WHERE id_estudiante = (?)",(id_a_borrar,))
        cursor.execute("UPDATE estudiantes_materias SET estado_estudiante_en_materia = 'Dado/a de baja de la carrera' WHERE id_estudiante = (?)",(id_a_borrar,))
        conexion.commit()
        self.base_de_datos.cerrar_conexion()
    
    def modificar_estudiante(self, id_a_modificar, nuevo_nombre, nuevo_apellido, nueva_fecha, nuevo_dni_estudiante, nuevo_telefono, nuevo_domicilio,numero_domicilio):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
                    UPDATE tabla_estudiantes 
                    SET nombre_estudiante = (?), apellido_estudiante = (?), fecha_nacimiento = (?), dni_estudiante = (?), telefono_estudiante = (?), domicilio_estudiante = (?), numero_domicilio = (?) 
                    WHERE id_estudiante = (?)''', (nuevo_nombre,nuevo_apellido,nueva_fecha,nuevo_dni_estudiante,nuevo_telefono,nuevo_domicilio,numero_domicilio,id_a_modificar))
        conexion.commit()
        self.base_de_datos.cerrar_conexion()
    
    def ordenamiento_por_apellido(self):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_estudiantes")
        datos = cursor.fetchall()
        for i in range(len(datos)):
            for j in range(0, len(datos) - i - 1):
                if datos[j][2]  > datos[j + 1][2]:
                    datos[j], datos[j + 1] = datos[j + 1], datos[j]
                if datos[j][2]  == datos[j + 1][2]:
                    if datos[j][1]  > datos[j + 1][1]:
                        datos[j], datos[j + 1] = datos[j + 1], datos[j]
        self.base_de_datos.cerrar_conexion()
        return datos

    def ordenamiento_por_edad(self):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_estudiantes")
        datos = cursor.fetchall()
        for i in range(len(datos)):
            for j in range(0,len(datos) - i - 1):
                if(datos[j][3] > datos [j + 1][3]):
                    datos[j], datos[j + 1] = datos[j + 1], datos[j]
        self.base_de_datos.cerrar_conexion()
        return datos


class Materias:
    def __init__(self, base_de_datos):
        self.base_de_datos = base_de_datos

    def validar_materia(self, materia):
        if(not materia):
            print("Error: El nombre no puede estar vacio")
            return False
        if(not re.fullmatch(r"([a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]+)(?: (\d+))?", materia)):
            print("Error: El nombre contiene caracteres invalidos")
            return False
        if("  " in materia):
            print("Error. No pueden haber espacios consecutivos")
            return False
        if(len(materia)< 2 or len(materia) > 50 ):
            print("Error: El nombre tiene una longitud incorrecta.")
            return False
        else:
            return True
    
    def insertar_materias(self, nombre_materia):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tabla_materias(nombre_materia)VALUES(?)",(nombre_materia,))
        conexion.commit()
        self.base_de_datos.cerrar_conexion()

    def ver_materias(self):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_materias")
        datos = cursor.fetchall()
        self.base_de_datos.cerrar_conexion()
        return datos
    
    def ver_materia_especifica(self, id_materia):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_materias WHERE id_materia = (?) AND estado_materia = 'Habilitada'",(id_materia,))
        if(cursor.rowcount ==0):
            self.base_de_datos.cerrar_conexion()
            return False
        else:
            datos = cursor.fetchone()
            self.base_de_datos.cerrar_conexion()
            return datos

    def deshabilitar_materia(self, id_materia):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE tabla_materias SET estado_materia = 'Deshabilitada' WHERE id_materia = (?)",(id_materia,))
        cursor.execute("""
            UPDATE estudiantes_materias
            SET estado_estudiante_en_materia = 'Dado/a de baja de la materia'
            WHERE id_materia = (?) AND NOT estado_estudiante_en_materia = 'Dado/a de baja de la carrera'""", (id_materia,))        
        conexion.commit()
        self.base_de_datos.cerrar_conexion()

    def modificar_materia(self, id_a_modificar, nueva_materia):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
                    UPDATE tabla_materias 
                    SET nombre_materia = (?)  
                    WHERE id_materia = (?)''', (nueva_materia,id_a_modificar))
        conexion.commit()
        self.base_de_datos.cerrar_conexion()

    def insertar_estudiantes_en_materias(self,id_estudiante, id_materia):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO estudiantes_materias(id_estudiante,id_materia) VALUES (?,?)",(id_estudiante,id_materia))
        conexion.commit()
        self.base_de_datos.cerrar_conexion()

    def ver_materias_con_estudiantes(self):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
        SELECT 
            em.id_relacion, 
            e.nombre_estudiante,
            e.apellido_estudiante, 
            e.dni_estudiante,
            e.estado_actual_estudiante,
            m.nombre_materia,
            em.estado_estudiante_en_materia,
            m.estado_materia
        FROM estudiantes_materias em
        INNER JOIN tabla_estudiantes e ON em.id_estudiante = e.id_estudiante
        INNER JOIN tabla_materias m ON em.id_materia = m.id_materia
        
    ''')        
        datos = cursor.fetchall()
        self.base_de_datos.cerrar_conexion()
        return datos
    
    def ver_materia_y_estudiante_especifico(self, id_relacion = None, id_estudiante = None, id_materia = None):
        if (id_relacion is not None):
            conexion = self.base_de_datos.abrir_conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM estudiantes_materias WHERE id_relacion = (?) AND estado_estudiante_en_materia = 'Activo/a'",(id_relacion,))
            if(cursor.rowcount == 0):
                self.base_de_datos.cerrar_conexion()
                return False
            else:
                datos = cursor.fetchone()
                self.base_de_datos.cerrar_conexion()
                return datos
        if ((id_estudiante is not None) and (id_materia is not None)):
            conexion = self.base_de_datos.abrir_conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM estudiantes_materias WHERE id_estudiante = (?) AND id_materia = (?)",(id_estudiante, id_materia))
            datos = cursor.fetchone()
            self.base_de_datos.cerrar_conexion()
            return datos

    def dar_baja_estudiante_en_materia(self, id_relacionado):
        conexion = self.base_de_datos.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
                    UPDATE estudiantes_materias 
                    SET estado_estudiante_en_materia = 'Dado/a de baja de la materia' 
                    WHERE id_relacion = (?)''',(id_relacionado,))
        if(cursor.rowcount == 0):
            self.base_de_datos.cerrar_conexion()
            return False
        
        else:
            conexion.commit()
            self.base_de_datos.cerrar_conexion()
            return True
        

    




