from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_bravo = Restaurante('bravo', 'Gourmet')
bebida_cerveja = Bebida('Stella Artois', 9.99,'330ml')
bebida_cerveja.aplicar_desconto()
prato_parmegiana = Prato('Filé à parmegiana',45.00,'O melhor Filé à parmegiana da cidade')
prato_parmegiana.aplicar_desconto()
restaurante_bravo.adicionar_no_cardapio(bebida_cerveja)
restaurante_bravo.adicionar_no_cardapio(prato_parmegiana)

def main():
    restaurante_bravo.exibir_cardapio

if __name__ == '__main__':
    main()