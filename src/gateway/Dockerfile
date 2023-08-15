# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the local requirements.txt file to the container
COPY requirements.txt ./

# Install any required packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9001", "--reload", "True"]