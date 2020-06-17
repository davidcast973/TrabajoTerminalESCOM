import pickle

a= [[x for x in range(0,1000,1)],[x for x in range(0,1000,2)],[x for x in range(0,1000,3)],]
b= {1:'Uno', 2:'Dos', 3:'Tres', 4:'Cuatro', 5:'Cinco', }

# Serializar archivo
archivo= open('Ejemplo.txt','wb')   # Escribir archivo binario
pickle.dump(a, archivo)         # Serializar variable en el archivo
archivo.close()                 # Cerrar archivo, si no, no lo guarda

# Deserializar archivo
archivo= open('Ejemplo.txt','rb')   # Leer archivo binario
variable= pickle.load(archivo)  # Poner el contenido del archivo deserializado en 'variable'
archivo.close()                 # Cerrar archivo, si no, no lo guarda