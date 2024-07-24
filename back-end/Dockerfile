FROM python:3.11.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

ENV FASTAPI_PORT=5555
ENV WORKER_COUNT=3

# CMD ["fastapi", "run", "app/main.py", "--port", "80"]
CMD ["python", "main.py"]