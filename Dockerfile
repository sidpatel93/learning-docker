FROM python:3.9.5-alpine3.13

RUN apk add --no-cache python3 py3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python","hello.py" ]