n1 = (input('Digite um numero: '))
n2 = (input('Digite outro: '))
s = n1 + n2

#print('A soma entre {} e {} é {}'.format(n1, n2, s))
print(f'A soma entre {int(n1)} e {int(n2)} é {int(n1) + int(n2)}')

print(n1.isalpha())
print(n1.isnumeric())
print(n1.isalnum())