# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all necessary files
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command allows flexibility to either run the script or execute tests
ENTRYPOINT ["python"]
CMD ["geo_util.py"]
