from math import hypot
catetoOposto = float(input('Informe o valor do cateto oposto: '))
catetoAdjacente = float(input('Informe o valor do cateto adjacente: '))

print(f'O valor da hipotenusa é: {hypot(catetoOposto ,catetoAdjacente):.2f}')