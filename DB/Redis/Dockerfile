FROM redis

COPY script.sh /

WORKDIR /

RUN chmod +x script.sh

ENTRYPOINT [ "./script.sh" ]

EXPOSE 6379 
