
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def Multiplicar(a, b):
    return a * b

def Dividir(a, b):
    return a / b

print("Calculadora")
print("1. Sumar")
print("2. Resta")
print("3. Multiplicacion")
print("4. Dividir")
print("5. Salir")

eleccion = (int(input("Elija una opcion: ")))
num1 = float(input("ingresa el primer numero: "))
num2 = float(input("ingresa el segundo numero: "))

if eleccion == 1:
    print(num1, "+", num2, "=",sumar(num1, num2))
          
    
elif eleccion == 2:
    print(num1, "-", num2, "=",restar(num1, num2))

elif eleccion == 3:
    print(num1, "*", num2, "=",Multiplicar(num1, num2))

elif eleccion == 4:
    print(num1, "/", num2, "=",Dividir(num1, num2))


else:
    print("Opcion no valida")