# Variables
IMAGE_NAME=albus
REQUIREMENTS=requirements.txt
ENV_FILE=.env

.PHONY: all clean build

all: build

# Export requirements using Poetry
$(REQUIREMENTS): pyproject.toml poetry.lock
	poetry export -f requirements.txt --output $(REQUIREMENTS) --without-hashes

# Build the Docker image
build: $(REQUIREMENTS)
	docker build -t $(IMAGE_NAME) .

# Utility target to run the Docker container
run: $(ENV_FILE)
	docker-compose up -d
