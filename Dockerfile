FROM python:3.8

WORKDIR /src/app

RUN pip install pandas scikit-learn flask gunicorn

COPY . .

ADD ./model ./model
ADD server.py server.py

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD ["server.py", "run", "--host", "0.0.0.0"]