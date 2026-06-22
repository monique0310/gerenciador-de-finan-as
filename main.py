from usuario import Usuario
from gerenciador import Gerenciador
from gasto import Gasto

print("-------Bem Vindo ao seu organizador financeiro---------")
print("1. cadastrar usuário")
print("2. cadastrar gasto")
print("3. gerar relatorio")
print("4. editar gasto")
print("5. excluir gasto")
print("6. excluir usuario")

gerenciador = Gerenciador()
while True:
    op = input("Escolha uma opcão:")
    if op == '1':
        nome = input('informe seu nome:')
        senha = input('crie uma senha:')
        novo_usuario = Usuario(nome, senha)
        gerenciador.cadastrar_usuario(novo_usuario)

    if op == '2':
        titulo = input('informe o tituto que deseja dar ao gasto:')
        valor = input('qual valor gasto: ')
        estabelecimento = input('nome do estabelecimento: ')
        data = input('data da compra: ')
        forma_pagamento = input('forma de pagamento: ')
        categoria = input('categoria (mercado, lazer, farmacia...):')
        tipo = input('gasto fixo ou variavel?')
        id = input('id')

        gasto = Gasto(titulo, valor, estabelecimento, data, forma_pagamento, categoria, tipo, id)
        gerenciador.incluir_gasto(gasto)

    if op == '3':
        gerenciador.listar_gasto()

    if op == '4':
        id = input("digite o id do gasto que deseja editar:")
        titulo = input('informe o tituto que deseja dar ao gasto:')
        valor = input('qual valor gasto: ')
        estabelecimento = input('nome do estabelecimento: ')
        data = input('data da compra: ')
        forma_pagamento = input('forma de pagamento: ')
        categoria = input('categoria (mercado, lazer, farmacia...):')
        tipo = input('gasto fixo ou variavel?')

        gerenciador.editar_gasto(id, titulo, valor, estabelecimento, data, forma_pagamento, categoria, tipo)

    if op == "5":
        id_gasto = input("informe o id do gasto que deseja remover?")
        gerenciador.excluir_gasto(id_gasto)

    if op == "6":
        nome = input("informe seu nome:")
        gerenciador.excluir_usuario(nome)


