from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

ruta_imagenes = "mondea3d/"
archivos = sorted(glob.glob(os.path.join(ruta_imagenes, "*.png")))
#image=io.imread("prueba-069-20250708-164958")

print("Cantidad de imágenes encontradas:", len(archivos))
print("Primer archivo:", archivos[0] if archivos else "Ninguno")

imagenes=[]
# 4. lee cada archivo y guarda en la lista
for archivo in archivos:
    img = io.imread(archivo, as_gray=True)  # leo la imagen como escala de grises (solo intensidades)
    imagenes.append(img)

volumen = np.stack(imagenes, axis=0)  # apilo las imágenes en un nuevo eje, a lo largo
print("Dimensiones del volumen:", volumen.shape)

#hago los ejes xyz
Z, Y, X = np.indices(volumen.shape)
X = X.flatten()
Y = Y.flatten()
Z = Z.flatten()
C = volumen.flatten()  # intensidad de cada pixel


factor = 30 # toma 1 de cada 5 puntos para q no se me cuelgue
X = X[::factor]
Y = Y[::factor]
Z = Z[::factor]
C = C[::factor]
#uso librería matplotlib para grafico 
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c=C, cmap="viridis", marker="o", s=1) # scatter = diagrama de puntos


 #marco mis ejes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
