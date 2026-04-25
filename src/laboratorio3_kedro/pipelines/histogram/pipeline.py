import sys
import os

# Asegurar que el directorio 'src' esté en PYTHONPATH para ejecuciones directas del archivo
current_dir = os.path.dirname(os.path.abspath(__file__))
# Regresamos 3 niveles: histogram -> pipelines -> laboratorio3_kedro -> src
src_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from kedro.pipeline import Pipeline, node
from laboratorio3_kedro.pipelines.histogram.nodes import analizar_imagen


def create_pipeline(**kwargs) -> Pipeline:
    """Crea el pipeline de análisis de histogramas."""
    return Pipeline(
        [
            node(
                func=analizar_imagen,
                inputs="params:image_path",
                outputs="resultado_analisis",
                name="analizar_imagen_node",
            )
        ]
    )
    