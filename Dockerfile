FROM python:3.8-slim

ADD . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "./tests.py"]