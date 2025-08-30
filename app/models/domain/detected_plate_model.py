from .bouding_box_model import BoudingBox
from typing import Optional, List

class DetectedPlateModel:
    """Modelo de uma placa de carro identificada pelo YOLO"""
    def __init__(self, original_frame, bouding_box : BoudingBox, score, class_id):
        self.original_frame = original_frame
        self.bouding_box: BoudingBox =  bouding_box,
        self.score = score
        self.class_id = class_id


    """Retorna uma imagem com a plca a partir do frame inicial"""
    @property
    def cropped_image(self):
        return self.original_frame[self.bouding_box.y1:self.bouding_box.y2, self.bouding_box.x1:self.bouding_box.x2, :]
    

    """Retorna uma classe DetectedPlateModal com base no retorno do YOLO"""
    @classmethod
    def from_yolo_detection(cls, detection_data: List[float], original_frame):
        x1, y1, x2, y2, score, class_id = detection_data
        try:
            box = BoudingBox(x1=x1, y1=y1, x2=x2, y2=y2 )

        except ValueError:
            raise Exception("Erro ao criar bouding box")
        
        return cls(
            score = score,
            class_id = class_id,
            original_frame = original_frame,
            box = box,
        )


     



        
