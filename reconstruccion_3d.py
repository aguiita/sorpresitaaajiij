import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import plotly.graph_objects as go

# Parámetros
longitud_onda = 650e-9  # en metros · luz roja led.

# Ruta donde están tus imágenes
ruta_imagenes = "mondea3d/"  # Cambiala si hace falta
imagenes = sorted(glob.glob(os.path.join(ruta_imagenes, "*.png")))

# Fases para cada imagen (ejemplo: 0, pi/8, 2pi/8, ...)
phis = np.array([i * np.pi / 8 for i in range(len(imagenes))])

# Cargar imágenes
imgs = []
for img_path in imagenes:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"No se pudo cargar {img_path}")
    else:
        print(f"Cargada {img_path} con shape {img.shape}")
        imgs.append(img.astype(np.float32))

if len(imgs) == 0:
    raise RuntimeError("No se cargó ninguna imagen válida.")

# Asegurar tamaños iguales
#alto_ref, ancho_ref = imgs[0].shape
#imgs_resized = []
#for im in imgs:
 #   if im.shape != (alto_ref, ancho_ref):
#        print(f"Redimensionando de {im.shape} a {(alto_ref, ancho_ref)}")
#        im_resized = cv2.resize(im, (ancho_ref, alto_ref))
 #       imgs_resized.append(im_resized)
  #  else:
   #     imgs_resized.append(im)

#convierte la lista a una matriz de tres dimensiones

#hace un array, como una lista con numeros que listan las fases

#Cada imagen es una matriz 2D de tamaño (alto, ancho)
imgs = np.array(imgs, dtype=np.float32)

# convierto esa lista de imágenes en un array de NumPy de 3 dimensiones
#  como si fuera un “cubo de datos”

#tomo el alto y ancho de las img, q es siempre el mismo en este caso
alto, ancho = imgs.shape[1], imgs.shape[2]

# Reconstrucción de fase
#Crea una "imagen vacía" (una matriz) donde 
# guardo la fase de cada píxel.
fase_reconstruida = np.zeros((alto, ancho), dtype=np.float32)

for y in range(alto):
    for x in range(ancho):
        I = imgs[:, y, x]
        A = np.vstack([np.cos(phis), np.sin(phis), np.ones_like(phis)]).T
        params, _, _, _ = np.linalg.lstsq(A, I, rcond=None)
        a, b, c = params
        varphi = np.arctan2(b, a)
        fase_reconstruida[y, x] = varphi
        #varphi es el valor de fase en ese pixel


# Fase a altura
altura = (fase_reconstruida * longitud_onda) / (4 * np.pi)

#use esta formula z = (ϕ · λ) / (4π)
# ϕ fase ,λ longitud de onda, z altura 

# Visualización 2D rápida
plt.imshow(altura, cmap='jet')
plt.colorbar(label='Altura relativa (m)')
plt.title('Mapa de altura reconstruida')
plt.show()

# Crear malla para gráfica 3D
x = np.linspace(0, 1, ancho)
y = np.linspace(0, 1, alto)
X, Y = np.meshgrid(x, y)

# Visualización  con Plotly
fig = go.Figure(data=[go.Surface(z=altura, x=X, y=Y)])
fig.update_layout(
    title='Reconstrucción 3D interactiva',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Altura'
    )
)

# Guardar el HTML antes de mostrar para poder abrirlo en google
output_file = "reconstruccion_3d.html"
fig.write_html(output_file)
print(f"Archivo {output_file} generado.")

# Mostrar en navegador
import webbrowser
import os
webbrowser.open("file://" + os.path.abspath(output_file))

# Mostrar en notebook / GUI
fig.show()
print("Gráfico mostrado.")
