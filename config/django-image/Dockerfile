FROM python:3.12.2-bookworm

RUN apt-get update && apt-get install python3-dev libgdal-dev graphviz graphviz-dev -y

WORKDIR /usr/src/app

RUN pip install --upgrade pip && pip install --upgrade setuptools

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN mkdir /script
COPY runserver.sh /script
RUN chmod +x /script -R

CMD ["/bin/bash","/script/runserver.sh"]