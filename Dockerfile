FROM python:3.13.3-alpine3.21

COPY requirements.txt /
COPY dj_practice /dj_practice
RUN pip install -r requirements.txt

WORKDIR /dj_practice

COPY docker_image_entrypoint.sh .

ENTRYPOINT ["./docker_image_entrypoint.sh"]
