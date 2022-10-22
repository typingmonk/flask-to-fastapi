FROM tiangolo/uvicorn-gunicorn-fastapi

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY run.py ./

RUN pip3 install --no-cache-dir -r requirements.txt

CMD python run.py
