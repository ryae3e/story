import os
import json

# Folder paths 
DEVCONTAINER_FOLDER = '.devcontainer'
DOCKER_COMPOSE_FILE = 'docker-compose.yml'
DOCKERFILE = 'Dockerfile'

# devcontainer.json contents
devcontainer_config = {
  "name": "Python 3 & Node.js",

  "dockerComposeFile": DOCKER_COMPOSE_FILE,

  "features": {
    "ghcr.io/devcontainers/features/python:1": {}
  },

  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python" 
      ]
    }
  }
}

# docker-compose.yml contents
docker_compose_config = '''
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile  
'''

# Dockerfile contents
dockerfile_config = '''
FROM python:3.8

# Install nodejs
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \\
    && apt install -y nodejs
    
# Install python packages etc    
'''

# Create .devcontainer folder
os.mkdir(DEVCONTAINER_FOLDER)

# Create devcontainer.json
with open(os.path.join(DEVCONTAINER_FOLDER, 'devcontainer.json'), 'w') as f:
    json.dump(devcontainer_config, f)
    
# Create docker-compose.yml    
with open(os.path.join(DEVCONTAINER_FOLDER, DOCKER_COMPOSE_FILE), 'w') as f:
    f.write(docker_compose_config)

# Create Dockerfile
with open(os.path.join(DEVCONTAINER_FOLDER, DOCKERFILE), 'w') as f: 
    f.write(dockerfile_config)

print("Devcontainer configuration created!")