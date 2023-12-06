#We will use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

#Seting the working directory to /app
WORKDIR /app

# Install FFMPEG
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

#Copying the current directory contents into the container at /app
COPY . /app

#Running the app.py when the container launches
CMD ["ffmpeg", "--version"]
