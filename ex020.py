from random import shuffle

primeiroAluno = input('primeiro aluno: ')
segundoAluno = input('segundo aluno: ')
terceiroAluno = input('terceiro aluno: ')
quartoAluno = input('quarto aluno: ')

alunos = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
shuffle(alunos)

print(f'A ordem de apresentação será\n'
      f'{alunos}')