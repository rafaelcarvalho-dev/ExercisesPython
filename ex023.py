numero = input('informe um número: ')

calculo = numero.zfill(4)  #zfill(nº) garante smp a qntd de numeros

print(f'analisando o número {numero}\n'
      f'unidade: {calculo[0]}\n'
      f'dezena: {calculo[1]}\n'
      f'centena: {calculo[2]}\n'
      f'milhar: {calculo[3]}\n')