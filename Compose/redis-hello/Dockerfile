FROM python

RUN pip install uvicorn[standard] && pip install fastapi && pip install redis

WORKDIR /app

COPY App.py .

EXPOSE 80

CMD uvicorn App:app --reload --host 0.0.0.0 --port 80

