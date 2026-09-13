from datetime import date

anoNascimento = int(input('ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade <= 9 :
    print(f'o atleta tem {idade} anos.\n'
          f'classificação: \033[36mMIRIM\033[m')
elif idade <= 14 :
    print(f'o atleta tem {idade} anos.\n'
          f'classificação: \033[35mINFANTIL\033[m')
elif idade <= 19 :
    print(f'o atleta tem {idade} anos.\n'
          f'classificação: \033[34mJUNIOR\033[m')
elif idade <= 25 :
    print(f'o atleta tem {idade} anos.\n'
          f'classificação: \033[33mSÊNIOR\033[m')
else :
    print(f'o atleta tem {idade} anos.\n'
          f'classificação: \033[31mMASTER\033[m')