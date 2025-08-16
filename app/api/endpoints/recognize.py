import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

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

    #Caso haja uma disconexão informa o erro
    except WebSocketDisconnect:
        logger.info(f"Cliente de teste desconectado: {websocket.client.host}")
    #Sempre fecha a conexão no final 
    except Exception as e:
        logger.error(f"Ocorreu um erro na conexão: {e}")
    finally:
        await websocket.close()

