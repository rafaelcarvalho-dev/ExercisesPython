cidade = input('Em que cidade você nasceu? ').lower()

lista = cidade.split()

primeiraPalavra = lista[0]

if (primeiraPalavra == 'santo'):
    print(True)
else :
    print(False)
