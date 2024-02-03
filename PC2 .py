#'''PRACTICA CALIFICADA 2'''
##Estructuras Iterativas: 
## Problema 1:

minimo = 1500 #numero minimo 
print("Los números divisibles por 7 y múltiplos de 5 en el rango de 1500 y 2700 son:")
while minimo <=  2700: #numero maximo:
    if minimo % 7 == 0 and minimo % 5 == 0:
        print(minimo)
    minimo += 1

## problema 2

h = 5 

for i in range(1, h+1): #linea de forma acendente
    print('* '*(i))

for i in range (h-1,0,-1): #linea de forma decendente
    print('* '*(i))
    
## problemo 3

Lista_numeros = []
num_pares = 0
num_impares = 0

while True:
    respuesta = input('¿Desea ingresar numero? (SI/NO): ')
    
    if respuesta == "SI":
        num = int(input('insertar numero : '))
        Lista_numeros.append(num)
        
        if num % 2 == 0:
            num_pares += 1
        else:
            num_impares += 1
    elif respuesta == "NO":
        break

print("Los numeros ingresados son:", Lista_numeros)
print("Cantidad de numeros pares:", num_pares)
print("Cantidad de numeros impares:", num_impares)

## problema 4

lista_alumnos = [{'nombre':'Juna','nota':[10,12,15]},{'nombre':'Sandra','nota':[15,18,20]},{'nombre':'Lisa','nota':[15,20,11]}]

for elemento in lista_alumnos:
    for llave,valor in elemento.items():
        print(f'{llave}: {valor}')
        
##Funciones:
## poblema 5

def numero_digitos(numero, digito):
    contador = 0
    for cifra in str(numero):
        if cifra == str(digito):
            contador += 1
    return contador

numero = input(" ingrese el siguiente numero: ")
digito = 0

cantidad = numero_digitos(numero, digito)
print(f"El numero ingresado es {numero} y dijito: {digito}")
print(f"Cantidad de veces {digito} en el número: {cantidad}")

## problema 6

def fibonacci(x):
    fib = [0 , 1]
    while fib[-1] < x:
        fib.append(fib[-1] + fib[-2])
    return fib[:-1]

secuencia = fibonacci(50)
print(secuencia)

## problema 7

def num_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Ingrese número: "))
if num_primo(num):
    print(num, "es numero es primo")
else:
    print(num, "el numero no es primo")
    
    
## problema 8

def calcular_factorial(numero):
    if numero < 0:
        return "El número debe ser un entero no negativo"
    elif numero == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial

# introducir el numero
numero = int(input('ingresar el numero:'))
factorial = calcular_factorial(numero)
print(f"El factorial de {numero} es: {factorial}")


##metodo cadena:
## problema 9

def omitir(cadena_texto):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    cadena_sin_vocal = ''
    for letra in cadena_texto:
        if letra not in vocales:
            cadena_sin_vocal += letra
    return cadena_sin_vocal

texto = input("Ingrese una cadena de texto: ")
sin_vocales = omitir(texto)
print("Texto sin vocales:", sin_vocales)


## problema 10






