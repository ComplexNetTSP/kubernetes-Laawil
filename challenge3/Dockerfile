# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /projetkubernetes-ali

# Copy the application files into the container
COPY . /projetkubernetes-ali

# Install dependencies
RUN pip install flask
RUN pip install pymongo

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
