 FROM python:3.9-alpine

 RUN apk update \
    && apk add --no-cache mariadb-dev build-base

 WORKDIR /usr/src/app
 COPY requirements.txt ./
 
 RUN python -m pip install --upgrade pip
 
 RUN pip install -r requirements.txt
 
 COPY . .

 EXPOSE 8210

 # 去除windows系统编辑文件中多余的\r回车空格
 RUN sed -i 's/\r//' ./start.sh

 # 给start.sh可执行权限
 RUN chmod +x ./start.sh

 CMD ["sh","./start.sh"]
