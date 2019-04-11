#Find the sum of all multiples of three or five below one thousand   

#The variable "sum" is to store all prime numbers.
sum = 0

#
for i in range(3,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum+i

print(sum)
