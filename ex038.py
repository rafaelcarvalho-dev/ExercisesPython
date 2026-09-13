primeiroNumero = int(input('primeiro número: '))
segundoNumero = int(input('segundo número: '))

if primeiroNumero == segundoNumero :
    print(f'os dois valores são \033[33mIGUAIS\033[m')
elif primeiroNumero > segundoNumero :
    print(f'o \033[32mPRIMEIRO\033[m valor é maior')
else :
    print(f'o \033[31mSEGUNDO\033[m valor é maior')