# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container to /flask-login
WORKDIR /flask-login

# Copy the current directory contents into the container at /flask-login
COPY . /flask-login

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=auth.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run app.py when the container launches
CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"]
