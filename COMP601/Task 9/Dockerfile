FROM openjdk:19
VOLUME /tmp
ARG JAVA_OPTS
ENV JAVA_OPTS=$JAVA_OPTS
COPY . /usr/src/JavaApp
WORKDIR /usr/src/JavaApp/src
RUN javac App.java
CMD ["java", "App"]