from plancuentas.dao import daoPlan


class ctrPlan:
    def __init__(self, grup=None):
        self.grupo = grup

    def consulta(self):
        objDao = daoPlan()  # instancia
        return objDao.consultar()  # realiza el select return result diccioario

    def ingresar(self, plan):
        objDao = daoPlan()  # instancia
        return objDao.ingresar(plan)

    def modificar(self, plan, id):
        objDao = daoPlan()
        return objDao.modificar(plan, id)

    def eliminar(self, id):
        objDao = daoPlan()
        return objDao.eliminar(id)