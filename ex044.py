print('=' * 10 + ' LOJAS CARVALHO ' + '=' * 10)

compra = float(input('preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n'
      '[ 1 ] à vista dinheiro/pix\n'
      '[ 2 ] à vista cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão')
condicao = int(input('qual é a opção: '))

if condicao == 1 :
    desconto10 = compra - (compra * 0.10)
    print(f'sua compra de R${compra:.2f} vai custar \033[32mR${desconto10:.2f}\033[m no final.')
elif condicao == 2 :
    desconto5 = compra - (compra * 0.05)
    print(f'sua compra de R${compra:.2f} vai custar \033[32mR${desconto5:.2f}\033[m no final.')
elif condicao == 3 :
    print(f'sua compra será parcelada em 2x de R${compra / 2:.2f} SEM JUROS\n'
          f'sua compra vai custar \033[33mR${compra:.2f}\033[m no final.')
elif condicao == 4 :
    parcela = int(input('quantas parcelas: '))
    if parcela >= 3 :
        precoFinal = compra + (compra * 0.20)
        print(f'sua compra será parcelada em {parcela}x de R${precoFinal / parcela:.2f} COM JUROS\n'
              f'sua compra de R${compra:.2f} vai custar \033[31mR${precoFinal:.2f}\033[m no final.')
    else :
        print(f'\033[31mFORMA DE PAGAMENTO INVÁLIDO!\033[m')
else :
    print('\033[31mOPÇÃO INVÁLIDA!\033[m')