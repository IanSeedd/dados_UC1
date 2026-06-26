# --------- Ordem Crescente bem deselegante mas serve ---------
num = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))
num3 = int(input("Digite mais um número: "))
# Se o número 1 for maior
if num > num2 and num > num3:
    print(num)
    if num2 > num3:
        print(num2)
        print(num3)
    elif num3 > num2:
        print(num3)
        print(num2)
# Se o número 2 for maior
elif num2 > num and num2 > num3:
    print(num2)
    if num > num3:
        print(num)
        print(num3)
    elif num3 > num:
        print(num3)
        print(num)
# Se o número 3 for maior
elif num3 > num and num3 > num2:
    print(num3)
    if num > num2:
        print(num)
        print(num2)
    elif num2 > num:
        print(num2)
        print(num)

# --------- Media EZZZZZZZZZ ---------
print("Bem-vindo ao sistema de média!")
nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota + nota2 + nota3 + nota4) / 4
if media >= 7:
    print(f"Passou {nome}! Sua media foi: {media}")
elif media >= 5:
    print(f"Recuperação {nome}! Sua media foi: {media}")
else:
    print(f"Reprovado {nome}! Sua media foi: {media}")

# --------- Temperatura EZZZZZZZZZ ---------
temp = float(input("Digite a temperatura: "))
if temp > 25:
    print("TA QUENTE DEMAIS KKKKKK")
elif temp >= 15:
    print("Que clima agradável")
else:
    print("Ta nevando ou ta frio pra caramba")

# --------- Login EZZZZZZZZZ ---------
user = "Pomothobic"
senha = "1234"
user_log = input("Nome de usuário: ")
user_senha = input("Senha de usuário: ")
if user_log == user and user_senha == senha:
    print(f"{user} Bem vindo!")
else:
    print("Acesso negado!")

# --------- Desconto EZZZZZZZZZ ---------
valor = float(input("Digite o valor total da compra: "))
if valor >= 200:
    desconto = 0.1
    valor_final = valor - (valor*desconto)
    print(f"Total a pagar com 10% de desconto: {valor_final}")
if valor >= 100:
    desconto = 0.05
    valor_final = valor - (valor*desconto)
    print(f"Total a pagar com 5% de desconto: {valor_final}")
else:
    print(f"Total a pagar: {valor}")

# --------- Par ou impar ou negativo EZZZZZZZZZ ---------
num = int(input("Digite um número: "))
if num > 0:
    if num%2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é impar")
if num < 0:
    if num%2 == 0:
        print(f"{num} é par e negativo")
    else:
        print(f"{num} é impar e negativo")
else:
    print("Digitou 0")
