FROM python:3.10

# working directory inside container
WORKDIR /app

# copy requirements
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY . .

# expose API port
EXPOSE 8000

# run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]