from PIL import Image
import io

class ByteToImageService:
    def __init__(self):
        pass

    """Converte um frame para uma imagem"""
    def frame_to_image_conveter(self,frame):
        try:
             image_stream = io.BytesIO(frame)
             image = Image.open(image_stream)
             image.load() 
        
             return image
        except Exception as e:
            print(f"ERRO: Falha ao converter bytes para imagem. Detalhes: {e}")
        return None