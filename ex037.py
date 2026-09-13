numero = int(input('digite um número inteiro: '))

print('escolha uma das bases para conversão: \n'
      '[ 1 ] converter para \033[4;33mBINÁRIO\033[m\n'
      '[ 2 ] converter para \033[4;31mOCTAL\033[m\n'
      '[ 3 ] converter para \033[34mHEXADECIMAL\033[m')

opcaoUsuario = int(input('sua opção: '))

if opcaoUsuario == 1 :
    print(f'{numero} convertido para \033[4;33mBINÁRIO\033[m é igual a \033[35m{bin(numero)}\033[m')
elif opcaoUsuario == 2 :
    print(f'{numero} convertido para \033[4;31mOCTAL\033[m é igual a \033[35m{oct(numero)}\033[m')
else :
    print(f'{numero} convertido para \033[34mHEXADECIMAL\033[m é igual a \033[35m{hex(numero)}\033[m')