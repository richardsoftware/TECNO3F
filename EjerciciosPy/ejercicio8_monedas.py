#calcular Cambio de Monedas
print("Calcular Cambio de moneda. Pesos a Dolares")
pesos = float(input("Ingrese Cantidad de Pesos a convertir: "))
dolar_hoy = float(input("Ingrese Valor del Dolar Hoy: "))

cambio = (pesos / dolar_hoy)

print(f"Tenes {cambio} U$S")