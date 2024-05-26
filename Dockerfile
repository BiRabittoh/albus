# Use the Alpine Linux base image
FROM alpine:latest

# Install dependencies
RUN apk update && \
    apk add --no-cache \
    pandoc \
    python3 \
    py3-pip \
    build-base \
    tectonic

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

# Copy the rest of the application code
COPY albus albus

# Add a non-root user and use it
RUN adduser -D appuser && \
    chown -R appuser /app
USER appuser

# Set the entrypoint to your application or provide a command for the container to run
CMD ["python", "-m", "albus.bot"]
