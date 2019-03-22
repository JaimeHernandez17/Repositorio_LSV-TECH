val = 0
palindromos = []
for i in range(100,1000):
    for j in range(101,1000):
        val = i * j
        if str(val) == str(val)[::-1]:
            palindromos.append(val)

print(max(palindromos))
