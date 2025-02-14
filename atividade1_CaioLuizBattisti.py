#Escreva um programa que forneça um tipo de aplicação financeira adequada ao um investidor a partir de dois dados fornecidos:
#O grau de aceitação de risco e o valor a ser investido. O grau de aceitação de risco deve ser lido no teclado na forma BX ou AL 
#se for fornecido algo diferente disso o programa deve mostrar uma mensagem indicando que foi fornecido dado invalido.
#Para o valor dever ser numero real.
aceitacao_risco = input("qual sua aceitação de risco, BX ou AL? ")
if aceitacao_risco == "bx":
    renda =int(input("quando vc quer depositar? "))
    if renda < (1000.00):
        print("voce deve abrir uma poupança.")
if renda >= (1000.00):
    print("voce deve abrir uma renda fixa.")
elif aceitacao_risco == "al":
    renda2 =int(input("quanto vc quer depositar? "))
    if renda2 <(1000.00):
        print("voce deve investir em bitcoin. ")
    if renda2 >= (1000.00):
        print("voce deve abrir uma ação. ")
else:
    print("dado informado invalido!")