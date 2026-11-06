
print("=== CALCULADORA DE MÉDIA ESCOLAR ===")

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("\n=== RESULTADO ===")
print("Aluno:", nome)
print("Média:", media)

if media >= 6:
    print("Situação: Aprovado!")
else:
    print("Situação: Reprovado!")
