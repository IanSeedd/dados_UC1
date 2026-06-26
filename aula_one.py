# --------- Media very simples ---------
# print("Bem-vindo ao sistema de média!")
# nome = input("Digite o nome do aluno: ")
# nota = float(input("Digite a sua primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# media = (nota + nota2) / 2
# if media >= 7:
#     print(f"Passou {nome}! Sua media foi: {media}")
# else:
#     print(f"Recuperação {nome}! Sua media foi: {media}")

# --------- Calculadora automática ---------
while True:
    num = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    # Pequeno update:
    op = input("Escolha sua operação(+, -, x, /, //, %): ")
    if op == "+":
        print(num + num2)
    elif op == "-":
        print(num - num2)
    elif op == "x":
        print(num * num2)
    elif op == "/":
        print(num / num2)
    elif op == "//":
        print(num // num2)
    elif op == "%":
        print(num % num2)
    else:
        print("Hello World KKKKKKKK")
    continuar = input("Deseja continuar(S/N): ")
    if continuar.lower() == "n":
        break
# Versão automática
# print(f"Soma: {num + num2} \nSubtração: {num - num2} \nMultiplicação: {num * num2} \nDivisão: {num / num2} \nMódulo: {num % num2}")

# --------- Conversor de temperatura Denovo Bem Simples e Versão de update ---------
tipo = input("Qual medida você usara(C, F, K): ")
temp = float(input("Digite a temperatura: "))

if tipo.lower() == "c":
    conver = input("Qual conversão(F, K):")
    if conver.lower() == "f":
        print(((temp * 9/5) + 32), "graus")
    elif conver.lower() == "k":
        print((temp + 273.15), "graus")

elif tipo.lower() == "f":
    conver = input("Qual conversão(C, K):")
    if conver.lower() == "f":
        print(((temp - 32) * (5/9)), "graus")
    elif conver.lower() == "k":
        print(((temp - 32) * (5/9) + 273.15), "graus")

elif tipo.lower() == "k":
    conver = input("Qual conversão(C, F):")
    if conver.lower() == "f":
        print(((temp - 273.15) * 9/5 + 32), "Kelvins")
    elif conver.lower() == "k":
        print((temp - 273.15), "Kelvins")
# Versão easy:
# print(f"Temperatura em Fahrenheit = {(temp * 9/5) + 32} \n Temperatura em Kelvin = {temp + 273.15}")

# --------- Calculadora de Troco ---------
dinheiro_client = float(input("Dinheiro do cliente: ")) # float por causa dos centavos
produto = 67.90
if dinheiro_client <= produto:
    print("Ta de brincadeira mano?")
print(f"O troco deve ser {(dinheiro_client - produto):.2f}")

# --------- Conta de Luz Very Easy ---------
consumo = float(input("Digite o consumo em kWh: "))
tarifa = float(input("Digite a tarifa por kWh: "))
pagamento = consumo * tarifa
print(pagamento)