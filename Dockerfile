FROM maven:3.9.1-amazoncorretto-17 as BUILDER
ARG VERSION=0.0.1-SNAPSHOT
WORKDIR /build
COPY pom.xml /build/
COPY src /build/src/

RUN mvn clean package
COPY target/booting-web-${VERSION}.jar target/application.jar

FROM openjdk:17.0.2-jdk-slim
WORKDIR /app/

COPY --from=BUILDER /build/target/application.jar /app/
CMD java -jar /app/application.jar