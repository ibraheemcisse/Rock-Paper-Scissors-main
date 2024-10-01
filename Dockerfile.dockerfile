# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for the app
EXPOSE 80

# Define environment variable
ENV FLASK_APP=app.py

# Run the application on port 80
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]