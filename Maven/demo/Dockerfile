#Build Stage
FROM maven AS build

WORKDIR /server

COPY src ./src

#Copiando as Dependênbcias
COPY pom.xml ./

#Gera o arquivo jar no /target
RUN mvn clean package

#Deploy - Utilizando JDK da Amazon(Corretto)
FROM amazoncorretto:17
WORKDIR /server
COPY --from=build /server/target/*.jar ./app.jar
ENTRYPOINT ["java","-jar","./app.jar"]