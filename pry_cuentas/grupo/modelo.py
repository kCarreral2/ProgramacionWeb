class modGrupo:
    def __init__(self,des=''):
        self.__descripcion = des

    @property
    def descripcion(self):
        return  self.__descripcion

    @descripcion.setter
    def descripcion(self, des):
        self.__descripcion = des
