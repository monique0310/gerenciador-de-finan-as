class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha 
        self.categorias = ["Alimentacao", "Transporte", "Contas", "Lazer"]

    def __str__(self):
        return f"Nome de usuário: {self.nome}"