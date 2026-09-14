print(f'\033[33m{'-=-' * 10}\033[m\n'
      f'analisador de triângulos\n'
      f'\033[33m{'-=-' * 10}\033[m')

segmento1 = float(input('primeiro segmento: '))
segmento2 = float(input('segundo segmento: '))
segmento3 = float(input('terceiro segmento: '))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2 :
    if segmento1 == segmento2 == segmento3 :
        print(f'os segmentos acima \033[32;40mPODEM FORMAR\033[m um triângulo EQUILÁTERO!')
    elif segmento1 != segmento2 != segmento3 != segmento1 :
        print(f'os segmentos acima \033[32;40mPODEM FORMAR\033[m um triângulo ESCALENO!')
    else :
        print(f'os segmentos acima \033[32;40mPODEM FORMAR\033[m um triângulo ISÓSCELES!')
else :
    print(f'os segmentos acima \033[31;40mNÃO PODEM FORMAR\033[m triângulo!')