import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.byte_to_image_service import ByteToImageService
from app.services.plate_recognition_service import PlateRecognitionService
from app.services.vehicle_detection_service import VehicleDectionService
from app.services.ocr_service import OCRService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

image_converter = ByteToImageService()
vehicle_recognizer = VehicleDectionService()
plate_recognizer = PlateRecognitionService()
ocr = OCRService()

#Define que o tipo de conexão que iremos usar é webscoket
@router.websocket("/ws/recognize")
async def websocket_reconize(websocket: WebSocket):

    #Recebe a conexão e conecta com o usuário
    await websocket.accept()
    logger.info(f"Usuário conectado via WebScoket: {websocket.client.host}")

    frame_count:int = 0

    try:
        while True:
            image_bytes = await websocket.receive_bytes()

            frame_size_kb = len(image_bytes)/1024
            frame_count += 1
            logger.info(f"Frame: {frame_count} recebido! Tamanho: {frame_size_kb:.2f} KB")

            
            image = image_converter.frame_to_image_conveter(image_bytes)
            coco_detection = vehicle_recognizer.detect_vehicles(image)

            if(coco_detection != None and coco_detection.is_vehicle):

                license_plate = plate_recognizer.detect_license_plate(image)

                if(license_plate != None):
                    license_plate_text =  ocr.process_license_plate(license_plate.cropped_image)
                    await websocket.send_json({"license_plate":license_plate_text})
                    break


    #Caso haja uma disconexão informa o erro
    except WebSocketDisconnect:
        logger.info(f"Cliente de teste desconectado: {websocket.client.host}")
    #Sempre fecha a conexão no final 
    except Exception as e:
        logger.error(f"Ocorreu um erro na conexão: {e}")
    finally:
        await websocket.close()

