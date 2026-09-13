valor = input('Digite algo: ')

tipo = type(valor)

print(f'O tipo primitivo do valor é: {tipo}')

print(f'O valor é numérico? {valor.isnumeric()}')
print(f'O valor é alfabético? {valor.isalpha()}')
print(f'O valor é alfanumérico? {valor.isalnum()}')
print(f'O valor contém espaços? {valor.isspace()}')
print(f'O valor está em maiúscula? {valor.isupper()}')
print(f'O valor está em minúsculas? {valor.islower()}')
print(f'O valor está capitalizado? {valor.istitle()}')

