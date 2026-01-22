#use official lightweight python image
FROM python:3.10-slim

#set working directory
WORKDIR /app

#install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# copy requirements 
COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]