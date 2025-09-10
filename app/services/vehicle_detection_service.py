from ultralytics import YOLO
import logging
from app.models.domain.coco_detection_model import CocoDetectionModel

logger = logging.getLogger(__name__)

class VehicleDectionService:
    def __init__(self):
        self._model = YOLO('/app/models_ml/yolo11n.pt')
        pass

    """Detecta o veículo com base no frame"""
    def detect_vehicles(self, frame):
     
     vehicles_predictions = self._model.predict(frame)

     vehicles_result = vehicles_predictions[0]

     if (len(vehicles_result) == 0):
         
         return None


     for results in vehicles_result.boxes.data.tolist():
         
         coco_detection = CocoDetectionModel.from_yolo_detection(results, frame)
         
         return coco_detection
    
        
    
    