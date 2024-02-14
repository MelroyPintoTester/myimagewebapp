FROM ubuntu

RUN apt-get update && apt-get install python3 python3-pip -y

RUN pip install Flask

RUN mkdir /home/webimageapp

COPY . /home/webimageapp

CMD ["python3","/home/webimageapp/app.py"]
