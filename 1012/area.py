# Como era pra ser feito:
valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

tri = (A * C) / 2  # Formula da are do triangulo
cir = (3.14159 * C**2)  # Formula da area do circulo
tra = ((A + B) * C) / 2  # Formula da area do trapezio
qua = B**2
ret = A * B

print('TRIANGULO: {:.3f}' .format(tri))
print('CIRCULO: {:.3f}' .format(cir))
print('TRAPEZIO: {:.3f}' .format(tra))
print('QUADRADO {:.3f}' .format(qua))
print('RETANGULO {:.3f}' .format(ret))
