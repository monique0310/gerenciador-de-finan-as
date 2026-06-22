class Gasto:
    def __init__(self, titulo, valor, estabelecimento,
                  data, forma_pagamento, categoria, tipo, id):
        self.titulo = titulo
        self.valor = valor
        self.estabelecimento = estabelecimento
        self.data = data
        self.forma_pagamento = forma_pagamento
        self.categoria = categoria #alimentação, farmacia, etc
        self.tipo = tipo #fixo ou variavel
        self.id = id

    def __str__(self):
        return (f"Gasto: {self.titulo}\n"
                f"R${self.valor}\n"
                f"estabelecimento: {self.estabelecimento}\n"
                f"data: {self.data}\n" 
                f"forma de pagamento: {self.forma_pagamento}\n"
                f"categoria: {self.categoria}\n"
                f"tipo: {self.tipo}"
                f"id: {self.id}")
