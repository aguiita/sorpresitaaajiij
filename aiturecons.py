import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

def cargar_imagen(ruta):
    if not os.path.isfile(ruta):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
    imagen = cv2.imread(ruta, cv2.IMREAD_COLOR)
    if imagen is None:
        raise ValueError(f"No se pudo cargar la imagen en {ruta}")
    return imagen

def convertir_a_grises(imagenes):
    """Convertir cada imagen a escala de grises."""
    return np.array([cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) for imagen in imagenes])

def redimensionar_volumen(volumen, nuevo_tamano):
    """Redimensionar cada capa del volumen."""
    return np.array([cv2.resize(slice_, nuevo_tamano[::-1], interpolation=cv2.INTER_LINEAR) for slice_ in volumen])

#rutas_imagenes = [
#    "C:/Users/usuario/letraM-001-20240806-164202.jpg",
#    "C:/Users/usuario/letraM-002-20240806-164202.jpg",
#    "C:/Users/usuario/letraM-003-20240806-164202.jpg",
#    "C:/Users/usuario/letraM-004-20240806-164202.jpg",
#    "C:/Users/usuario/letraM-005-20240806-164202.jpg"
#]

def obtener_rutas_imagenes(carpeta, extensiones=(".jpg", ".png", ".jpeg")):
    """Obtener todas las rutas de archivos de imagen en una carpeta."""
    rutas = [
        os.path.join(carpeta, archivo)
        for archivo in os.listdir(carpeta)
        if archivo.lower().endswith(extensiones)
    ]
    if not rutas:
        raise ValueError(f"No se encontraron imágenes con extensiones {extensiones} en la carpeta {carpeta}")
    return sorted(rutas)  # Ordenar para garantizar consistencia

# Ruta de la carpeta que contiene las imágenes
carpeta_imagenes = "C:/Users/usuario/OneDrive/Documentos/3d-reconstruction"

try:
    rutas_imagenes = obtener_rutas_imagenes(carpeta_imagenes)
    
    imagenes = [cargar_imagen(ruta) for ruta in rutas_imagenes]

    shape = imagenes[0].shape
    for img in imagenes[1:]:
        if img.shape != shape:
            raise ValueError(f"Las imágenes deben tener las mismas dimensiones. Dimensiones encontradas: {img.shape}")

    imagen_3d = np.stack(imagenes, axis=0)
    volumen = convertir_a_grises(imagen_3d)

    # Redimensionar el volumen para hacer el gráfico más manejable
    nuevo_tamano = (50, 50)  # Ajusta el tamaño según lo necesites
    volumen_redimensionado = redimensionar_volumen(volumen, nuevo_tamano)

    # Verificar dimensiones
    print(f"Dimensiones del volumen redimensionado: {volumen_redimensionado.shape}")

    # Crear coordenadas 3D
    x = np.linspace(0, volumen_redimensionado.shape[2] - 1, volumen_redimensionado.shape[2])
    y = np.linspace(0, volumen_redimensionado.shape[1] - 1, volumen_redimensionado.shape[1])
    z = np.arange(volumen_redimensionado.shape[0])

    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

    X = X.flatten()
    Y = Y.flatten()
    Z = Z.flatten()
    C = volumen_redimensionado.flatten()

    # Verificar tamaños de los datos
    print(f"Tamaño de X: {len(X)}")
    print(f"Tamaño de Y: {len(Y)}")
    print(f"Tamaño de Z: {len(Z)}")
    print(f"Tamaño de C: {len(C)}")

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Asegurarse de que los datos no sean demasiado grandes
    if len(X) > 1e6:
        print("Demasiados puntos para mostrar. Reduciendo la cantidad de puntos para visualización.")
        step = len(X) // int(1e6)
        X, Y, Z, C = X[::step], Y[::step], Z[::step], C[::step]

    img = ax.scatter(X, Y, Z, c=C, cmap='viridis', marker='o', s=1)
    fig.colorbar(img, ax=ax, shrink=0.5, aspect=5)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
    plt.show()

except Exception as e:
    print(f"Error: {e}")
