FROM jenkins/jenkins:lts

USER root

# Установка Docker CLI и Python с обходом PEP 668
RUN apt-get update && \
    apt-get install -y docker.io curl python3 python3-pip && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    pip install --no-cache-dir --upgrade pip --break-system-packages

# Установка kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod +x kubectl && mv kubectl /usr/local/bin/

# Добавление пользователя Jenkins в группу docker
RUN usermod -aG docker jenkins

USER jenkins
