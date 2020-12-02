# pull official base image
FROM python:3.8-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/scripts:${PATH}"

# install dependencies
COPY requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

# copy directory
RUN mkdir /app
COPY ./app /app

# set work directory
WORKDIR /app

# copy directory
COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
RUN chown -R user:user /app
USER user

CMD ["entrypoint.sh"]