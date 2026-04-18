import pytest
import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.image_processing.transform import apply_grayscale, adjust_brightness

def test_apply_grayscale():
    # Crear una imagen ficticia de 10x10 en BGR
    dummy_image = np.zeros((10, 10, 3), dtype=np.uint8)
    
    gris = apply_grayscale(dummy_image)
    
    # La imagen en gris debe tener ancho y alto, pero no canales (o 1 canal implícito)
    assert len(gris.shape) == 2
    assert gris.shape == (10, 10)

def test_adjust_brightness():
    dummy_image = np.zeros((10, 10), dtype=np.uint8)
    
    brillo = adjust_brightness(dummy_image, alpha=1.0, beta=50)
    
    # El valor debería haber sumado 50 a los pixeles
    assert np.all(brillo == 50)
