FROM ubuntu:latest
LABEL authors="jonat"

ENTRYPOINT ["top", "-b"]