import cv2
import os

def load_image(path):
    """
    Carga una imagen desde la ruta especificada.
    """
    if not os.path.exists(path):
        print("No hay imagen en la ruta:", path)
        return None
    
    imagen = cv2.imread(path)
    if imagen is None:
        print("Error al cargar la imagen")
        return None
        
    return imagen
