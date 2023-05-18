def imc(a, b):
    imc = a/b**2
    print(f"Seu IMC é: {imc:.2f} Kg/m²")
    
def despedida():
    print("Obrigado por utilizar a calculadora.\nAté mais!")

while True:
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc(peso, altura)
    opc = input("Deseja calcular novamente [S/N]: ")
    if opc in "Nn": break

despedida()
input()