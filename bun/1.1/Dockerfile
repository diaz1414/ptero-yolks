FROM oven/bun:1.1-debian AS bun-source

FROM --platform=$TARGETOS/$TARGETARCH debian:bookworm-slim

LABEL author="diaww.dev" maintainer="ferdiazprasida@gmail.com"
LABEL org.opencontainers.image.source="https://github.com/diaz1414/ptero-yolks"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        ffmpeg \
        imagemagick \
        build-essential \
        python3 \
        tzdata \
        zip \
        unzip \
        iproute2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=bun-source /usr/local/bin/bun /usr/local/bin/bun
RUN ln -s /usr/local/bin/bun /usr/local/bin/bunx 2>/dev/null || true

RUN useradd -d /home/container -m container

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER container
ENV USER=container HOME=/home/container
WORKDIR /home/container

CMD ["/bin/bash", "/entrypoint.sh"]
