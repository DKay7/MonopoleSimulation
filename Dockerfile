# Use an official Python runtime as a parent image
# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN python3 -m venv .venv
RUN . .venv/bin/activate
RUN pip3 install -r src/requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV NAME World

# Run Streamlit when the container launches
CMD ["streamlit", "run", "src/main.py"]