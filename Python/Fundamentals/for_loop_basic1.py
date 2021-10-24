# 1 Básico
for i in range(0,151):
    print(i)

#Multiplos de 5
for i in range(0,1001,5):
    print(i)

#Contar, Dojo way
for i in range(0,101):
    if i%10==0:
        print('Coding Dojo')
    elif i%5 ==0:
        print('Coding')
    else:
        print(i)

#¡Uf, eso es bastante grande!
suma_impares=0
for i in range(0,500001):
    if i%2!=0:
        suma_impares+=i
print(suma_impares)

#Cuenta regresiva por 4
for i in range(2018,-1,-4):
    print(i)

#Contador flexible
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,highNum+1):
    if i%mult==0:
        print(i)

# Numeros primos
for i in range(1,1001):
    if (i%2 != 0 and i%3 !=0 and i%5!=0 and i%7!=0)or(i==2 or i==3 or i==5 or i==7):
        print(f'{i} es un número primo')
    