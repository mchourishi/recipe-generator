# Use an official Python runtime as a parent image, This is the base image from which your container will be built. It’s a minimal version of Python 3.9.
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
 COPY . /app

 # Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside the container
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Copy the entrypoint script
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["/docker-entrypoint.sh"]

# Run the flask app, This starts the Flask app inside the container, making it accessible from outside the container.
CMD [ "flask" , "run", "--host=0.0.0.0" ]
