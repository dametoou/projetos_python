import os

# Solicitando informções para o usuário em loop.
escolha = 0
while escolha != 4:
    os.system('cls') # Limpar a tela do programa quando iniciado ou reiniciado.
    print("Calculadora conversora de decimal para bases (binário, octal, hexadecimal)\n")
    print("Escolha uma opção:")
    print("1 - Binário")
    print("2 - Octal")
    print("3 - Hexadecimal")
    print("4 - Sair\n")
    escolha = int(input("Opção escolhida: ")) # Escolhendo as opções disponíveis.

# Convertendo o número decimal para binário.
    if escolha == 1:
        decimal = int(input("Digite um número decimal: ")) # Digitando o número que será convertido.
        num_decimal = decimal
        conv = ''
        digito = '01'
        while decimal > 0:
            conv = str(digito[decimal % 2]) + conv
            decimal = decimal // 2
        print(f"\nDecimal para Binário:\nDecimal: {num_decimal}\nBinário: {conv}")
        input("Aperte qualquer tecla para continuar...") # Reinciar o programa.

# Convertendo o número decimal para octal.
    elif escolha == 2:
        decimal = int(input("Digite um número decimal: ")) # Digitando o número que será convertido.
        num_decimal = decimal
        conv = ''
        digito = '01234567'
        while decimal > 0:
            conv = str(digito[decimal % 8]) + conv
            decimal = decimal // 8
        print(f"\nDecimal para Octal:\nDecimal: {num_decimal}\nOctal: {conv}")
        input("Aperte qualquer tecla para continuar...") # Reinciar o programa.

# Convertendo o número decimal para hexadecimal.
    elif escolha == 3:
        decimal = int(input("Digite um número decimal: ")) # Digitando o número que será convertido.
        num_decimal = decimal
        conv = ''
        digito = '0123456789ABCDEF'
        while decimal > 0:
            conv = str(digito[decimal % 16]) + conv
            decimal = decimal // 16
        print(f"\nDecimal para Hexadecimal:\nDecimal: {num_decimal}\nHexadecimal: {conv}")
        input("Aperte qualquer tecla para continuar...") # Reinciar o programa.

# Saindo do programa e exibindo as informações do projeto.
    elif escolha == 4:
        break

    else:
        print("Opção inválida!")
        input("Aperte qualquer tecla para continuar...") # Reinciar o programa.

# Informações sobre o projeto (exibe somente após sair do programa).
print("\nObrigado por utilizar nossa calculadora de conversão!\n")
print("Curso: Análise e Desenvolvimento de Sistemas\n")
print("Componentes do grupo: \n- Beatriz Santos Loçaes (33420947)\n- Rafael Costa da Silva (33616019)\n- Ryan da Costa Ferreira (33539227)\n- Thiago Silva Dameto (33351821)\n")
print("Disciplinas envolvidas: Programação de Computadores\n")
print("Versão do aplicativo: Visual Studio Code 1.76.0\n")
input()