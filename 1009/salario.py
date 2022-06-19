nome = input()
salario_fixo = float(input())
qtde_vendas = float(input())

bonus = float(qtde_vendas * (15 / 100))

total = salario_fixo + bonus

print("TOTAL = R$ %0.2f" % total)
