from ultralytics import YOLO
from sort.sort import *
from app.models.domain.detected_vehicle_model import DetectedVehicleModel

class VehicleDectionService:
    def __init__(self):
        self._model = YOLO('yolov11n.pt')
        self._vehicles_ids = [2,3,5,6,7]
        pass

    """Detecta o veículo com base no frame"""
    def detect_vehicles(self, frame):
     
     vehicles_predictions = self._model.predict(self, frame)

     vehicles_result = vehicles_predictions[0] 

     for results in vehicles_result.boxes.data.tolist():
         
         detected_vehicle = DetectedVehicleModel.from_yolo_detection(results, frame)
        
         if  detected_vehicle.class_id in self._vehicles_ids:
      
            return detected_vehicle
         
         raise Exception("Veículo não encontrado!")
    
        
    
    