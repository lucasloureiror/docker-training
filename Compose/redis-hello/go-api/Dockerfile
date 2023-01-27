#Build
FROM golang:1.19.5-alpine as build

WORKDIR /app

COPY go.mod ./

COPY go.sum ./

COPY Main.go ./

RUN go build -o /API



#Deploy
FROM alpine:latest

WORKDIR /

COPY --from=build /API /API

EXPOSE 8080
RUN addgroup -S cetacean && adduser -S mobydick -G cetacean

USER mobydick

ENTRYPOINT [ "/API" ]

