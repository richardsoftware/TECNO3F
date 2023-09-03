#ARRAY
import numpy as np
a= np.array([2,3,4])
b= np.array([[2,5,1],[5,6,3],[8,9,2]])
print(a)
print (b)
print("numero de elementos en a: ", a.size)
print("numero de elementos en b: ", b.size)
TempC=[12.5,3.4,3.6,6.4,6.5,8.3]

arregloTemp= np.array(TempC)
print("Temperaturas en C")
print(arregloTemp)
print("Temperaturas en Kelvin")
print(arregloTemp+273.15)

t= np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])

for i in range (0,12):
    print("Valor anterior: ", t[i+1])
    t[i+1]= t[i+1]*2
    print("Valor actual: ", t[i+1])

A= np.array([[1,1],[0,1]])

for j in range (0,2):
    A[1][j]= A[1][j]*2

print (A)
