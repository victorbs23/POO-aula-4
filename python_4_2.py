from python_4 import Produto

if __name__ == '__main__':
    prod_1 = Produto('Arroz', 29.00, 37.50, 67, 20)
    print('Objeto criado:', prod_1)
    prod_2 = Produto('Farinha', 9.00, 11.50, 87, 25)
    print('Objeto criado:', prod_2)

    print('________________________________________________________')

    print('Produto 1:', prod_1.get_nome())
    print('Valor da compra:', prod_1.get_vlr_venda())

    print('________________________________________________________')

    print('Produto 2:', prod_2.get_nome())
    print('Valor da venda:', prod_2.get_vlr_venda())

    print('________________________________________________________')

    prod_1.set_vlr_venda(39.00)

    print('Produto 1:', prod_1.get_nome())
    print('Valor alterado:', prod_1.get_vlr_venda())

    print('________________________________________________________')

    vlr_digitado = float(input('Digite um valor:'))
    prod_1.set_vlr_venda(vlr_digitado)
    print('Valor do produto:', prod_1.get_vlr_venda())

    print('Dados do Produto 1')
    prod_1.mostra_dados ()

    print('________________________________________________________')

    print('Dados do produto 2:')
    prod_2.mostra_dados()

    print('________________________________________________________')

    print('Valor dos lucros produto 1:', prod_1.calcula_lucro())