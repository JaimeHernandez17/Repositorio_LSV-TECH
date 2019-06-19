#frase = input("Ingrese frase: ")

frase = "A la gorda drogal"
frase_v = (frase.lower()).split(" ")
copia_frase = ""

for i in range(len(frase_v)):
    copia_frase+=frase_v[i]

frase_reves = frase[::-1]
frase_reves_v = (frase_reves.lower()).split(" ")
copia_frase_reves = ""

for i in range(len(frase_reves_v)):
    copia_frase_reves+=frase_reves_v[i]

i = 0
j = 0
cont = 0
while i < (len(copia_frase)):
    if copia_frase[i] != copia_frase_reves[j]:
        if i == 0 and j == 0:
            i = i+1
        i = i + 1
        j = j + 1
    else:
        i = i+1
        j=j+1
        cont=cont+1

prom = round((cont/len(copia_frase))*100)
if copia_frase == copia_frase_reves:
    print("La palabra es un palindromo")
elif prom >= 80:
    print("La palabra es casi palindromo, tiene un parecido al revés del: ",prom,"%")
else:
    print("La palabra no es un palindromo")



