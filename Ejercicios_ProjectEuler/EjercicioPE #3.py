num = 600851475143
factores = []
for i in range(2,num+1):
    if num / i == 1:
        factores.append(i)
        break
    if num % i == 0:
        num = num / i
        factores.append(i)


print(max(factores))