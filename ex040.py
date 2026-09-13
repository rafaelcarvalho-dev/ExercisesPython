primeiraNota = float(input('primeira nota: '))
segundaNota = float(input('segunda nota: '))

media = (primeiraNota + segundaNota) / 2

if media >= 7 :
    print(f'tirando {primeiraNota} e {segundaNota}, a média do aluno é {media:.2f}\n'
          f'o aluno está \033[32mAPROVADO!\033[m')
elif media >= 5 and media <= 6.5 :
    print(f'tirando {primeiraNota} e {segundaNota}, a média do aluno é {media:.2f}\n'
          f'o aluno está em \033[33mRECUPERAÇÃO.\033[m')
else :
    print(f'tirando {primeiraNota} e {segundaNota}, a média do aluno é {media:.2f}\n'
          f'o aluno está \033[31mREPROVADO!\033[m')