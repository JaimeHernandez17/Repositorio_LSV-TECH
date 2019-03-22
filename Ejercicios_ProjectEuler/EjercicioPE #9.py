#Hallar un triplete pitagorico(abc) para el que a+b+c = 1000

for a in range(1,501):
    for b in range(a,501):
        for c in range(b,501):
            if a**2+b**2 == c**2 and c**2 == a**2+b**2 and a+b+c == 1000:
                print(a,"² + ",b,"² = ",a**2+b**2)
                print(c,"² = ",c**2)
                print(a,"+",b,"+",c," = ",a+b+c)
                exit()