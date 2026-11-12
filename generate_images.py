import os
import json

base_dir = r"c:\diaz\egg python&nodejs"

node_versions = [
    "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"
]

python_versions = [
    "2.7", "3.7", "3.8", "3.9", "3.10", "3.11", "3.12", "3.13", "3.14", "3.15"
]

def make_node_dockerfile(ver):
    return f"""FROM --platform=$TARGETOS/$TARGETARCH node:{ver}-slim

LABEL author="diaww.dev" maintainer="ferdiazprasida@gmail.com"
LABEL org.opencontainers.image.source="https://github.com/DIAWWDEV/yolks"

RUN if [ -f /etc/apt/sources.list ]; then \\
        if grep -q 'Debian GNU/Linux 10' /etc/issue 2>/dev/null || grep -q 'buster' /etc/apt/sources.list 2>/dev/null; then \\
            sed -i 's|deb.debian.org/debian|archive.debian.org/debian|g' /etc/apt/sources.list && \\
            sed -i 's|security.debian.org/debian-security|archive.debian.org/debian-security|g' /etc/apt/sources.list && \\
            sed -i '/buster-updates/d' /etc/apt/sources.list ; \\
        elif grep -q 'Debian GNU/Linux 9' /etc/issue 2>/dev/null || grep -q 'stretch' /etc/apt/sources.list 2>/dev/null; then \\
            sed -i 's|deb.debian.org/debian|archive.debian.org/debian|g' /etc/apt/sources.list && \\
            sed -i 's|security.debian.org|archive.debian.org|g' /etc/apt/sources.list && \\
            sed -i '/stretch-updates/d' /etc/apt/sources.list ; \\
        fi ; \\
    fi \\
    && apt-get update --allow-releaseinfo-change \\
    && apt-get install -y --no-install-recommends \\
        ca-certificates \\
        curl \\
        git \\
        ffmpeg \\
        build-essential \\
        python3 \\
        tzdata \\
        zip \\
        unzip \\
        iproute2 \\
    && apt-get clean \\
    && rm -rf /var/lib/apt/lists/*

RUN useradd -d /home/container -m container

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER container
ENV USER=container HOME=/home/container
WORKDIR /home/container

CMD ["/bin/bash", "/entrypoint.sh"]
"""

def make_python_dockerfile(ver):
    return f"""FROM --platform=$TARGETOS/$TARGETARCH python:{ver}-slim

LABEL author="diaww.dev" maintainer="ferdiazprasida@gmail.com"
LABEL org.opencontainers.image.source="https://github.com/DIAWWDEV/yolks"

RUN if [ -f /etc/apt/sources.list ]; then \\
        if grep -q 'Debian GNU/Linux 10' /etc/issue 2>/dev/null || grep -q 'buster' /etc/apt/sources.list 2>/dev/null; then \\
            sed -i 's|deb.debian.org/debian|archive.debian.org/debian|g' /etc/apt/sources.list && \\
            sed -i 's|security.debian.org/debian-security|archive.debian.org/debian-security|g' /etc/apt/sources.list && \\
            sed -i '/buster-updates/d' /etc/apt/sources.list ; \\
        elif grep -q 'Debian GNU/Linux 9' /etc/issue 2>/dev/null || grep -q 'stretch' /etc/apt/sources.list 2>/dev/null; then \\
            sed -i 's|deb.debian.org/debian|archive.debian.org/debian|g' /etc/apt/sources.list && \\
            sed -i 's|security.debian.org|archive.debian.org|g' /etc/apt/sources.list && \\
            sed -i '/stretch-updates/d' /etc/apt/sources.list ; \\
        fi ; \\
    fi \\
    && apt-get update --allow-releaseinfo-change \\
    && apt-get install -y --no-install-recommends \\
        ca-certificates \\
        curl \\
        git \\
        ffmpeg \\
        build-essential \\
        tzdata \\
        zip \\
        unzip \\
        iproute2 \\
    && apt-get clean \\
    && rm -rf /var/lib/apt/lists/*

RUN useradd -d /home/container -m container

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER container
ENV USER=container HOME=/home/container
WORKDIR /home/container

CMD ["/bin/bash", "/entrypoint.sh"]
"""

node_entrypoint = """#!/bin/bash
cd /home/container

# Output Current IP
INTERNAL_IP=$(ip route get 1 | awk '{print $(NF-2);exit}')
export INTERNAL_IP

# Branding Banner
echo -e "\\033[1;36m====================================================\\033[0m"
echo -e "\\033[1;37m  ⚡ RUNTIME CONTAINER BY \\033[1;35mDIAWW.DEV\\033[0m"
echo -e "\\033[0;37m  🌐 Web: https://diaww.my.id | ✉️ ferdiazprasida@gmail.com\\033[0m"
echo -e "\\033[1;36m====================================================\\033[0m"

# Display Runtime Version
node -v
npm -v

# Convert Pterodactyl {{VARIABLE}} into ${VARIABLE}
MODIFIED_STARTUP=$(echo -e "${STARTUP}" | sed -e 's/{{/${/g' -e 's/}}/}/g')
echo -e "diaww.dev:/home/container$ ${MODIFIED_STARTUP}"

# Run the Server
eval ${MODIFIED_STARTUP}
"""

python_entrypoint = """#!/bin/bash
cd /home/container

# Output Current IP
INTERNAL_IP=$(ip route get 1 | awk '{print $(NF-2);exit}')
export INTERNAL_IP

# Branding Banner
echo -e "\\033[1;36m====================================================\\033[0m"
echo -e "\\033[1;37m  ⚡ RUNTIME CONTAINER BY \\033[1;35mDIAWW.DEV\\033[0m"
echo -e "\\033[0;37m  🌐 Web: https://diaww.my.id | ✉️ ferdiazprasida@gmail.com\\033[0m"
echo -e "\\033[1;36m====================================================\\033[0m"

# Display Runtime Version
python --version
pip --version

# Convert Pterodactyl {{VARIABLE}} into ${VARIABLE}
MODIFIED_STARTUP=$(echo -e "${STARTUP}" | sed -e 's/{{/${/g' -e 's/}}/}/g')
echo -e "diaww.dev:/home/container$ ${MODIFIED_STARTUP}"

# Run the Server
eval ${MODIFIED_STARTUP}
"""

print("Generating files...")

# Write Node.js directories and files
for ver in node_versions:
    dir_path = os.path.join(base_dir, "nodejs", ver)
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, "Dockerfile"), "w", newline="\n", encoding="utf-8") as f:
        f.write(make_node_dockerfile(ver))
    with open(os.path.join(dir_path, "entrypoint.sh"), "w", newline="\n", encoding="utf-8") as f:
        f.write(node_entrypoint)
    print(f"Created nodejs/{ver}")

# Write Python directories and files
for ver in python_versions:
    dir_path = os.path.join(base_dir, "python", ver)
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, "Dockerfile"), "w", newline="\n", encoding="utf-8") as f:
        f.write(make_python_dockerfile(ver))
    with open(os.path.join(dir_path, "entrypoint.sh"), "w", newline="\n", encoding="utf-8") as f:
        f.write(python_entrypoint)
    print(f"Created python/{ver}")

print("Done generating Dockerfile and entrypoints!")

