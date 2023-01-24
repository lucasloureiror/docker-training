FROM mysql:latest

RUN chown -R mysql:root /var/lib/mysql/
COPY script.sql /docker-entrypoint-initdb.d/script.sql
RUN chmod -R 775 /docker-entrypoint-initdb.d

ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_ROOT_PASSWORD

ENV MYSQL_ROOT_PASSWORD root

EXPOSE 3306