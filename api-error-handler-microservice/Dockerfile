# Use Python 3.9 as base
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy necessary files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 3002
EXPOSE 3002

# Start the application
CMD ["python", "main.py"]
