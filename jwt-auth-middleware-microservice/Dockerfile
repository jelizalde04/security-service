# Usar Python 3.9 como base
FROM python:3.9

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 3001
EXPOSE 3001

# Comando de inicio
CMD ["python", "main.py"]
