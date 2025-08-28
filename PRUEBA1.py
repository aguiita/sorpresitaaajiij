import numpy as np
import cv2
import matplotlib.pyplot as plt

# Dimensiones de la imagen simulada
alto = 150
ancho = 400

# 1. Creamos una imagen negra
imagen = np.zeros((alto, ancho), dtype=np.uint8)

# 2. Generamos un perfil suave: seno + ruido
x = np.linspace(0, 4 * np.pi, ancho)
perfil = 75 + 10 * np.sin(x)          # perfil base
perfil += 3 * np.random.randn(ancho)  # ruido gaussiano

# 3. Suavizamos el perfil para evitar puntos aislados
perfil = cv2.GaussianBlur(perfil.astype(np.float32), (11, 1), 0).flatten()

# 4. Dibujamos la línea continua con cierto grosor
grosor = 3  # píxeles arriba y abajo
for i in range(ancho):
    y = int(np.clip(perfil[i], 0, alto - 1))
    imagen[max(y-grosor,0):min(y+grosor+1, alto), i] = 255

# 5. Añadimos unas líneas horizontales aleatorias tipo artefacto
for y_line in [20, 60, 100]:
    nivel = np.random.randint(180, 220)
    imagen[y_line-1:y_line+2, :] = nivel

# 6. Aplicamos un desenfoque suave para realismo
imagen = cv2.GaussianBlur(imagen, (5, 5), 0)
# ... tu código hasta el paso 6

imagen = cv2.GaussianBlur(imagen, (5, 5), 0)

def crear_matriz(frecuencia=0.1, amplitud=20, fase=0, ancho=400, alto=150):
    x = np.linspace(0, 4 * np.pi, ancho)
    y = alto // 2 + amplitud * np.sin(2 * np.pi * frecuencia * x + fase)
    matriz = np.zeros((alto, ancho), dtype=np.uint8)
    for i in range(ancho):
        pos = int(np.clip(y[i], 0, alto - 1))
        matriz[pos-2:pos+3, i] = 255
    matriz = cv2.GaussianBlur(matriz, (5,5), 0)
    return matriz

for i in range(5):
    fase = i * np.pi / 8
    matriz = crear_matriz(frecuencia=0.1, amplitud=20, fase=fase)
    plt.imshow(matriz, cmap='gray')
    plt.title(f"Onda fase {fase:.2f}")
    plt.savefig(f"interferometro_fase_{i}.png")
    plt.show()

cv2.imwrite("interferograma_simulado_continuo.png", imagen)
