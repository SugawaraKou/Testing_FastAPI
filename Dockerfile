FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/src

COPY requirements.txt /code/requirements.txt
COPY app.log /code/app.log

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src
ENV PYTHONPATH=/code/src

CMD ["python3", "main.py"]
