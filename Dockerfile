FROM python:3.8-slim

WORKDIR /usr/src/ipextractor

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ipextractor ./
COPY config.ini init.sh README.md LICENCE ./

ENTRYPOINT ["sh", "init.sh"]
# CMD python main.py