# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /people_api

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Default command (you can override in podman run)
CMD ["python", "main.py"]