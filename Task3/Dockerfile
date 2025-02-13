# Use an official Python image as the base
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the app to the container
COPY app.py /app

# Install Flask
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
