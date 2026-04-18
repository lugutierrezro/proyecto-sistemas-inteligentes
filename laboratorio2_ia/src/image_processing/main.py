import cv2
import matplotlib.pyplot as plt
from image_processing.loader import load_image
from image_processing.transform import apply_grayscale, adjust_brightness

def main():
    ruta = 'data/ejemplo.jpg'
    imagen = load_image(ruta)
    
    if imagen is None:
        return

    # Convertir a RGB para mostrar con matplotlib
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    
    # Aplicar transformaciones
    gris = apply_grayscale(imagen)
    brillo = adjust_brightness(gris)

    # Mostrar resultados
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(imagen_rgb)
    plt.title("Imagen Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(gris, cmap='gray')
    plt.title("Imagen en Escala de Grises")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(brillo, cmap='gray')
    plt.title("Imagen con Brillo Ajustado")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
