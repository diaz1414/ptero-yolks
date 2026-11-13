#!/bin/bash
cd /home/container

# Output Current IP
INTERNAL_IP=$(ip route get 1 | awk '{print $(NF-2);exit}')
export INTERNAL_IP

# Branding Banner
echo -e "\033[1;36m====================================================\033[0m"
echo -e "\033[1;37m  ⚡ RUNTIME CONTAINER BY \033[1;35mDIAWW.DEV\033[0m"
echo -e "\033[0;37m  🌐 Web: https://diaww.my.id | ✉️ ferdiazprasida@gmail.com\033[0m"
echo -e "\033[1;36m====================================================\033[0m"

# Display Runtime Version
bun -v

# Convert Pterodactyl {{VARIABLE}} into ${VARIABLE}
MODIFIED_STARTUP=$(echo -e "${STARTUP}" | sed -e 's/{{/${/g' -e 's/}}/}/g')
echo -e "diaww.dev:/home/container$ ${MODIFIED_STARTUP}"

# Run the Server
eval ${MODIFIED_STARTUP}
