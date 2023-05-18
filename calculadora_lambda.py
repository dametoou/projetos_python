soma = lambda a,b: a+b
sub = lambda a,b: a-b
mult = lambda a,b: a*b
div = lambda a,b: a/b

menu = ["Soma", "Subtração", "Multiplicação", "Divisão", "Sair"]

while True:
    print("Calculadora Lambda")
    for n, item in enumerate(menu):
        print(f"[{n+1}] - {item}")
    opc = int(input("Opção escolhida: "))
    
    if opc == 5: break
    else:
        n1 = int(input("1º número: "))
        n2 = int(input("2º número: "))
        if opc == 1: print(f"{n1}+{n2} = {soma(n1, n2)}")
        if opc == 2: print(f"{n1}-{n2} = {sub(n1, n2)}")
        if opc == 3: print(f"{n1}*{n2} = {mult(n1, n2)}")
        if opc == 4: print(f"{n1}/{n2} = {div(n1, n2)}")
        
print("Obrigado por utilizar a Calculadora Lambda!")