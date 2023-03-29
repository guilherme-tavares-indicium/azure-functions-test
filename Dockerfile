# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files to working directory
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD ["python", "main.py"]
