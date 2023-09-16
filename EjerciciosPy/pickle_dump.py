#dump Almacenar datos en el archivo
import pickle

# tomar la entrada del usuario para tomar la cantidad de datos
number_of_data = int(input('Cantidad de datos a ingresar: '))
data = []

# tomar entrada de los datos
for i in range(number_of_data):
    raw = input('Enter data '+str(i)+' : ')
    data.append(raw)

# abrir un archivo, donde desea almacenar los datos.(wb) Write Binary
file = open('important', 'wb')

# volcar información a ese archivo
pickle.dump(data, file)

# cerrar el archivo
file.close()