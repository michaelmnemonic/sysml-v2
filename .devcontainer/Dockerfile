FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# Install SBT
COPY sbt.list /etc/apt/sources.list.d/
COPY sbt.asc /etc/apt/trusted.gpg.d/
RUN apt -y update && apt -y install openjdk-11-jdk postgresql sbt

# Setup PostgreSQL
RUN service postgresql start && \
    sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'mysecretpassword';" && \
    sudo -u postgres createdb -O postgres sysml2 

# Get SysML-v2-API-Services
#RUN git clone https://github.com/Systems-Modeling/SysML-v2-API-Services.git /opt/