from math import cos,tan,sin,radians

angulo = int(input('Informe o ângulo: '))

print(f'O Seno do ângulo de {angulo} é: {sin(radians(angulo)):.2f}\n'
      f'O Cosseno do ângulo de {angulo} é: {cos(radians(angulo)):.2f}\n'
      f'A tangente do ângulo de {angulo} é: {tan(radians(angulo)):.2f}')