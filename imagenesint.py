import numpy as np
import matplotlib.pyplot as plt
import cv2

# Crear un interferograma sintético con franjas horizontales
def generar_interferograma(frecuencia=10, tamaño=(256, 256)):
    y = np.linspace(0, 2 * np.pi * frecuencia, tamaño[0])
    x = np.linspace(0, 2 * np.pi * frecuencia, tamaño[1])
    X, Y = np.meshgrid(x, y)
    interferograma = 127.5 + 127.5 * np.cos(X)  # Rango 0-255
    return interferograma.astype(np.uint8)

imagen = generar_interferograma()

# Guardarla si querés usarla con el código anterior
cv2.imwrite("interferograma.png", imagen)

# Mostrarla
plt.imshow(imagen, cmap='gray')
plt.title("Interferograma Sintético")
plt.axis('off')
plt.show()
