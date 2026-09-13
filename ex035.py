print(f'\033[33m{'-=-' * 10}\033[m\n'
      f'analisador de triângulos\n'
      f'\033[33m{'-=-' * 10}\033[m')

primeiroSegmento = float(input('primeiro segmento: '))
segundoSegmento = float(input('segundo segmento: '))
terceiroSegmento = float(input('terceiro segmento: '))

if (primeiroSegmento + segundoSegmento > terceiroSegmento) :
    print(f'os segmentos acima \033[32;40mPODEM FORMAR\033[m triângulo!')
else :
    print(f'os segmentos acima \033[31;40mNÃO PODEM FORMAR\033[m triângulo!')