class Produto:
    def __init__(self, nome, vlr_compra, vlr_venda, qtd_estoque, qtd_minima):
        self.nome = nome
        self.vlr_compra = vlr_compra
        self.vlr_venda = vlr_venda
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima

    def get_nome (self):
        return self.nome

    def get_vlr_venda (self):
        return self.vlr_venda

    def set_nome (self, novo_nome):
        self.nome = novo_nome

    def set_vlr_venda(self, novo_vlr):
        self.vlr_venda = novo_vlr

    def mostra_dados (self):
        print('Nome:', self.nome)
        print('Valor da compra:', self.vlr_compra)
        print('Valor da venda:', self.vlr_venda)
        print('Quantidade do estoque:', self.qtd_estoque)
        print('Quantidade minima:', self.qtd_minima)

    def calcula_lucro(self):
      vlr_lucro = self.vlr_venda - self.vlr_compra
      return vlr_lucro