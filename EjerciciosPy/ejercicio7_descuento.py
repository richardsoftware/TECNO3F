#calcular descuento
print("Calcular descuento en tu compra")
subtotal = float(input("Ingrese el Total de la compra: "))
dto = float(input("Ingrese el porcentaje de descuento %: "))

descuento = (subtotal * dto)/100
total = subtotal - descuento

print(f"Total de la compra sin descuento: {subtotal}")
print(f"descuento {dto} %: {descuento}")
print(f"Total de la compra {total} Gracias")