# MASTERCLASSE
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
        self.nome_da_classe = self.__class__.__name__
    
    def falar(self):
        print(f"{self.nome_da_classe} falando...")



# A classe "Cliente" está herdando tudo que tem na classe "Pessoa"
# SUBCLASSE
class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nome_da_classe} comprando...")

        

# A classe "Aluno" está herdando tudo que tem na classe "Pessoa"    
# SUBCLASSE
class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nome_da_classe} estudando...")
    

    