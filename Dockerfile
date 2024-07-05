# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk update \
    && apk add --no-cache postgresql-dev gcc python3-dev musl-dev

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variables
ENV DATABASE_URL="sqlite:///development.db"
ENV JWT_SECRET_KEY="your_secret_key"

# Command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
