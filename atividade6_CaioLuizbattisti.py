municipio =input("Digite o nome do municipio: ")
eleitores=int(input("Digite a quantidade total de eleitores: "))
votos_mais_votados=int(input("digite a quantidade de votos do canditado mais votado: "))
porcentagem = (votos_mais_votados / eleitores)*100
if eleitores >=200.000 and porcentagem <= 50:
    print("no municipio de",municipio,"havera segundo turno.")
else:
    print("no municipio de",municipio,"nao havera segundo turno.")