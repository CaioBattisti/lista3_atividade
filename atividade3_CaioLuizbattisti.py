#uma empresa financeira concebe empréstimos a pessoa física, quando o valor da parcela e menor que 8% do salário da pessoa.
#Escreva um programa que leia dois números reais.
#O valor do salario e o valor da parcela e informe se o empréstimo será concebido ou não
valor_salario =int(input("digite seu salario:"))
valor_parcela =int(input("digite sua parcela:"))
if valor_parcela < ((valor_salario * 0.08)):
    print("seu emprestimo sera consebido.")
else:
    print("seu emprestimo nao sera consebido.")