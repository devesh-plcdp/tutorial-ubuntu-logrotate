# Use the official Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Django project
COPY . .

# Copy the Bash script
COPY /entrypoint.sh /entrypoint.sh

# Make the Bash script executable
RUN chmod +x /entrypoint.sh

# Expose port
EXPOSE 8000

# Convert the entrypoint script to Unix-style line endings
# RUN apt-get install -y dos2unix && dos2unix /entrypoint.sh && chmod +x /entrypoint.sh

# Run logrotate setup
COPY logrotate.conf /etc/logrotate.d/celery_logs

# Start the Bash script
CMD ["/entrypoint.sh"]
