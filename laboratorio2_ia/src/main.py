import cv2
import matplotlib.pyplot as plt
import os


def main():
    ruta = 'data/ejemplo.jpg'

    if not os.path.exists(ruta):
        print("No hay imagen")
        return

    imagen = cv2.imread(ruta)

    if imagen is None:
        print("No hay imagen")
        return

    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    brillo = cv2.convertScaleAbs(gris, alpha=1.2, beta=30)

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