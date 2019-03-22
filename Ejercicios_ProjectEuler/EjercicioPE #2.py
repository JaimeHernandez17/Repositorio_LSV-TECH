
a = 1
b = 2
sum = [1]
while b < 4000000:

    a,b = b, a+b
    sum.append(a)

sum2 = 0

for i in range(len(sum)):

    if sum[i] % 2 == 0:
        sum2 += sum[i]

print(sum)
print(sum2)