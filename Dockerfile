# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Install wget to download protoc
RUN apt-get update && apt-get install -y protobuf-compiler


# Set the working directory
WORKDIR /app

# Copy all files
COPY . .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the protoc command and then keep the container running
CMD protoc -I ./protoDef --python_out=./protoCompile proto.proto && tail -f /dev/null