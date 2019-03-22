def Es_primo(num):
    if num == 2:
        True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


cont = 0
i = 2
while True:

    if Es_primo(i):
        cont += 1

    if cont == 10001:
        print(i)
        break
    i += 1

