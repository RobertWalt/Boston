# app/Dockerfile# Start with a base image
FROM python:3-onbuild

# Copy our application code
COPY . .
COPY requirements.txt .

# Fetch app specific dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Start the app
WORKDIR App
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]