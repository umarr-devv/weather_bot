FROM python:3.11
WORKDIR home/bot
COPY . home/bot
RUN pip install -r home/bot/requirements.txt