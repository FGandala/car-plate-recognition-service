from ultralytics import YOLO
from sort.sort import *
from app.models.domain.detected_vehicle_model import DetectedVehicleModel

class VehicleDectionService:
    def __init__(self):
        self._model = YOLO('yolov11n.pt')
        self._vehicles_ids = [2,3,5,6,7]
        self._mot_tracker = Sort() 
        pass

    """Detecta o veículo com base no frame, e atualiza o Mot Tracker"""
    def detect_vehicles(self, frame):
     
     vehicles_predictions = self._model.predict(self, frame)

     vehicles_detections = []

     vehicles_result = vehicles_predictions[0] 

     for results in vehicles_result.boxes.data.tolist():
         
         detected_vehicle = DetectedVehicleModel.from_yolo_detection(results)
        
         if  detected_vehicle.class_id in self._vehicles_ids:

            vehicles_detections.append(detected_vehicle.to_list())
      
         return self._mot_tracker.update(np.asanyarray(vehicles_detections))
    
        
    
    