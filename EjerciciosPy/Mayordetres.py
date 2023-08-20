a = 1
b = 0
c=2

a = int(input("Ingresa un numero natural:"))
b = int(input("Ingresa otro:"))
c = int(input("Ingresa otro mas:"))

print(f"Los numeros ingresados son: {a}, {b} y {c}")

if (a > b)and(a > c):
    print("El Primer numero es mayor")
elif (b > a)and(b > c): 
    print("El segundo numero es mayor")
elif (c > a)and(c > b): 
    print("El tercer numero es mayor")
else:
    print("Los numeros son iguales")