from grupo.dao import daoGrupo


class ctrGrupo:
    def __init__(self, grup=None):
        self.grupo = grup

    def consulta(self):
        objDao = daoGrupo()  # instancia
        return objDao.consultar()  # realiza el select return result diccioario

    def ingresar(self, gru):
        objDao = daoGrupo()  # instancia
        return objDao.ingresar(gru)

    def modificar(self, gru, id):
        objDao = daoGrupo()
        return objDao.modificar(gru, id)

    def eliminar(self, id):
        objDao = daoGrupo()
        return objDao.eliminar(id)