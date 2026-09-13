salario = float(input('qual é o salário do funcionário? R$'))

if (salario <= 1250) :
    print(f'quem ganhava \033[0;31mR${salario:.2f}\033[m passa a ganhar \033[1;32mR${((salario * 0.15) + salario):.2f}\033[m agora.')
else:
    print(f'quem ganhava \033[31mR${salario:.2f}\033[m passa a ganhar \033[32mR${((salario * 0.10) + salario):.2f}\033[m agora.')
