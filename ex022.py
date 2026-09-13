nome = str(input('digite seu nome completo: ')).strip()
primeiroNome = nome.split()

print(f'analisando seu nome completo...\n'
      f'seu nome em maiúsculas é {nome.upper()}\n'
      f'seu nome em minúsculas é {nome.lower()}\n'
      f'seu nome tem ao todo {len(nome) - nome.count(" ")} letras\n'
      f'seu primeiro nome é {primeiroNome[0]} e ele tem {len(primeiroNome[0])} letras')