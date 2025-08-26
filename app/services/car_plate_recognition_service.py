from ultralytics import YOLO
import io
from PIL import Image
from sort.sort import *


class CarPlateRecoginitionService():
    def __init__(self):
        self._coco_model = YOLO('yolov11n.pt')
        self._license_plate_detector = YOLO('/app/models_ml/plate_recognition.pt')
        self._vehicles_ids = [2,3,5,6,7]
        self._mot_tracker = Sort() 
        
    def read_frame(self, frame):
      
      image_stream = io.BytesIO(frame)

      image = Image.open(image_stream)
      predictions = self._coco_model.predict(image)

      detections = []

      result = predictions[0] 

      for detection in result.boxes.data.tolist():
         #Todo: Transformar em uma classe 
         x1,y1,x2,y2,score, class_id = detection

         if int(class_id) in self._vehicles_ids:
            detections.append([x1,y1,x2,y2,score])
            

      






