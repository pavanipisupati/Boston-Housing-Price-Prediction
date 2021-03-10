FROM python:3.8

WORKDIR /src/app

RUN pip install pandas scikit-learn flask flask_api coverage jsonschema gunicorn

COPY . .

ADD ./model ./model
ADD ./app/server_app.py ./app/server_app.py

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD ["./app/server_app.py","-u", "run", "--host", "0.0.0.0"]