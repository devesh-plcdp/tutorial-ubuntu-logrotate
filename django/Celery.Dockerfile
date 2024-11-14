# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update dependencies
RUN apt-get update && apt-get upgrade -y

# Install supervisor
RUN apt-get install -y supervisor

# Create the celery log directory
RUN mkdir -p /var/log/celery

# Copy the supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Set the working directory in the container
WORKDIR /home/django

# Copy the requirements file
COPY requirements.txt .

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose Celery Flower port
EXPOSE 5555

# Run logrotate setup
COPY logrotate.conf /etc/logrotate.d/celery_logs

# Run Supervisor to manage Celery workers
CMD ["supervisord", "-n"]
