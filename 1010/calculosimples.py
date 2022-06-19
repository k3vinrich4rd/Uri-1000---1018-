Kevin = input().split()
c1 = int(Kevin[0])
n1 = int(Kevin[1])
v1 = float(Kevin[2])
total1 = n1*v1

Richard = input().split()
c2 = int(Richard[0])
n2 = int(Richard[1])
v2 = float(Richard[2])
total2 = n2*v2

total_das_somas = total1+total2
print("VALOR A PAGAR: R$ {:.2f}".format(total_das_somas))
        