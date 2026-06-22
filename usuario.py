class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha 

    def __str__(self):
        return f"Nome de usuário: {self.nome}"