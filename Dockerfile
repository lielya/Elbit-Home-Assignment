FROM python:latest

WORKDIR /home/user
COPY web_app.py ./
RUN pip install flask docker

CMD [ "python", "./web_app.py"]
