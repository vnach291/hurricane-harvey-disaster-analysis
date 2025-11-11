FROM python:3.10-slim 
WORKDIR /app
COPY docker_requirements.txt .
RUN pip install --default-timeout=300 -r docker_requirements.txt
COPY server.py best_swin_model.pth ./
EXPOSE 5000
CMD ["python", "server.py"]