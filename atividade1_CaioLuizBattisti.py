#Escreva um programa que forneça um tipo de aplicação financeira adequada ao um investidor a partir de dois dados fornecidos:
#O grau de aceitação de risco e o valor a ser investido. O grau de aceitação de risco deve ser lido no teclado na forma BX ou AL 
#se for fornecido algo diferente disso o programa deve mostrar uma mensagem indicando que foi fornecido dado invalido.
#Para o valor dever ser numero real.
aceitacao_risco = input("qual sua aceitação de risco, BX ou AL? ")
if aceitacao_risco == "bx":
    investir = input("quando deseja investir? ")
elif investir < 100:
    print("voce deve abrir uma poupança.")
