#load leer datos del archivo
import pickle

# abrir el archivo, donde se almacenaron los datos. (rb) read-binary
file = open('important', 'rb')

# leer la informacion de ese archivo
data = pickle.load(file)

# cerrar el archivo
file.close()

#mostrar en pantalla los datos
print('Showing the pickled data:')

cnt = 0
for item in data:
    print('The data ', cnt, ' is : ', item)
    cnt += 1