# Use a lightweight version of Python as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Make sure the .env file is not copied into the container
# .dockerignore will ensure .env is ignored

# Expose the port your app will use (optional, if needed)
EXPOSE 8000

# Run the Python application
CMD ["python", "app/main.py"]
