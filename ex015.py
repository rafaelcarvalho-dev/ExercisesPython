diasUsado = int(input('Quantos dias alugados ? '))
qntdRodado = float(input('Quantos Km rodados ? '))

print(f'O total a pagar é de R${(diasUsado * 60) + (qntdRodado * 0.15):.2f}')