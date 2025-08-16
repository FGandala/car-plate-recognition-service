#Imagem base 
FROM python:3.10-slim

#Diretório de trabalho
WORKDIR /app

#Cópia as blibliotecas
COPY requirements.txt

#Instala as blibliotecas
RUN pip install --no-cache-dir -r requirements.txt

#Copía o código principal do serviço e os modelos de ml
COPY ./app ./app
COPY ./models_ml ./models_ml

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0","--port","8000"]
