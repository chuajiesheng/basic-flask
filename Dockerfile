FROM python:3-buster AS base

LABEL maintainer="Chua Jie Sheng <hello@jschua.com>"

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gunicorn3

WORKDIR /wheels
COPY README.md /wheels/README.md
COPY setup.py /wheels/setup.py

RUN pip3 install --upgrade pip \
    && pip3 wheel '.[test]' --wheel-dir=/wheels

WORKDIR /app
COPY . /app
RUN mkdir -p uploads/resumes

FROM base AS test

RUN pip3 install '.[test]' --find-links=/wheels \
    && python3 setup.py test

FROM base AS deploy

RUN pip3 install . --find-links=/wheels \
    && python3 setup.py install

EXPOSE 5000

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["gunicorn", "-t 300", "-b 0.0.0.0:5000", "engine:app"]
