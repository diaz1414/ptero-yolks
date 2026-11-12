FROM --platform=$TARGETOS/$TARGETARCH node:19-slim

LABEL author="diaww.dev" maintainer="ferdiazprasida@gmail.com"
LABEL org.opencontainers.image.source="https://github.com/diaz1414/ptero-yolks"

RUN echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until \
    && if [ -f /etc/apt/sources.list ]; then \
        if grep -q -E 'buster|stretch' /etc/apt/sources.list 2>/dev/null; then \
            sed -i 's|deb.debian.org/debian|archive.debian.org/debian|g' /etc/apt/sources.list && \
            sed -i 's|security.debian.org/debian-security|archive.debian.org/debian-security|g' /etc/apt/sources.list && \
            sed -i 's|security.debian.org|archive.debian.org|g' /etc/apt/sources.list && \
            sed -i '/updates/d' /etc/apt/sources.list ; \
        fi ; \
    fi \
    && apt-get update -o Acquire::Check-Valid-Until=false --allow-releaseinfo-change \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        ffmpeg \
        build-essential \
        python3 \
        tzdata \
        zip \
        unzip \
        iproute2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -d /home/container -m container

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER container
ENV USER=container HOME=/home/container
WORKDIR /home/container

CMD ["/bin/bash", "/entrypoint.sh"]
