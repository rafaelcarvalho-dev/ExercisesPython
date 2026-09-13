from datetime import date

ano = int(input('que ano quer analisar? coloque 0 para analisar o ano atual: '))

if (ano == 0) :
    ano = date.today().year
if (ano % 100 != 0 and ano % 400 == 0) or (ano % 4 == 0) :
    print(f'o ano {ano} é BISSEXTO')
else :
    print(f'o ano {ano} NÃO é BISSEXTO')