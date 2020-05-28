FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /smm
WORKDIR /smm
COPY requirements.txt /smm/
RUN pip install -r requirements.txt
COPY . /smm/