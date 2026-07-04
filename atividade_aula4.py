# Ez números:
# for i in range(1, 6):
#     x = int(input("Digite um número bro: "))
#     print(f"Dobro: {x*2} | Triplo: {x*3} | Quadruplo: {x*4}")

# Boas vindas
# nomes = ["Ichigo Kurosaki", "Izuku Midoriya", "Son Goku", "Tomura Shigaraki", "Yuji Itadori", "Rimuru Tempest", "Rudeus Greyrat", "Subaru Natsuki", "Naoya Zenin", "Maki Zenin", "Ochako Uraraka"]
# for nome in nomes:
#     print(f"Bem vindo(a), {nome}")

# Notas de estudantes
# for i in range(1, 11):
#     nome = input("Digite seu nome: ")
#     nota = float(input("Digite a primeira nota: "))
#     nota2 = float(input("Digite a segunda nota: "))
#     media = (nota + nota2) / 2
#     if media >= 7:
#         print(f"Parabéns {nome}, você foi aprovado! sua media foi: {media}")
#     elif media >=5:
#         print(f"{nome}, você ficou de recuperação. Sua media foi: {media}")
#     else:
#         print(f"Que infortunio, {nome} foi reprovado. Sua media foi: {media}")

# Cadastro: 
lista = []
# Anotação do futuro: O melhor jeito é usar mais de uma lista ai os index vão se alinhar logo é facil de printar também, então é só fazer uma lógca onde se a idade for menor que 18 ele cancela tudo antes do append
for i in range(1, 11):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu email: ")
    formacao = input("Digite sua formação: ")
    dado = f"Nome: {nome} | Idade: {idade} | Telefone = {telefone} | Email: {email} | Formação: {formacao}" # Cada dado em string 
    if idade >= 18:
        print("Seus dados foram adicionados")
        lista.append(dado)
    print("Candidato inválido, menor de 18")
for i in range(len(lista)):
    print(f"Candidato {i+1}: \n{lista[i]}")
# Eu corrigi já, ta no jupiter 
