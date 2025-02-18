#Escreva um programa para exibir na tela o nome e a categoria de um lutador.
#O programa deve ler string para o nome e um numero real para o peso.
#Conforme o peso ocorrera o enquadramento na categoria segundo essa tabela.
nome = input(("Qual nome do lutador? "))
peso =float(input("qual o seu peso? "))
if peso < (52):
    print("invalido, tente de novo!")
    print("CAIO LUIZ BATTISTI")
elif peso >= (52) and peso < (65):
    print(nome)
    print("peso pena")
    print("CAIO LUIZ BATTISTI")
elif peso >= (65) and peso < (72):
    print(nome)
    print("peso pena")
    print("CAIO LUIZ BATTISTI")
elif peso >= (72) and peso < (79):
    print(nome)
    print("peso ligeiro")
    print("CAIO LUIZ BATTISTI")
elif peso >= (79) and peso < (86):
    print(nome)
    print("peso meio medio")
    print("CAIO LUIZ BATTISTI")
elif peso >= (86) and peso < (90):
    print(nome)
    print("peso medio")
    print("CAIO LUIZ BATTISTI")
elif peso >= (90) and peso < (100):
    print(nome)
    print("meio pesado")
    print("CAIO LUIZ BATTISTI")
elif peso >= (100):
    print(nome)
    print("pesado")
    print("CAIO LUIZ BATTISTI")