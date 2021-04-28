FROM python:3.9.4-alpine
ENV PYTHONUNBUFFERED=1

RUN apk update \
	# psycopg2 dependencies
	&& apk add --virtual build-deps gcc python3-dev musl-dev \
	&& apk add postgresql-dev \
	# CFFI dependencies
	&& apk add libffi-dev py-cffi \
	&& apk add --no-cache openssl-dev libffi-dev \
	&& apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev

RUN mkdir /app
WORKDIR /app
COPY ./requirements /app/
RUN pip install -r local.txt
COPY . /app/
