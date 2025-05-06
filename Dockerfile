# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# Set the environment variable to control the environment (e.g., 'development' or 'production')
ENV TEST_ENV=development

# Run tests when the container starts
CMD ["behave"]
