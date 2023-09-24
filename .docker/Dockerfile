
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install any dependencies or packages required for development
RUN pip install -r requirements-dev.txt

# Set entrypoint
CMD ["python", "app.py"]
