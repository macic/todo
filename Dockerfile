ARG project=todo

FROM python:3.8.2-alpine as base

RUN set -ex \
    && apk --no-cache add \
    postgresql-libs \
	build-base \
    libxml2-dev \
    libxslt-dev \
    openssl-dev \
    && apk --no-cache add --virtual .build-deps gcc musl-dev postgresql-dev

RUN mkdir -p /source/$project
WORKDIR /source/$project
ENV PYTHONPATH=/source/$project

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

ADD . ./