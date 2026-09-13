from datetime import date

anoNascimento = int(input('ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento


if idade == 18 :
    print(f'quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}.\n'
          f'você tem que se alistar IMEDIATAMENTE!')
elif idade > 18 :
    print(f'quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}.\n'
          f'você já deveria ter se alistado há {anoAtual - (anoNascimento + 18)} anos.\n'
          f'seu alistamento foi em {anoNascimento + 18}')
else :
    print(f'quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}\n'
          f'ainda faltam {(anoNascimento + 18) - anoAtual} anos para o alistamento\n'
          f'seu alistamento será em {anoNascimento + 18}')