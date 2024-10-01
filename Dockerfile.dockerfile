# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code and static files
COPY . .

# Expose port 80
EXPOSE 80

# Run the application
CMD ["python", "app.py"]
