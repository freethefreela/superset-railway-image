FROM apache/superset:latest

USER root


ENV SQLALCHEMY_DATABASE_URI $DATABASE_URL

ENV ADMIN_USERNAME $ADMIN_USERNAME
ENV ADMIN_EMAIL $ADMIN_EMAIL
ENV ADMIN_PASSWORD $ADMIN_PASSWORD

RUN pip install --no-cache-dir mysqlclient

WORKDIR /
COPY /config/superset_init.sh ./superset_init.sh
RUN chmod +x ./superset_init.sh

COPY /config/superset_config.py /app/

ENV SUPERSET_CONFIG_PATH /app/superset_config.py
ENV SECRET_KEY $SECRET_KEY
ENV REDIS_HOST $REDISHOST
ENV REDIS_PORT $REDISPORT
ENV REDIS_URL $REDIS_URL

USER superset

ENTRYPOINT [ "./superset_init.sh" ]
