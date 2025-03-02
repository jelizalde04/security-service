# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the microservice port
EXPOSE 3003

# Run the application
CMD ["python", "main.py"]
