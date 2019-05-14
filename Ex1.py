for i in range (0,10):
    x = str(input('Bom dia senhor, qual seu pedido? '))

    def valor(x):

        if x == 'Salgado':
            print('Seu pedido custa 4 reais.')

        elif x == 'Refrigerante':
            print('Seu pedido custa 4 reais e 50 centavos')
            

        elif x== 'Suco':
            print('Seu pedido custa 5 reais.')

        elif x == 'Sorvete':
            print('Seu pedido custa 6 reais.')

        elif x == 'Cafe':
            print('Seu pedido custa 4 reais.')

        elif x == 'Capuccino':
            print('Seu pedido custa 6 reais.')

        elif x == 'Bolo':
            print('Seu pedido custa 4 reais e 50 centavos.')

        elif x == 'Dadinho':
            print('Seu pedido custa 50 centavos.')
        
    valor(x)
