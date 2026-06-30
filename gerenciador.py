class Gerenciador:
    def __init__(self):
        self.gastos = []
        self.usuarios = []
        self.usuario_logado = None
    
    #métodos de gasto
    def incluir_gasto(self, gasto:Gasto):
        gasto.id = len(self.gastos) + 1
        self.gastos.append(gasto)
        print(f"gasto {gasto.titulo} incluido com sucesso!")
    
    def buscar_gasto(self, id_procurado):
        try: 
            id_procurado = int(id_procurado)
        except:
            print("digite um numero de id")
            return None
        for gasto in self.gastos:
            if int(id_procurado) == gasto.id:
                return gasto

    def excluir_gasto(self, id_procurado):
        achei = self.buscar_gasto(id_procurado)
        if achei:
            self.gastos.remove(achei)
            print('gasto excluido com sucesso!')
        else:
            print('gasto não encontrado!') 

    def editar_gasto(self, id_procurado, titulo_novo=None, valor_novo=None,
     data_novo=None, forma_pagamento_novo=None, categoria_novo=None):
        try: 
            id_procurado = int(id_procurado)
        except:
            print("digite um numero de id")
            return None
        
        for gasto in self.gastos:
            if id_procurado == gasto.id:
                if titulo_novo is not None and titulo_novo.strip() != "":
                    gasto.titulo = titulo_novo
                
                if valor_novo is not None:
                    gasto.valor = valor_novo

                if data_novo is not None and data_novo.strip() != "":
                    gasto.data = data_novo

                if forma_pagamento_novo is not None:
                    gasto.forma_pagamento = forma_pagamento_novo

                if categoria_novo is not None:
                    gasto.categoria = categoria_novo

                print("Gasto atualizado com sucesso!")
                return True
        print("Id não encontrado!")
        return False
                      
    def listar_gasto(self):
        print("---- lista de gastos ----")
        for gasto in self.gastos:
            print(gasto.exibir_resumo())
    
    #métodos usuario
    def cadastrar_usuario(self, usuario:Usuario):
        self.usuarios.append(usuario)
        print(f"{usuario.nome} cadastrado com sucesso!")

       
    def buscar_usuario(self, nome_procurado):
        for usuario in self.usuarios:
            if nome_procurado == usuario.nome:
                return usuario

    def excluir_usuario(self, senha):
            if senha == self.usuario_logado.senha:
                self.usuarios.remove(self.usuario_logado)
                self.logout()
                print('usuario excluido com sucesso!')
            else:
                print('senha incorreta!')
        

    def login(self, nome_usuario, senha):
        usuario_encontrado = self.buscar_usuario(nome_usuario)
        if usuario_encontrado:
            if senha == usuario_encontrado.senha:
                self.usuario_logado = usuario_encontrado
                print(f"Bem-Vindo(a) {usuario_encontrado.nome}!")
            else:
                print(f"senha incorreta!")
        else:
            print("usuario não encontrado!")

    def logout(self):
        self.usuario_logado = None
        print("Até logo!")
    
    #metodos de categoria
    def adicionar_categoria(self, categoria):
        self.usuario_logado.categorias.append(categoria)

    def listar_categoria(self):
        print("Categorias: ")
        for i, item in enumerate(self.usuario_logado.categorias, 1):
            print(f"{i}. {item}")

    def excluir_categoria(self, categoria_excluir):
        if categoria_excluir in self.usuario_logado.categorias:
            for gasto in self.gastos:
                if gasto.categoria == categoria_excluir:
                    print("existem gastos nestas categorias!")
                    break
            else:
                self.usuario_logado.categorias.remove(categoria_excluir)
                print("categoria removida!")
        else:
            print("não encontrado!")

    def relatorio_categoria(self):
        relatorio = {}
        for gasto in self.gastos:
            if gasto.categoria in relatorio:
                relatorio[gasto.categoria] = relatorio[gasto.categoria] + float(gasto.valor)
            else:
                relatorio[gasto.categoria] = float(gasto.valor)
        return relatorio
    def relatorio_mensal(self, mes, ano):
        lista_gasto = []
        soma_mes = 0
        for gasto in self.gastos:
            try:
                partes = gasto.data.split("/")
            except:
                continue
            if mes == partes[1] and ano == partes[2]:
                soma_mes += float(gasto.valor)
                lista_gasto.append(gasto)
        if not lista_gasto: 
            print("mes ou ano incorretos!")
        return lista_gasto, soma_mes


    def relatorio_anual(self, ano):
        soma_ano = 0
        lista_gasto = []
        for gasto in self.gastos:
            try:
                partes = gasto.data.split("/")
            except:
                continue
            if ano == partes[2]:
                soma_ano += float(gasto.valor)
                lista_gasto.append(gasto)
        if not lista_gasto:
            print("ano invalido")
        return lista_gasto, soma_ano









    
           



