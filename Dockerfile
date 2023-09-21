# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables for mysqlclient
ENV MYSQLCLIENT_CFLAGS=-I/usr/include/mariadb
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmariadb"

# Set the working directory in the container
WORKDIR /app

# Install NLTK and download the VADER lexicon data
RUN pip install nltk && \
    python -m nltk.downloader vader_lexicon

# Install system dependencies for "pattern" and pkg-config
RUN apt-get update && \
    apt-get install -y libmariadb-dev build-essential pkg-config

# Install the "pattern" library
RUN pip install pattern

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 8000 for the FastAPI app (Uvicorn defaults to 8000)
EXPOSE 8000

# Define the command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
