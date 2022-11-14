class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None
    
    @property
    def nome(self):
        return self.__nome.title()

    @property
    def ferramenta(self):
        return self.__ferramenta

    def ferramenta(self, tipo):
        self.__ferramenta = tipo
        return self.__ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print("Caneta está escrevendo...")



class MaquinaDeEscrever:
    def escrever(self):
        print("Maquina está escrevendo...")

