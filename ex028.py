from random import randint
from time import sleep

print('vou pensar em um número entre 0 e 5. tente adivinhar...')

numero = int(input('em que número eu pensei: '))

condicao = randint(0, 6)

print('PROCESSANDO...')
sleep(3)

if (numero == condicao) :
    print(f'PARABÉNS! você conseguiu me vencer!')
else :
    print(f'GANHEI! eu pensei no número {condicao} e não no {numero}!')