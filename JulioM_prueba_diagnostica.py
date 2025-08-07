############## codigo 1
##lista = (3, 5, 7, 9, 11)
##total = 0
##for numero in lista:
##   total += numero
##print("el resultado es", total)

############## codigo 2
##numero = int(input("ingresa un numero: "))
##if numero % 2 ==0:
##    print("es par")
##else:
##    print("no es par")

############## codigo 3
##numero = int(input("ingresa un numero:"))
##for i in range(1,11):
##    resultado = numero * i
##    print(f"{numero} x {i}= {resultado}")

############## codigo 4
##lista = (4, 6, 8, 10, 12)
##total = sum(lista)
##cantidad = len(lista)
##promedio = total / cantidad
##print("el promedio de la lista es en total:",promedio)

############## codigo 5
##c = input("ignresa una palabra:")
##contador = 0
##for i in c:
##     if i in "aeiouAEIOU":
##         contador += 1
##print(f"Las vocales de su palabra son: {contador}")

############## codigo 6
##cadena= input("ingresa una cadena: ")
##cadena_invertida = ""
##
##for caracter in cadena:
##    cadena_invertida = caracter + cadena_invertida
##
##print("la cadena invertida es:", cadena_invertida)
##
####cadena = input("ingresa una cadena: ")
####cadena_invertida = cadena[::-1]
####print("la cadena invertida es:", cadena_invertida)
##al momento de confirmar si tenia algun error en el codigo chatgpt me mostro esa manera mas compacta
############## codigo 7
##lista=[i for i in range (0,51)]
##print(lista)
##
##contador = 0
##
##for numero in lista:
##    if numero % 2 == 0:
##        contador += 1
##print("la cantidad de numeros pares es:", contador)

############## codigo 8
##num1 = float(input("ingresa un numero: "))
##num2 = float(input("ingresa un numero: "))
##num3 = float(input("ingresa un numero: "))
##
##mayor = max(num1, num2, num3)
##print("El numero mayor es:",mayor)

############## codigo 9
##numero = int(input("ingresa un numero: "))
##numero = abs(numero)
##suma = 0
##for digito in str(numero):
##    suma +=int(digito)
##print("la suma de los digitos es;",suma)
############## codigo 10
##frase = input("Ingresa una frase: ")
##
##contador_espacios = 0
##for caracter in frase:
##    if caracter == " ":
##        contador_espacios += 1
##total_palabras = contador_espacios + 1
##print(f"El número total de palabras en tu frase es: {total_palabras}")

############## codigo 11
##lista_invertida = list(range(10, 0, -1))
##print(lista_invertida)

############## codigo 12
##import random
##
##lista = [random.randint(1, 20) for _ in range(5)]
##print(lista)

############## codigo 13
##import random
##
##numero_secreto = random.randint(1, 10)
##intentos = 0
##
##while True:
##    intento = int(input("Adivina el número (entre 1 y 10): "))
##    intentos += 1
##
##    if intento == numero_secreto:
##        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
##        break
##    elif intento < numero_secreto:
##        print("El número es mayor.")
##    else:
##        print("El número es menor.")
##
############## codigo 14
##multiplos_de_3 = [i for i in range(1, 31) if i % 3 == 0]
##print(multiplos_de_3)
##


