class Gerenciador:
    def __init__(self):
        self.gastos = []
        self.usuarios = []
    
    def incluir_gasto(self, gasto:Gasto):
        self.gastos.append(gasto)
        print(f"gasto {gasto.titulo} incluido com sucesso!")
    
    def buscar_gasto(self, id_procurado):
        for gasto in self.gastos:
            if id_procurado == gasto.id:
                return gasto

    def excluir_gasto(self, id_procurado):
        achei = self.buscar_gasto(id_procurado)
        if achei:
            self.gastos.remove(achei)
            print('gasto excluido com sucesso!')
        else:
            print('gasto não encontrado!')
        


    def editar_gasto(self, id_procurado, titulo_novo=None, valor_novo=None, estabelecimento_novo=None,
                  data_novo=None, forma_pagamento_novo=None, categoria_novo=None, tipo_novo=None):
        for gasto in self.gastos:
            if id_procurado == gasto.id:
                if titulo_novo is not None and titulo_novo.strip() != "":
                    gasto.titulo = titulo_novo
                
                if valor_novo is not None and valor_novo.strip() != "":
                    gasto.valor = valor_novo

                if estabelecimento_novo is not None and estabelecimento_novo.strip() != "":
                    gasto.estabelecimento = estabelecimento_novo
                
                if data_novo is not None and data_novo.strip() != "":
                    gasto.data = data_novo

                if forma_pagamento_novo is not None and forma_pagamento_novo.strip() != "":
                    gasto.forma_pagamento = forma_pagamento_novo

                if categoria_novo is not None and categoria_novo.strip() != "":
                    gasto.categoria = categoria_novo
                
                if tipo_novo is not None and tipo_novo.strip() != "":
                    gasto.tipo = tipo_novo

                print("Gasto atualizado com sucesso!")
                return True
        print("Id não encontrado!")
        return False
                      
    def listar_gasto(self):
        print("---- lista de gastos ----")
        for gasto in self.gastos:
            print(gasto)

    def cadastrar_usuario(self, usuario:Usuario):
        self.usuarios.append(usuario)
        print(f"{usuario.nome} cadastrado com sucesso!")

       
    def buscar_usuario(self, nome_procurado):
        for usuario in self.usuarios:
            if nome_procurado == usuario.nome:
                return usuario

    def excluir_usuario(self, nome):
        achei = self.buscar_usuario(nome)
        if achei:
            self.usuarios.remove(achei)
            print('usuario excluido com sucesso!')
        else:
            print('usuario não encontrado!')

