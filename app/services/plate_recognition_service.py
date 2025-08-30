from ultralytics import YOLO
from app.models.domain.detected_plate_model import DetectedPlateModel

class PlateRecognitionService:
    def __init__(self):
        self._license_plate_detector = YOLO('/app/models_ml/plate_recognition.pt')
        pass


    """Detecta o veículo com base no frame, e atualiza o Mot Tracker"""
    def detect_license_plate(self, frame)->DetectedPlateModel:
      
      license_plates_prediciton = self._license_plate_detector.predict(frame)[0]

      if(len(license_plates_prediciton) == 0):
         
         return None

      for results in license_plates_prediciton.boxes.data.tolist():

        detected_plate = DetectedPlateModel.from_yolo_detection(results)

      return detected_plate


