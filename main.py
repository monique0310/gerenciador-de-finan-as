from usuario import Usuario
from gerenciador import Gerenciador
from gasto import Gasto
import getpass

gerenciador = Gerenciador()
while True:
  
    if gerenciador.usuario_logado == None:
        print("-------Bem Vindo ao seu organizador financeiro---------")
        print("1. cadastrar usuário")
        print("2. entrar")

        op = input("Escolha uma opcao:")
        if op == '1':
            nome = input('informe seu nome:')
            senha = getpass.getpass('crie uma senha:')
            novo_usuario = Usuario(nome, senha)
            gerenciador.cadastrar_usuario(novo_usuario)
        
        if op == '2':
            nome = input('informe seu nome:')
            senha = getpass.getpass('digite a senha:')
            gerenciador.login(nome, senha)
        
    if gerenciador.usuario_logado:

        print("-------Bem Vindo ao seu organizador financeiro---------")
        print("1. incluir gasto")
        print("2. gerar relatorio de gastos")
        print("3. editar gasto")
        print("4. excluir gasto")
        print("5. alterar senha")
        print("6. excluir conta")
        print("7. adicionar categoria")
        print("8. excluir categoria")
        print("9. sair")
        op = input("Escolha uma opcão:")

        if op == '1':
            titulo = input('informe o tituto que deseja dar ao gasto:')
            while True:
                try:
                    valor = float(input('qual valor gasto: '))
                    break
                except:
                    print("digite um valor valido")
            data = input('data da compra: ')
            forma_pagamento = ["Débito", "Crédito", "Dinheiro"]
            for i, item in enumerate(forma_pagamento, 1):
                        print(f"{i}. {item}")
            while True:
                try:
                    pagamento = int(input('forma de pagamento: '))
                    pg = forma_pagamento[pagamento - 1]
                    break
                except:
                    print("digite um indice válido")
            gerenciador.listar_categoria()
            while True:
                try:
                    escolha = int(input('Digite o indice da categoria: '))
                    categoria = gerenciador.usuario_logado.categorias[escolha - 1]
                    break
                except:
                    print("digite um indice valido")
            gasto = Gasto(titulo, valor, data, pg, categoria)
            gerenciador.incluir_gasto(gasto)

        if op == '2':
            gerenciador.listar_gasto()
            print("1. ver detalhes de um gasto especifico \n2. ver gastos por categoria \n3.ver gasto mensal \n4. ver gasto anual")
            sub_op = input("escolha uma opcao: ")
            if sub_op == "1":
                id_escolhido = input("digite o id para ver os detalhes (ou Enter para voltar): ")
                if id_escolhido:
                    achei = gerenciador.buscar_gasto(id_escolhido)
                    print(achei)
            if sub_op == "2":
                for categoria, total in gerenciador.relatorio_categoria().items():
                    print(f"{categoria}: R${total}")
            if sub_op == "3":
                mes = input("informe o número do mes: ")
                ano = input("informe o ano")
                if mes.isdigit() and ano.isdigit():
                    lista, soma = gerenciador.relatorio_mensal(mes, ano)
                    print(f"gastos:")
                    for item in lista:
                        print(item.exibir_resumo())
                    print(f"Valor total gasto: {soma}")
                else:
                    print("formato de mes ou ano invalido")
            if sub_op == "4":
                ano = input("informe o ano")
                if ano.isdigit():
                    lista, soma = gerenciador.relatorio_anual(ano)
                    print(f"gastos:")
                    for item in lista:
                        print(item.exibir_resumo())
                    print(f"Valor total gasto: {soma}")
                else: 
                    print("apenas numeros")


        
    if op == '3':
        while True:
            id = input("digite o id do gasto que deseja editar:")
            if id.isdigit():
                break
            print("digite um id válido")

        titulo = input('informe o tituto que deseja dar ao gasto (ou Enter para pular):')

        while True:
            valor = input('qual valor gasto (ou Enter para pular): ')
            if valor == "":
                valor = None
                break
            try:
                valor = float(valor)
                break
            except:
                print("digite um valor válido")

        data = input('data da compra (ou Enter para pular): ')

        forma_pagamento_lista = ["Débito", "Crédito", "Dinheiro"]
        print("(ou Enter para pular)")
        for i, item in enumerate(forma_pagamento_lista, 1):
            print(f"{i}. {item}")
        while True:
            escolha_pg = input("forma de pagamento: ")
            if escolha_pg == "":
                forma_pagamento = None
                break
            try:
                forma_pagamento = forma_pagamento_lista[int(escolha_pg) - 1]
                break
            except:
                print("digite um indice válido")

        gerenciador.listar_categoria()
        while True:
            escolha = input("Digite o número da categoria (ou Enter para pular): ")
            if escolha == "":
                categoria = None
                break
            try:
                categoria = gerenciador.usuario_logado.categorias[int(escolha) - 1]
                break
            except:
                print("digite um indice valido")

        gerenciador.editar_gasto(id, titulo, valor, data, forma_pagamento, categoria)

        if op == "4":
            id_gasto = input("informe o id do gasto que deseja remover?")
            gerenciador.excluir_gasto(id_gasto)

        if op == "6":
            senha = getpass.getpass("digite sua senha:")
            gerenciador.excluir_usuario(senha)
        
        if op == '7':
            nova_categoria = input("nome da nova categoria: ")
            gerenciador.adicionar_categoria(nova_categoria)
        
        if op == "8":
            gerenciador.listar_categoria()
            escolha = int(input("escolha a categoria a ser removida: "))
            remover_categoria = gerenciador.usuario_logado.categorias[escolha - 1]
            gerenciador.excluir_categoria(remover_categoria)

        if op == "9":
            gerenciador.logout()
            


