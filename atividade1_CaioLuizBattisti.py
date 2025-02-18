#Escreva um programa que forneça um tipo de aplicação financeira adequada ao um investidor a partir de dois dados fornecidos:
#O grau de aceitação de risco e o valor a ser investido. O grau de aceitação de risco deve ser lido no teclado na forma BX(baixo valor) ou AL(auto valor) 
#se for fornecido algo diferente disso o programa deve mostrar uma mensagem indicando que foi fornecido dado invalido.
#Para o valor dever ser numero real.
#bx:
bxrenda =float(input("Quanto voce quer depositar? "))
aceitacao_risco = input("qual sua aceitação de risco, BX ou AL? ").strip().lower()
if aceitacao_risco == "bx" and bxrenda < 1000.00:
    print("voce deve abrir uma poupança.")
if bxrenda > 1000.00:
    print("voce deve abrir uma renda fixa.")
#al:    
if aceitacao_risco == "al":
    alrenda =float(input("Quanto voce quer depositar? "))
    if alrenda < 1000.00:
        print("voce deve investir em bitcoin.")
    if alrenda > 1000.00:
        print("voce deve abrir uma ação")
    else:
        print("dado invalido, tente novamente.")