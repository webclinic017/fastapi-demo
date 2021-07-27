FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY ./app /app/app
COPY ./setup.py /app/setup.py
COPY ./prestart.sh /app/prestart.sh
RUN python /app/setup.py install