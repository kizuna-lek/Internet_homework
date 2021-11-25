FROM mysql:5.7
COPY ./mysql-script /usr/local/sql
COPY ./initdb.sh /docker-entrypoint-initdb.d/
RUN chmod a+x /docker-entrypoint-initdb.d/initdb.sh
