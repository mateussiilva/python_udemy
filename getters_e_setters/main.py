


class Produto():
    def __init__(self, nome,preco):
        self.nome = nome
        self.preco = preco
        
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, text):
        if isinstance(text, str):
            if len(text) > 0:
                self._nome = text.upper()
            else:
                pass
        return text




    # GETTER
    @property
    def preco(self):
        return self._preco

    # SETTER

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = valor.replace("R$",'')
            valor = float(valor)
        self._preco = valor
        return valor

p1 = Produto("Camiseta 1", 50)
p1.desconto(10)


p2 = Produto("Caneca", "R$15")
p2.desconto(10)


print(p1.nome,p1.preco)
print(p2.nome,p2.preco)
