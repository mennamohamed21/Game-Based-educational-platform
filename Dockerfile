FROM ubuntu:latest
MAINTAINER Emp "itsjustbulletz@hotmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app1
WORKDIR /app1
ENV PYTHONPATH /app1
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app/project.py"]