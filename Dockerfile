# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed dependencies specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a directory for chromedriver and copy the executable from host to container

COPY chromedriver.exe .

# Set PATH environment variable to include chromedriver

# Set display environment variable (required for Selenium)
ENV DISPLAY=:99

# Copy the current directory contents into the container at /app
COPY . .

# Run your Python script when the container launches
#CMD ["python", "-m", "Front_Test_Framework_NG.Tests.Main", "0"]
