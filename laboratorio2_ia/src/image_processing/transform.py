import cv2

def apply_grayscale(image):
    """
    Convierte una imagen a escala de grises.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def adjust_brightness(image, alpha=1.2, beta=30):
    """
    Ajusta el brillo de una imagen.
    """
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
