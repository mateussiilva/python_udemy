# ENCAPSULAMENTO

""" 
public = são metodos e atributos que pode ser acessados dentro e fora da classe 
protected = atributos que podem ser acessados dentro da classe ou pela as filhas da classe(a famosa herança)
private = significa que aquele metodo só está disponivel dentro da classe


EM PYTHON NÃO EXISTE essas palavras citadas ai cima
mas para conseguimos trabalhar com oriteção a objeto em python 
foram criadas algumas convenções

um underline(_) na frente do nome do atributo é para dizer que não devemos acessar este atributo

        _ == protected

    (privado, porem é um private fraco) mesmo com essa convenção ainda sim conseguimos acessar este atributo

    conseguimos acessar os atributos private/protected assim:
        instacia_classe._nomeAtributo

---------------------------------------

dois underline(__) na frente do nome do atributo ou metodo(função dentro das classe) significa que ele PRIVADO OU PRIVATE

        __ == private
        (privado então não conseguimos acessar o metodo ou atributo protegido com esse filosofia)

    conseguimos acessar os atributos private/protected assim:
        instacia_classe._no
        

"""

class BaseDeDados():
         #CONSTRUTOR  EM PYTHON
    def __init__(self):
        self.__dados_sigilosos = [ item for item in range(15)]
        self._dados = {}

    # INSERINDO DADOS 
    def insert_clientes(self,id, name):
        if "clientes" not in self._dados:
            self._dados["clientes"] = {id:name}
        else:
            self._dados["clientes"].update({id:name})



    # LISTAR CLIENTES
    def listar_clientes(self):
        for id,nome in self._dados["clientes"].items():
            print(id,nome)


    # APAGAR CLIENTE
    def delete_cliente(self,id):
        del self._dados["clientes"][id]

bd = BaseDeDados()
bd.insert_clientes(1, "Mateus")
bd.insert_clientes(2, "José")
bd.insert_clientes(3, "da Silva")
print(bd.)

bd.listar_clientes()

