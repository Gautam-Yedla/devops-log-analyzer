FROM python:3.11-slim

WORKDIR /app
COPY app/ ./
COPY requirements.txt ./

RUN pip install -r requirements.txt


ENV PYTHONPATH=/app

CMD ["python", "main.py"]


# FROM python:3.11-slim

# WORKDIR /app

# # Copy everything from app/ into /app/app/
# COPY app/ app/
# COPY requirements.txt ./
# COPY .env .env

# COPY app/sample_logs/ app/sample_logs/

# # Install dependencies
# RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Set PYTHONPATH to recognize 'app' as a package
# ENV PYTHONPATH=/app

# # Run the main script
# CMD ["python", "app/main.py"]
