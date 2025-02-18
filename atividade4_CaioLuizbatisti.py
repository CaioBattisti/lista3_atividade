#No Senailandia mulheres e homens  podem servir o exercito do país.
#O cerviço e opcional e é muito comum que as pessoas se apresentem para o cerviço em algum momento da vida.
#Existe uma única restrição para o ingresso que e a idade da pessoa: 
#A. para mulheres a idade aceita e entre 21 e 34 anos.
#B. para homens a idade aceita e entre 18 e 39 anos.
#Escreva um programa que leia 3 dados de entrada: nome da pessoa, idade e sexo e informe se a pessoa será aceita ou não para o serviço.
#obs:para o sexo deve ser lido apenas um caractere que pode ser “F” ou “f” “m” ou “M” para masculino e feminino, qualquer coisa diferente deve ser informado
nome = input("digite o nome:")
idade =float(input("digite a idade:"))
genero = input("digite seu genero:")
if genero == ("M") or ("m") and idade >= 18 and idade < 39:
    print("voce pode servir.")
    print("CAIO LUIZ BATTISTI")
elif genero == ("F") or ("f") and idade >= 21 and idade < 34:
    print("voce pode servir.")
    print("CAIO LUIZ BATTISTI")
else:
    print("desculpe, voce nao pode servir.")
    print("CAIO LUIZ BATTISTI")