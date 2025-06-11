FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY app/ ./app
COPY tests/ ./tests


COPY requirements.txt ./

COPY .env .env

RUN pip install -r requirements.txt


CMD ["python", "app/main.py"]

# FROM python:3.11-slim

# # Set working directory inside the container
# WORKDIR /app

# # Set PYTHONPATH so Python knows where to find your modules
# ENV PYTHONPATH=/app

# # Copy everything from local directory into the container
# COPY . .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Default command: run your main app
# CMD ["python", "app/main.py"]
