from skimage import io
#para leer imagenes

import numpy as np
#para trabajar con arreglos y matrices

import glob
import os
#para buscar archivos en carpetas

# Para gráficos
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  # para gráficos 3D

# carpeta donde estan las fots

ruta_imagenes= "mondea3d/"

#busco todos los png en la carpta y los ordeno
#igual ya son todos png
archivos=sorted(glob.glob(os.path.join(ruta_imagenes, "*.png")))
# os.path.join("mondea3d/", "*.png") en esa carpeta busca todo lo que termine en .png


#printeo la cantidad y el primero para probar
print("Cantidad de imágenes encontradas:", len(archivos))
print("Primer archivo:", archivos[0] if archivos else "Ninguno")

# ahora que encontre las imagenes, las voy a leer y guardar en una lista
imagenes=[]
for archivo in archivos:
    img=io.imread(archivo, as_gray=True)
    imagenes.append(img) #agrego la imagen a la lista

#printeo para ver que onda
#eso lo puedo sacar despues
    print(f"Imagen {archivo} leída con forma {img.shape} y tipo {img.dtype}")
   
  #imagenes es una lista de matrices 
  #Cada matriz es una “rebanada” del volumen.

#ahora la lista de matrices la hago 3d
#porque quiero tener un array 3d, una pila de mis matrices
#Eje Z, es el 0 = número de imágenes
#Eje Y , es el 1 = altura de la imagen
#Eje X , es el 2 = ancho de la imagen
volumen = np.stack(imagenes, axis=0)
#axis 0 porque quiero apilar a lo largo del primer eje (el z)
# lo convierto en un bloque continuo de datos en memoria
#el npstack lo que hace es tomar cada matriz de la lista y las apila en un nuevo eje
#osea si tengo 100 imagenes de 200x200, me queda un array de 100x200x200
print("Dimensiones del volumen:", volumen.shape)