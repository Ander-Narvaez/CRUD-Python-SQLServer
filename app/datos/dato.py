class Dato():
    __aId_         = int
    __aTexto       = str
    __aDescripcion = str

    def __init__(self, pId_, ptexto, pdescripcion):
        self.__aId_repuesto  = pId_
        self.__aModelo       = ptexto
        self.__aNombre       = pdescripcion
 
    def getaId_(self):
         return self.__aId_

    def setaId_(self, aId_):
         self.__aId_repuesto = aId_

    def getaTexto(self):
         return self.__aTexto

    def setaTexto(self, aTexto):
        self.__aModelo = aTexto

    def getaDescripcion(self):
         return self.__aDescripcion

    def setaDescripcion(self, aDescripcion):
         self.__aDescripcion = aDescripcion
 
    def get_attributes(self):
        return [self.getaId, self.getaModelo, self.getaNombre()]

    def get_list_insert_db(self):
        return [self.getaModelo, self.getaNombre(),
                self.getaPrecio(), self.getaDescuesto()]

    def get_list_update_db(self):
        return [self.getaId_repuesto, self.getaModelo, self.getaNombre(),
                self.getaPrecio(), self.getaDescuesto()]

    def __str__(self):
        return ('Id_repuesto:  '+ self.__aId_repuesto + 
                '\nModelo      '+ self.__aModelo      +  
                '\Nombre:      '+ self.__aNombre      )     