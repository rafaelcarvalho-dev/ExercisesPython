from random import choice

primeiroAluno = input('primeiro aluno: ')
segundoAluno = input('segundo aluno: ')
terceiroAluno = input('terceiro aluno: ')

alunos = [primeiroAluno, segundoAluno, terceiroAluno]

print(f'O aluno sorteado foi: {choice(alunos)}')
