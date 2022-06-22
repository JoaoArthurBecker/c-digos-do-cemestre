numeros = [
    1, 2, 7
]

for numero in numeros:
    is_primo=True
    if (numero==0 or numero ==1):
        is_primo=False
    else:
        for temp_numero in range (  2, numero):
            print ("número:", numero, temp_numero)
            if (numero%temp_numero==0):
                is_primo=False
    print (numero,is_primo)