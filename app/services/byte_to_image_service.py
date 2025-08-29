from PIL import Image
import io

class ByteToImageService:
    def __init__(self):
        pass

    """Converte um frame para uma imagem"""
    def frameToImageConveter(frame):
        image_stream = io.BytesIO(frame)
        return Image.open(image_stream)
    