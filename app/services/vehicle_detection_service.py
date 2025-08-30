from ultralytics import YOLO
import logging
from app.models.domain.detected_vehicle_model import DetectedVehicleModel

logger = logging.getLogger(__name__)

class VehicleDectionService:
    def __init__(self):
        self._model = YOLO('yolo11n.pt')
        self._vehicles_ids = [2,3,5,6,7]
        pass

    """Detecta o veículo com base no frame"""
    def detect_vehicles(self, frame):
     
     vehicles_predictions = self._model.predict(frame)

     vehicles_result = vehicles_predictions[0]

     if (len(vehicles_result) == 0):
         
         return None


     for results in vehicles_result.boxes.data.tolist():
         
         detected_vehicle = DetectedVehicleModel.from_yolo_detection(results, frame)
        
         if  detected_vehicle.class_id in self._vehicles_ids:

            return detected_vehicle
         
         return None
    
        
    
    