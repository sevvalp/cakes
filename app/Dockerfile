# Use an official Python runtime as a parent image
FROM python:3.11.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
RUN python3 -m pip install --upgrade pip setuptools wheel
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r app/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

CMD ["python", "transformer.py"]
