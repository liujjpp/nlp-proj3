# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:1.8.1

USER root

ADD project_2 /app/project_2

ADD docker_dependencies.txt /app/docker_dependencies.txt

ADD actions /app/actions

# Add a custom system library (e.g. git)
RUN apt-get update && \
    apt-get install -y git

# Add a custom python library (e.g. jupyter)
RUN pip install -r docker_dependencies.txt

# change user to not run as root
USER 1001

EXPOSE $PORT