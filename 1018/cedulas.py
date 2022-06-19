# ler um valor inteiro
# calcular o menor numero de notas no qual o valor pode ser decomposto
# imprimir o resultado

notas001 = int(input())

print(notas001)

notas100 = notas001 // 100
notas001 = notas001 % 100

notas50 = notas001 // 50
notas001 = notas001 % 50

notas20 = notas001 // 20
notas001 = notas001 % 20

notas10 = notas001 // 10
notas001 = notas001 % 10

notas05 = notas001 // 5
notas001 = notas001 % 5

notas02 = notas001 // 2
notas001 = notas001 % 2

print(f"{notas100} notas(s) de R$ 100,00")
print(f"{notas50} notas(s) de R$ 50,00")
print(f"{notas20} notas(s) de R$ 20,00")
print(f"{notas10} notas(s) de R$ 10,00")
print(f"{notas05} notas(s) de R$ 5,00")
print(f"{notas02} notas(s) de R$ 2,00")
print(f"{notas001} notas(s) de R$ 1,00")
