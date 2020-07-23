from conexion import Conector


class daoPlan(Conector):
    def __init__(self, server='localhost', usuario='root', password='', basedato='crud'):
        Conector.__init__(self, server='localhost', usuario='root', password='', basedato='crud')

    def consultar(self):
        result = True
        try:
            sql = "Select p.idplancuenta, p.codigo, g.descripcion, p.descripcion, case p.naturaleza when 'A' then 'ACREEDOR' when 'D' then 'DEUDOR' END AS naturalezap, case p.estado when 0 then 'FALSE' when 1 then 'TRUE' END AS estadop from plancuenta p, grupo g where p.grupoid = g.idgrupo"
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

    def ingresar(self, plan):
        result = True
        try:
            sql = "insert into plancuenta(codigo,grupoid,descripcion,naturaleza,estado)VALUES (%s,%s,%s,%s,%s)"  # para seguridad enviamos %s, no se sepa lo que se
            # esta insertando
            self.conectar()  # va lamar all constructor, crea con y conector
            self.conector.execute(sql, (plan.codigo,plan.grupoid,plan.descripcion,plan.naturaleza,plan.estado))  # en una tupla enviamos los partametros de s
            self.conn.commit()
        except:
            result = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def modificar(self, plan, id):
        correcto = True
        try:
            sql = "update plancuenta set codigo = %s , grupoid = %s, descripcion = %s, naturaleza = %s, estado = %s where idplancuenta = %s"  # para seguridad enviamos %s, no se sepa lo
            # que se esta insertando
            self.conectar()  # va lamar all constructor, crea con y conector
            self.conector.execute(sql, (plan.codigo,plan.grupoid,plan.descripcion,plan.naturaleza,plan.estado, id))  # e una tupla enviamos los partametros de s
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
            sql = "Delete from plancuenta where idplancuenta = %s"  # para seguridad enviamos %s, no se sepa lo
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
