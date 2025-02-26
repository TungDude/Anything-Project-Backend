FROM python:3.9-slim-buster

WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

# Copy and Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Set and expose port environment variable
ENV PORT=5000
EXPOSE 5000

CMD [ "python3", "run.py" ]