from PIL import Image
import xerox
from PIL import Image
import io

def image_to_bytes(image_path):
    with open(image_path, 'rb') as f:
        image = Image.open(f)

        # Convierte la imagen a bytes
        with io.BytesIO() as output:
            image.save(output, format='PNG')
            return output.getvalue()

# Ejemplo de uso
def copy_image_to_clipboard(image_path):
    
    xerox.copy(image_to_bytes(image_path))


copy_image_to_clipboard("C:\Cosas\Proyectos\WppBot\clipboard.png")
