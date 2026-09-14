peso = float(input('qual é o seu peso: '))
altura = float(input('qual é sua altura: '))
imc = peso / pow(altura, 2)

if imc > 40 :
    print(f'o IMC dessa pessoa é de {imc:.1f}\n'
          f'você está em \033[31mOBESIDADE MÓRBIDA\033[m, cuidado!')
elif imc >= 30 :
    print(f'o IMC dessa pessoa é de {imc:.1f}\n'
          f'você está em \033[33mOBESIDADE!\033[m')
elif imc >= 25:
    print(f'o IMC dessa pessoa é de {imc:.1f}\n'
          f'você está em \033[35mSOBREPESO\033[m')
elif imc >= 18.5:
    print(f'o IMC dessa pessoa é de {imc:.1f}\n'
          f'PARABÉNS, você está na faixa de \033[32mPESO IDEAL\033[m')
else :
    print(f'o IMC dessa pessoa é de {imc:.1f}\n'
          f'você está \033[36mABAIXO DO PESO\033[m normal')
