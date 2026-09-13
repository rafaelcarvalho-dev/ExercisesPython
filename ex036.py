valorCasa = float(input('valor da casa: R$'))
salarioComprador = float(input('salário do comprador: R$'))
financiamento = int(input('quantos anos de financiamento? '))

prestacaoMensal = valorCasa / (financiamento * 12)

if(prestacaoMensal > salarioComprador * 0.30):
    print(f'para pagar uma casa de R${valorCasa:.2f} em {financiamento} anos a prestação será de \033[33mR${prestacaoMensal:.2f}\033[m\n'
          f'empréstimo \033[31mNEGADO!\033[m')
else :
    print(f'para pagar uma casa de R${valorCasa:.2f} em {financiamento} anos a prestação será de \033[33mR${prestacaoMensal:.2f}\033[m\n'
          f'empréstimo \033[32mAPROVADO!\033[m')