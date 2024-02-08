FROM python:3.8

WORKDIR /kata

COPY user-registration/requirements.txt .
RUN pip install -r requirements.txt