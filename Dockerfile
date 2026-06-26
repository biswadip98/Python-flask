# Base image (OS)
FROM python:3.14-slim

#Current working directory inside the container
WORKDIR /app

#Copy the code into the container
COPY . .

#Install dependencies, # Run the build commands
RUN pip install -r requirements.txt

#Open port 80 for access locally
EXPOSE 80

# serve the app / run the app (keep it running)
CMD ["python", "run.py"]

