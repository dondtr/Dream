FROM eclipse-temurin:17-jdk-jammy

ENV APP_USER=lucy \
    APP_PORT=8080 \
    DEBUG_PORT=5005

RUN adduser --disabled-password --gecos "" "${APP_USER}"

WORKDIR /app

COPY --chown=${APP_USER}:${APP_USER} ./deploy/ApiTest-0.0.1-SNAPSHOT.jar ./app.jar

USER ${APP_USER}

EXPOSE ${APP_PORT}
EXPOSE ${DEBUG_PORT}

CMD ["java", \
     "-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005", \
     "-jar", \
     "/app/app.jar"]