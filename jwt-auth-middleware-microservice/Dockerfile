# Use official Python image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the service port
EXPOSE 3001

# Command to run the application
CMD ["python", "main.py"]
