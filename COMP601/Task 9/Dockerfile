FROM openjdk:19
VOLUME /tmp
ARG JAVA_OPTS
ENV JAVA_OPTS=$JAVA_OPTS
COPY . /usr/src/JavaApp
WORKDIR /usr/src/JavaApp/src
RUN javac App.java
CMD ["java", "App"]
# For Spring-Boot project, use the entrypoint below to reduce Tomcat startup time.
#ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar task8.jar
