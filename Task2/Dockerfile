# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install flask

# Make port 5000 available to the outside world
EXPOSE 5000

# Run the web application
CMD ["python", "app.py"]
