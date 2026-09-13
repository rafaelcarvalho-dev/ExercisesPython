primeiroNumero = int(input('primeiro valor: '))
segundoNumero = int(input('segundo valor: '))
terceiroNumero = int(input('terceiro valor: '))

menor = min(primeiroNumero, segundoNumero, terceiroNumero)
maior = max(primeiroNumero, segundoNumero, terceiroNumero)

print(f'o menor valor digitado foi {menor}\n'
      f'o maior valor digitado foi {maior}')