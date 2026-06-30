class Gasto:
    def __init__(self, titulo, valor, data, forma_pagamento, categoria):
        self.titulo = titulo
        self.valor = valor
        self.data = data
        self.forma_pagamento = forma_pagamento
        self.categoria = categoria #alimentação, farmacia, etc
        self.id = None

    def __str__(self):
        return (f"Gasto: {self.titulo}\n"
                f"R${self.valor}\n"
                f"data: {self.data}\n" 
                f"forma de pagamento: {self.forma_pagamento}\n"
                f"categoria: {self.categoria}\n"
                f"id: {self.id}")
    
    def exibir_resumo(self):
        return(f"Gasto: {self.titulo}\n"
               f"R$: {self.valor}\n"
               f"id: {self.id}\n")
