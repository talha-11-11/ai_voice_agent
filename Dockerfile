# Use the official Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

# Create the application directory
WORKDIR $APP_HOME

# Copy the requirements file first to leverage Docker's cache
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project files into the Docker image
COPY . .

# Expose the port for the Flask backend
EXPOSE 5000

# Set environment variables for Flask app
ENV FLASK_APP=backend.py

# Command to run the Flask backend server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]