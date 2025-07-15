FROM python:latest

RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app
# source destination

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# RUN within_container_while_building
COPY ./src .  

CMD [ "python", "-m", "http.server", "8000" ]