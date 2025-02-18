#
preco_custo =float(input("Digite o preço de custo do produto: "))
if preco_custo <=100:
    margem = 0.45
else:
    margem = 0.35
preco_venda =preco_custo * (1+margem)
print("O preço de venda do produto é:R$",preco_venda)