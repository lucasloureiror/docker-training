#Build
FROM golang:1.19.5-alpine as build

WORKDIR /app

COPY go.mod ./

COPY *.go ./

RUN go build -o /HelloWorld



#Deploy
FROM alpine:latest

WORKDIR /

COPY --from=build /HelloWorld /HelloWorld

EXPOSE 80
RUN addgroup -S cetacean && adduser -S mobydick -G cetacean

USER mobydick

ENTRYPOINT [ "/HelloWorld" ]



