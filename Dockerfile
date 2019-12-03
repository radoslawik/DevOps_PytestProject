FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
ADD . .
CMD [ "python3", "./haversine.py", "db", "root", "pass" ]
RUN pytest