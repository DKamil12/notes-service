FROM jenkins/jenkins:lts

USER root

# Установка Docker CLI и Python
RUN apt-get update && \
    apt-get install -y docker.io curl python3 python3-pip && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    pip install --no-cache-dir --upgrade pip --break-system-packages

# Установка kubectl (надёжный способ)
RUN set -eux; \
    KUBECTL_VERSION="$(curl -s https://dl.k8s.io/release/stable.txt)"; \
    curl -LO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl"; \
    chmod +x kubectl; \
    mv kubectl /usr/local/bin/kubectl

# Добавление Jenkins в группу docker
RUN usermod -aG docker jenkins

USER jenkins
