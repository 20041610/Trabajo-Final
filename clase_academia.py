import sqlite3
from datetime import datetime
import re

class Academia:
    def abrir_conexion(self):   
        try:
            variable_de_conexion = sqlite3.connect('test.db')
            cursor = variable_de_conexion.cursor()

            # Habilitar claves foráneas
            cursor.execute("PRAGMA foreign_keys = ON")

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tabla_estudiantes (
                    id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_estudiante VARCHAR(50) NOT NULL,
                    apellido_estudiante VARCHAR(50) NOT NULL,
                    fecha_nacimiento DATE NOT NULL,
                    dni_estudiante VARCHAR(8) NOT NULL,
                    telefono_estudiante VARCHAR(20) NOT NULL,
                    domicilio_estudiante VARCHAR(50) NOT NULL
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tabla_materias (
                    id_materia INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_materia VARCHAR(50) NOT NULL)
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS estudiantes_materias (
                    id_relacion INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_estudiante INTEGER NOT NULL,
                    id_materia INTEGER NOT NULL,
                    FOREIGN KEY (id_estudiante) REFERENCES tabla_estudiantes (id_estudiante) 
                    ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (id_materia) REFERENCES tabla_materias (id_materia) 
                    ON DELETE CASCADE ON UPDATE CASCADE,
                    UNIQUE (id_estudiante, id_materia)
                )
            ''')

            return variable_de_conexion

        except sqlite3.Error as e:
            print(f"Error al abrir la conexión: {e}")
            return None

    def validar_nombre(self, nombre_estudiante):
        if (not nombre_estudiante):
            print("Error. El nombre no puede estar vacio.")
            return False
        elif (not re.match(r"^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]+$", nombre_estudiante)):
            print("Error.El nombre contiene caracteres invalidos")                        
            return False
        elif ("  " in nombre_estudiante):
            print("Error. No pueden haber espacios consecutivos.")
            return False
        elif (len(nombre_estudiante) < 2 or len(nombre_estudiante) > 50):
            print("Error. El nombre tiene una longitud incorrecta.")
            return False
        else:
            return nombre_estudiante.strip().title()

    def validar_apellido(self, apellido_estudiante):
        if (not apellido_estudiante):
            print("Error. El apellido no puede estar vacio.")
            return False
        elif (not re.match(r"^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]+$", apellido_estudiante)):
            print("Error.El apellido contiene caracteres invalidos")                        
            return False
        elif ("  " in apellido_estudiante):
            print("Error. No pueden haber espacios consecutivos.")
            return False
        elif (len(apellido_estudiante) < 2 or len(apellido_estudiante) > 50):
            print("Error. El apellido tiene una longitud incorrecta.")
            return False
        else:
            return apellido_estudiante.strip().title()        
    
    def validar_fecha(self, fecha_nacimiento):
        try:
            fecha = datetime.strptime(fecha_nacimiento, '%d-%m-%Y')
            if (fecha > datetime.now()):
                print("La fecha no puede ser en el futuro.")
                return False 
            edad = ((datetime.now() - fecha).days // 365)
            if (edad < 18 or edad > 100):
                print(f"La edad ({edad} años) no es válida.")
                return False
            else:
                return fecha.strftime("%Y-%m-%d")
        except ValueError:
            print("Error. Debe ingresar una fecha válida en formato DD-MM-YYYY.")
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
        else:
            return dni_estudiante

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
            return telefono_estudiante
    
    def validar_domicilio(self, domicilio_estudiante):
        if(not domicilio_estudiante):
            print("Error. El domicilio no puede estar vacio.")
            return False
        if (not re.match(r"^[-.a-zA-ZáéíóúüñÁÉÍÓÚÜÑ0-9\s]+$", domicilio_estudiante)):
            print("Error. El domicilio contiene caracteres invalidos.")                        
            return False
        if("  " in domicilio_estudiante):
            print("Error. El domicilio no puede tener espacios consecutivos.")
            return False
        if(len(domicilio_estudiante) < 2 or len(domicilio_estudiante) > 50):
            print("Error. El domicilio tiene una longitud no permitida.")
            return False
        else:
            return domicilio_estudiante.strip().title()

    def validar_materia(self, materia):
        if(not materia):
            print("Error: El nombre no puede estar vacio")
            return False
        if(not re.match(r"^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]+$", materia)):
            print("Error: El nombre contiene caracteres invalidos")
            return False
        if("  " in materia):
            print("Error. No pueden haber espacios consecutivos")
            return False
        if(len(materia)< 2 or len(materia) > 50 ):
            print("Error: El nombre tiene una longitud incorrecta.")
            return False
        else:
            return materia.title().strip()

    def insertar_datos(self, nombre_estudiante, apellido_estudiante, fecha_nacimiento, dni_estudiante, telefono_estudiante, domicilio_estudiante):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
                        INSERT INTO tabla_estudiantes(nombre_estudiante,apellido_estudiante,fecha_nacimiento, dni_estudiante, telefono_estudiante, domicilio_estudiante) 
                        VALUES(?,?,?,?,?,?)''',(nombre_estudiante,apellido_estudiante,fecha_nacimiento,dni_estudiante,telefono_estudiante,domicilio_estudiante))
        conexion.commit()
        conexion.close()

    def lectura_datos(self):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_estudiantes")
        datos = cursor.fetchall()
        conexion.close()
        return datos

    def lectura_especifica(self, id):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_estudiantes WHERE id_estudiante = (?)", (id,))
        datos = cursor.fetchone()
        conexion.close()
        return datos

    def borrar_datos(self, id_a_borrar):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM tabla_estudiantes WHERE id_estudiante = (?)",(id_a_borrar,))
        conexion.commit()
        conexion.close()
    
    def modificar_datos(self, id_a_modificar, nuevo_nombre, nuevo_apellido, nueva_fecha, nuevo_dni_estudiante, nuevo_telefono, nuevo_domicilio):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
                    UPDATE tabla_estudiantes 
                    SET nombre_estudiante = (?), apellido_estudiante = (?), fecha_nacimiento = (?), dni_estudiante = (?), telefono_estudiante = (?), domicilio_estudiante = (?) 
                    WHERE id_estudiante = (?)''', (nuevo_nombre,nuevo_apellido,nueva_fecha,nuevo_dni_estudiante,nuevo_telefono,nuevo_domicilio,id_a_modificar))
        conexion.commit()
        conexion.close()
    
    def insertar_materias(self, nombre_materia):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tabla_materias(nombre_materia)VALUES(?)",(nombre_materia,))
        conexion.commit()
        conexion.close()

    def ver_materias(self):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_materias")
        datos = cursor.fetchall()
        conexion.close()
        return datos
    
    def ver_materia_especifica(self, id_materia):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_materias WHERE id_materia = (?)",(id_materia,))
        datos = cursor.fetchone()
        conexion.close()
        return datos

    def borrar_materia(self, id_a_borrar):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM tabla_materias WHERE id_materia = (?)",(id_a_borrar,))
        conexion.commit()
        conexion.close()

    def modificar_materia(self, id_a_modificar, nueva_materia):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
                    UPDATE tabla_materias 
                    SET nombre_materia = (?)  
                    WHERE id_materia = (?)''', (nueva_materia,id_a_modificar))
        conexion.commit()
        conexion.close()

    def insertar_estudiantes_en_materias(self,id_estudiante, id_materia):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO estudiantes_materias(id_estudiante,id_materia) VALUES (?,?)",(id_estudiante,id_materia))
        conexion.commit()
        conexion.close()

    def ver_materias_con_estudiantes(self):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
        SELECT 
            em.id_relacion, 
            e.nombre_estudiante,
            e.apellido_estudiante, 
            e.dni_estudiante, 
            m.nombre_materia 
        FROM estudiantes_materias em
        INNER JOIN tabla_estudiantes e ON em.id_estudiante = e.id_estudiante
        INNER JOIN tabla_materias m ON em.id_materia = m.id_materia
    ''')        
        datos = cursor.fetchall()
        conexion.close()
        return datos
    
    def ver_materia_y_estudiante_especifico(self, id_estudiante, id_materia):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM estudiantes_materias WHERE id_estudiante = (?) AND id_materia = (?)",(id_estudiante, id_materia))
        datos = cursor.fetchone()
        conexion.close()
        return datos

    def ordenamiento_por_apellido(self):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_estudiante, apellido_estudiante FROM tabla_estudiantes")
        datos = cursor.fetchall()
        for i in range(len(datos)):
            for j in range(0, len(datos) - i - 1):
                if datos[j][1] > datos[j + 1][1]:
                    datos[j], datos[j + 1] = datos[j + 1], datos[j]
        return datos
    
    def ordenamiento_por_edad(self):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_estudiante, apellido_estudiante, fecha_nacimiento FROM tabla_estudiantes")
        datos = cursor.fetchall()
        for i in range(len(datos)):
            for j in range(0,len(datos) - i - 1):
                if(datos[j][2] > datos [j + 1][2]):
                    datos[j], datos[j + 1] = datos[j + 1], datos[j]
        return datos



