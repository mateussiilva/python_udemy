
# Um metodo não é nada mesmo que uma função dentro de uma classe

#   SETTER = CONFIGURANDO UM VALOR (=)
#   GETTER = OBTER UM VALOR (.)

""" 
Eu posso ter  GETTER  sem precisar de um SETTER,
mas NÃO conseguino ter um SETTER sem um GETTER.
 
O Getter pode retornar qualquer coisa não precisa se um atributo da classe, podemo retornar uma str um float ou int ou outra coisa que precisamos! 

Quando criamos um SETTER ou GETTER estamos indicando para o python que aquela função deve se comportar como um atributo e não mais como um metodo, por isso quando chamamos esse "atributo" não precimos colocar os parenteses 
-----------------------//---------------------------

Para criarmos um setter precisomos definir o decorator com o nome do GETTER que que criamos ".setter". 
Exemplo:

    class Pessoa():
        @property  #MEU GETTER
        def nome(self):
            return 

        @nome.setter
        def nome(self, nome):
            # o parametro nome é o atributo que vai ser retorando pelo GETTER para que ele possa ser usado dentro do setter para aplicarmos as devidas configuração
            #  nesse caso estamos retorando o "nome" todo em maiusculo
            return nome.upper() 


O GETTER e o SETTER precisam ter o mesmo nome


"""

class Pessoa():
    # O INIT é responsalvel por inicilar os atributos ele é chamado antes de qual outro metodo ou GETTER ou um SETTER
    def __init__(self,nome) -> None:
        self.nome =  nome   

    @property # Esse decorator indiaca pro python que esse "metodo" é na verdade um
    # atributo
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        print("SETTER EXECUTADO")
        self._nome = nome

p1 = Pessoa("Mateus")
print(p1.nome)

