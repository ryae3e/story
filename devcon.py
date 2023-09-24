import os
import json

# Folder paths
DOCKER_FOLDER = '.docker'
DOCKER_COMPOSE_FILE = 'docker-compose.yml'
DOCKERFILE = 'Dockerfile'
REQUIREMENTS_FILE = 'requirements-dev.txt'

# Create .docker folder
os.mkdir(DOCKER_FOLDER)

# Create docker-compose.yml
docker_compose_config = '''
version: '3'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
'''
with open(os.path.join(DOCKER_FOLDER, DOCKER_COMPOSE_FILE), 'w') as f:
    f.write(docker_compose_config)

# Create Dockerfile
dockerfile_config = '''
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install any dependencies or packages required for development
RUN pip install -r requirements-dev.txt

# Set entrypoint
CMD ["python", "app.py"]
'''
with open(os.path.join(DOCKER_FOLDER, DOCKERFILE), 'w') as f:
    f.write(dockerfile_config)

# Create requirements-dev.txt
with open(os.path.join(DOCKER_FOLDER, REQUIREMENTS_FILE), 'w') as f:
    # Write any development dependencies required
    f.write('')

# Print success message
print("Docker configuration created!")