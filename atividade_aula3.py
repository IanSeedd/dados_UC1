# ----------------- Sistema de medias:
# print("Faça seu cadastro de aluno para saber sua media atual: ")
# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# n1 = float(input("Digite sua primeira nota: "))
# n2 = float(input("Digite sua segunda nota: "))
# media = (n1 + n2)/2
# if media >= 7:
#     print(f"Nome: {nome} | Idade: {idade} anos | Média: {media} | Situação: Aprovado")
# elif media >= 5:
#     print(f"Nome: {nome} | Idade: {idade} anos | Média: {media} | Situação: Recuperação")
# else:
#     print(f"Nome: {nome} | Idade: {idade} anos | Média: {media} | Situação: Reprovado")

# ----------------- Prateleira de mercado:
arroz = 29.90
feijao = 8.50
macarrao = 4.30
m_tomate = 3.70
oleo_soja = 8.90
conta = 0
# Poderia ter usado o .lower() mas preguiça, o if é apenas para não repetir o match e ficar confuso
if int(input(f"Deseja comprar Arroz 5kg por R${arroz}(1. Sim/2. Não)?")) == 1:
    conta += arroz
if int(input(f"Deseja comprar Feijão 1kg por R${feijao}(1. Sim/2. Não)?")) == 1:
    conta += feijao
if int(input(f"Deseja comprar Macarrão 500g por R${macarrao}(1. Sim/2. Não)?")) == 1:
    conta += macarrao
if int(input(f"Deseja comprar Molho De Tomate por R${m_tomate}(1. Sim/2. Não)?")) == 1:
    conta += m_tomate
if int(input(f"Deseja comprar Óleo de Soja 900ml por R${oleo_soja}(1. Sim/2. Não)?")) == 1:
    conta += oleo_soja
print(f"Sua conta foi: R${conta} \nComo deseja pagar?: 1. Credito(Acréscimo de 10%) 2. Debito(Sem alteração) 3. Dinheiro(Desconto de 5%)")
match int(input("")):
    case 1:
        conta += conta*0.1
        print(f"Total a pagar: {conta:.2f}")
    case 2:
        print(f"Total a pagar: {conta:.2f}")
    case 3:
        conta -= conta*0.05
        print(f"Total a pagar: {conta:.2f}")
    case _:
        print("Inválido")

# ----------------- Calculadora de gorjeta:
nota = int(input("Em uma escala de 1 a 4 avalie o serviço: "))
valor_conta = 100
match nota:
    case 1:
        print(f"Obrigado pela avalição!\n Sua conta foi: R${valor_conta}")
    case 2:
        print(f"Obrigado pela avalição!\n Sua conta foi: R${valor_conta}, deseja adicionar uma gorgeta de 5%? Caso adicione o valor será: R${valor_conta+(valor_conta*0.05)}")
    case 3:
        print(f"Obrigado pela avalição!\n Sua conta foi: R${valor_conta}, deseja adicionar uma gorgeta de 10%? Caso adicione o valor será: R${valor_conta+(valor_conta*0.1)}")
    case 4:
        print(f"Obrigado pela avalição!\n Sua conta foi: R${valor_conta}, deseja adicionar uma gorgeta de 15%? Caso adicione o valor será: R${valor_conta+(valor_conta*0.15)}")
    case _:
        print("Nota inválida")

# ----------------- Calculadora de viagem:
print("Bem vindo ao trip planner! Por favor informe os dados da viagem.")
km = float(input("Digite a distância que vai ser percorrida: "))
consumo = int(input("Digite o consumo do seu veiculo(Km/L): "))
preco = float(input("Digite o preço do combustível: "))
litros = round(km/consumo, 2)
print(f"Litros necessários: {litros}L | Custo total da viagem: R${round(litros*preco, 2)}\nBoa viagem!")

# ----------------- Conversor de moedas:
real = float(input("Digite a quantia em real que você deseja converter: "))
moeda = int(input("Para qual moeda deseja converter(1. dolar, 2. euro, 3. Libra)?: "))
match moeda:
    case 1:
        print(f"Você receberá: ${round(real/5.20, 2)}")
    case 2:
        print(f"Você receberá: €{round(real/5.65, 2)}")
    case 3:
        print(f"Você receberá: £{round(real/6.60, 2)}")
    case _:
        print("Valor inválido")

# ----------------- Goku Lanches:
print("Bem vindo ao Goku Lanches!")
xburger = 18
xbacon = 22
fritas = 9
refri = 6
suco = 7
conta = 0
match int(input(f"Deseja adicionar x-burger por R${xburger}(1. Sim/2. Não)?")):
    case 1: conta += xburger
match int(input(f"Deseja adicionar x-bacon por R${xbacon}(1. Sim/2. Não)?")):
    case 1: conta += xbacon
match int(input(f"Deseja adicionar fritas por R${fritas}(1. Sim/2. Não)?")):
    case 1: conta += fritas
match int(input(f"Deseja adicionar refrigerante por R${refri}(1. Sim/2. Não)?")):
    case 1: conta += refri
match int(input(f"Deseja adicionar suco por R${suco}(1. Sim/2. Não)?")):
    case 1: conta += suco
if conta > 40:
    conta = conta-(conta*0.1)
    print(f"Parabéns você teve 10% de desconto! \nSua conta com desconto foi: R${conta}")
else:
    print(f"Você deve pagar: {conta}")

