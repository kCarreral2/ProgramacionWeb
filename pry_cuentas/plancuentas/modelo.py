class modPlan:
    def __init__(self,cod='',gru=0,des='',nat='', est=True):
        self.__codigo = cod
        self.__grupoid = gru
        self.__descripcion = des
        self.__naturaleza = nat
        self.__estado = est

    @property
    def codigo(self):
        return  self.__codigo

    @codigo.setter
    def codigo(self, cod):
        self.__codigo = cod

    @property
    def grupoid(self):
        return  self.__grupoid

    @grupoid.setter
    def grupoid(self, gru):
        self.__grupoid = gru

    @property
    def descripcion(self):
        return  self.__descripcion

    @descripcion.setter
    def descripcion(self, des):
        self.__descripcion = des

    @property
    def naturaleza(self):
        return  self.__naturaleza

    @naturaleza.setter
    def naturaleza(self, nat):
        self.__naturaleza = nat

    @property
    def estado(self):
        return  self.__estado

    @estado.setter
    def estado(self, est):
        self.__estado = est
