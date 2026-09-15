from random import randint
from time import sleep

opcao = ('pedra', 'papel', 'tesoura')
jogadaComputador = randint(0,2)

print('suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')

jogada = int(input('qual é a sua jogada? '))

print('\033[34mJO\033[m')
sleep(1)
print('\033[34mKEN\033[m')
sleep(1)
print('\033[34mPO!!!\033[m')

if jogada >= 0 and jogada <= 2 and jogadaComputador >= 0 and jogadaComputador <= 2 :

    print('\033[37m-=-\033[m' * 8)
    print(f'computador jogou \033[35m{opcao[jogadaComputador]}\033[m\n'
          f'jogador jogou \033[35m{opcao[jogada]}\033[m')
    print('\033[37m-=-\033[m' * 8)

    if jogada == jogadaComputador :
        print('\033[33mEMPATE\033[m')
    else :
        if jogada == 0 and jogadaComputador == 1 or jogada == 1 and jogadaComputador == 2 or jogada == 2 and jogadaComputador == 0 :
            print('\033[31mJOGADOR PERDE\033[m')
        else :
            print('\033[32mJOGADOR VENCE\033[m')
else :
    print('\033[31mJOGADA INVÁLIDA!\033[m')