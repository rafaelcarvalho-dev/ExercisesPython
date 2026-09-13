distancia = int(input('qual é a distância da sua viagem? '))


if (distancia <= 200) :
    print(f'você está prestes a começar uma viagem de {distancia:.1f}Km\n'
          f'o preço da sua passagem será de R${(distancia * 0.50):.2f}')
else :
    print(f'você está prestes a começar uma viagem de {distancia:.1f}\n'
          f'o preço da sua passagem será de R${(distancia * 0.45):.2f}')