nome = input('digite seu nome completo: ').strip()

lista = nome.split()

print(f'muito prazer em te conhecer!\n'
      f'seu primeiro nome é {lista[0]}\n'
      f'seu último nome é {lista[len(lista)-1]}')