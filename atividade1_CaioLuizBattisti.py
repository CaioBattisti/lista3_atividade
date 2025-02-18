#Escreva um programa que forneça um tipo de aplicação financeira adequada ao um investidor a partir de dois dados fornecidos:
#O grau de aceitação de risco e o valor a ser investido. O grau de aceitação de risco deve ser lido no teclado na forma BX(baixo valor) ou AL(auto valor) 
#se for fornecido algo diferente disso o programa deve mostrar uma mensagem indicando que foi fornecido dado invalido.
#Para o valor dever ser numero real.
#bx:
aceitacao_risco =input("Qual sua aceitação de risco? BX ou AL?").strip().lower()
if aceitacao_risco == "bx" or aceitacao_risco == "al":
    valor_investido =float(input("Quando voce quer depositar? "))
    if aceitacao_risco == "bx":
        if valor_investido < 1000.00:
            print("voce deve abrir uma poupança.")
            print("CAIO LUIZ BATTISTI")
        else:
            print("voce deve abrir uma renda fixa.")
            print("CAIO LUIZ BATTISTI")
    elif aceitacao_risco == "al":
        if valor_investido < 1000.00:
            print("voce deve investir em bitcoin.")
            print("CAIO LUIZ BATTISTI")
        else:
            print("voce deve abrir uma ação.")
            print("CAIO LUIZ BATTISTI")
if aceitacao_risco != "bx" and aceitacao_risco != "al":
    print("Dado invalido, tente novamente!")
    print("CAIO LUIZ BATTISTI")