a, b, c = [float(x) for x in input().split()]

triangulo = (a * c) / 2
print("TRIANGULO:", '{:.3f}'.format(triangulo))

pi = 3.14159
ac = pi * (c**2)
print("CIRCULO:", '{:.3f}'.format(ac))

at = ((a+b)*c)/2
print("TRAPEZIO:", '{:.3f}'.format(at))

aq = b**2
print("QUADRADO:", '{:.3f}'.format(aq))

ar = a*b
print("RETANGULO:", '{:.3f}'.format(ar))
