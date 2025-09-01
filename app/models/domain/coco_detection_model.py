from .bouding_box_model import BoudingBox
from typing import Optional, List
from .bouding_box_model import BoudingBox

class CocoDetectionModel:

    """Representa um carro detectado pelo YOLO"""
    def __init__(self, bouding_box:BoudingBox, score, class_id, frame):
        self.bouding_box = bouding_box
        self.score = score
        self.class_id = class_id
        self.original_frame = frame
        pass
 
        
    """Retorna um objeto do DetectedVehicleModel com base na resposta da detecção do YOLO"""
    @classmethod
    def from_yolo_detection(cls, detection_data: List[float], original_frame):
        x1, y1, x2, y2, score, class_id = detection_data

        try:
            box = BoudingBox(x1=x1,y1=y1,x2=x2,y2=y2)
        except ValueError:

            raise Exception('Erro ao tentar criar objeto veículo a partir da detecção do modelo')
        
        return cls(
            bouding_box = box,
            score = score,
            class_id = int(class_id),    
            frame = original_frame  
        )
    """Retorna se a detectação foi ou não de um veículo"""
    @property
    def is_vehicle(self):
        vehicle_ids =  [2,3,5,6,7]
        return self.class_id  in vehicle_ids

