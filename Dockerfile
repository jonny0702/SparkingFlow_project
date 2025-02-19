FROM apache/airflow:2.7.1-python3.11

USER root
RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-11-jdk procps iputils-ping  && \
    apt-get clean

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

USER airflow

RUN pip install \
    apache-airflow==2.7.1 \
    apache-airflow-providers-apache-spark==4.0.1 \
    pyspark