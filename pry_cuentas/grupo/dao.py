from conexion import Conector


class daoGrupo(Conector):
    def __init__(self, server='localhost', usuario='root', password='', basedato='crud'):
        Conector.__init__(self, server='localhost', usuario='root', password='', basedato='crud')

    def consultar(self):
        result = True
        try:
            sql = 'Select * from grupo'
            self.conectar()  # Llama al constructor y crea una conexión con la BD
            self.conector.execute(sql)  # Instanciamos  conector, y le mando una sentencia sql para ejecutar en la
            # base de datos
            result = self.conector.fetchall()  # Fetchall devuelve un diccionario de mi tabla Grupo
            self.conn.commit()  # asegura que los datos
        except Exception as ex:
            result = False
            self.conn.rollback()  # muestra el error
        finally:
            self.cerrar()  # llama al metodo cerra de Conector
        return result

    def ingresar(self, gru):
        result = True
        try:
            sql = "insert into grupo(descripcion)VALUES (%s)"  # para seguridad enviamos %s, no se sepa lo que se
            # esta insertando
            self.conectar()  # va lamar all constructor, crea con y conector
            self.conector.execute(sql, (gru.descripcion))  # en una tupla enviamos los partametros de s
            self.conn.commit()
        except:
            result = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def modificar(self, grupo, id):
        correcto = True
        try:
            sql = "update grupo set descripcion = %s where idgrupo = %s"  # para seguridad enviamos %s, no se sepa lo
            # que se esta insertando
            self.conectar()  # va lamar all constructor, crea con y conector
            self.conector.execute(sql, (grupo.descripcion, id))  # e una tupla enviamos los partametros de s
            self.conn.commit()
        except:
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eliminar(self, id):
        correcto = True
        try:
            sql = "Delete from grupo where idgrupo = %s"  # para seguridad enviamos %s, no se sepa lo
            # que se esta insertando
            self.conectar()  # va lamar all constructor, crea con y conector
            self.conector.execute(sql, (id))  # e una tupla enviamos los partametros de s
            self.conn.commit()
        except:
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
