
velocidade = int(input('Qual é a velocidade do carro: '))

condicao = (velocidade - 80) * 7

if (velocidade > 80) :

    print(f'MULTADO! você excedeu o limite permitido que é de 80Km\n'
          f'você deve pagar uma multa de R${condicao:.2f}!\n'
          f'tenha um bom dia! dirija com segurança!')
else :
    print(f'tenha um bom dia! dirija com segurança!')
