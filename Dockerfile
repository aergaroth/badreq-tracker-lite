FROM python:3.13-slim

WORKDIR /app

# create non-root user
RUN useradd -ms /bin/bash uuser

# copy files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ ./app/

# give ownership to non-root user
RUN chown -R uuser:uuser /app

USER uuser

EXPOSE 5000

CMD ["python", "-m", "app.main"]
