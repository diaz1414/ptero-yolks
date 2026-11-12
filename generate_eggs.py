import json
import os

eggs_dir = r"c:\diaz\egg python&nodejs\eggs"
os.makedirs(eggs_dir, exist_ok=True)

# 1. Node.js Generic Egg
nodejs_egg = {
    "_comment": "DO NOT EDIT: FILE GENERATED AUTOMATICALLY BY PTERODACTYL PANEL - PTDL_v2",
    "meta": {
        "version": "PTDL_v2",
        "update_url": None
    },
    "exported_at": "2026-11-13T02:18:00+07:00",
    "name": "Node.js Generic (diaww.dev)",
    "author": "ferdiazprasida@gmail.com",
    "description": "Custom high-performance generic Node.js & TypeScript egg by diaww.dev (parkervcp style). Supports Node.js 14 to 26, custom/optional package.json, auto git pull, auto dependency install, ts-node support, and full variable compatibility.",
    "features": None,
    "docker_images": {
        "Node.js 26 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_26",
        "Node.js 25 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_25",
        "Node.js 24 (LTS) (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_24",
        "Node.js 23 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_23",
        "Node.js 22 (LTS) (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_22",
        "Node.js 21 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_21",
        "Node.js 20 (LTS) (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_20",
        "Node.js 19 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_19",
        "Node.js 18 (LTS) (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_18",
        "Node.js 17 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_17",
        "Node.js 16 (LTS) (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_16",
        "Node.js 15 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_15",
        "Node.js 14 (LTS) (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:nodejs_14"
    },
    "file_denylist": [],
    "startup": "echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Initializing Node.js runtime environment...\"; if [[ -d .git ]] && [[ \"{{AUTO_UPDATE}}\" == \"1\" ]]; then echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Updating repository via git pull...\"; git pull; fi; if [[ ! -z \"{{NODE_PACKAGES}}\" ]]; then echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Installing extra packages ({{NODE_PACKAGES}})...\"; /usr/local/bin/npm install {{NODE_PACKAGES}}; fi; if [[ ! -z \"{{UNNODE_PACKAGES}}\" ]]; then echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Uninstalling packages ({{UNNODE_PACKAGES}})...\"; /usr/local/bin/npm uninstall {{UNNODE_PACKAGES}}; fi; PKG_FILE=\"{{PACKAGE_FILE}}\"; if [ -z \"${PKG_FILE}\" ]; then PKG_FILE=\"package.json\"; fi; if [ -f \"/home/container/${PKG_FILE}\" ]; then echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Installing dependencies from ${PKG_FILE}...\"; if [ \"${PKG_FILE}\" != \"package.json\" ]; then cp \"/home/container/${PKG_FILE}\" /home/container/package.json 2>/dev/null || true; fi; /usr/local/bin/npm install; fi; if [[ \"${MAIN_FILE}\" == *.js ]]; then echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Booting application via node {{MAIN_FILE}}...\"; /usr/local/bin/node \"/home/container/{{MAIN_FILE}}\" {{NODE_ARGS}}; else echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Booting TypeScript application via ts-node {{MAIN_FILE}}...\"; /usr/local/bin/ts-node --esm \"/home/container/{{MAIN_FILE}}\" {{NODE_ARGS}}; fi",
    "config": {
        "files": "{}",
        "startup": "{\r\n    \"done\": \"diaww.dev\"\r\n}",
        "stop": "^^C",
        "logs": "{}",
        "file_denylist": []
    },
    "scripts": {
        "installation": {
            "script": "#!/bin/bash\n# DIAWW.DEV - Pterodactyl Node.js Installation Script\n\napt update -y\napt install -y git curl ca-certificates\n\nmkdir -p /mnt/server\ncd /mnt/server\n\nif [ \"${USER_UPLOAD}\" == \"true\" ] || [ \"${USER_UPLOAD}\" == \"1\" ]; then\n    echo -e \"\\033[1;33m[DIAWW.DEV]\\033[0m USER_UPLOAD enabled. Skipping git clone.\"\n    exit 0\nfi\n\nif [ -z \"${GIT_ADDRESS}\" ]; then\n    echo -e \"\\033[1;33m[DIAWW.DEV]\\033[0m No GIT_ADDRESS specified. Creating default index.js...\"\n    if [ ! -f index.js ]; then\n        cat << 'EOF' > index.js\nconsole.log(\"[DIAWW.DEV] Node.js container is up and running!\");\nsetInterval(() => {\n    console.log(\"[DIAWW.DEV] Server heartbeat tick: \" + new Date().toISOString());\n}, 30000);\nEOF\n    fi\n    exit 0\nfi\n\nGIT_TARGET=\"${GIT_ADDRESS}\"\nif [ ! -z \"${GIT_USERNAME}\" ] && [ ! -z \"${GIT_ACCESS_TOKEN}\" ]; then\n    GIT_TARGET=\"https://${GIT_USERNAME}:${GIT_ACCESS_TOKEN}@$(echo -e ${GIT_ADDRESS} | cut -d/ -f3-)\"\nfi\n\necho -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Cloning repository from ${GIT_ADDRESS}...\"\nif [ -z \"${BRANCH}\" ]; then\n    git clone ${GIT_TARGET} .\nelse\n    git clone --single-branch --branch ${BRANCH} ${GIT_TARGET} .\nfi\n\nPKG_TARGET=\"${PACKAGE_FILE}\"\nif [ -z \"${PKG_TARGET}\" ]; then PKG_TARGET=\"package.json\"; fi\nif [ -f \"${PKG_TARGET}\" ]; then\n    echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Installing dependencies from ${PKG_TARGET}...\"\n    npm install\nfi\n\necho -e \"\\033[1;32m[DIAWW.DEV]\\033[0m Installation complete!\"",
            "container": "node:22-slim",
            "entrypoint": "bash"
        }
    },
    "variables": [
        {
            "name": "Main Application File",
            "description": "The entrypoint file to run with Node.js or ts-node (e.g. index.js or index.ts).",
            "env_variable": "MAIN_FILE",
            "default_value": "index.js",
            "user_viewable": True,
            "user_editable": True,
            "rules": "required|string|max:100",
            "field_type": "text"
        },
        {
            "name": "Package JSON File (Optional)",
            "description": "The package configuration file to install dependencies from (defaults to package.json). Optional: if file does not exist, it will be skipped safely.",
            "env_variable": "PACKAGE_FILE",
            "default_value": "package.json",
            "user_viewable": True,
            "user_editable": True,
            "rules": "nullable|string|max:100",
            "field_type": "text"
        },
        {
            "name": "Auto Update",
            "description": "Automatically perform a 'git pull' on every container start if a .git repository exists.",
            "env_variable": "AUTO_UPDATE",
            "default_value": "0",
            "user_viewable": True,
            "user_editable": True,
            "rules": "required|boolean",
            "field_type": "text"
        },
        {
            "name": "Additional Node.js Arguments",
            "description": "Additional CLI arguments or flags passed to the Node.js / ts-node process.",
            "env_variable": "NODE_ARGS",
            "default_value": "",
            "user_viewable": True,
            "user_editable": True,
            "rules": "nullable|string",
            "field_type": "text"
        },
        {
            "name": "Additional NPM Packages",
            "description": "Space-separated list of extra NPM packages to install automatically on startup without modifying package.json.",
            "env_variable": "NODE_PACKAGES",
            "default_value": "",
            "user_viewable": True,
            "user_editable": True,
            "rules": "nullable|string",
            "field_type": "text"
        },
        {
            "name": "Uninstalled NPM Packages",
            "description": "Space-separated list of NPM packages to uninstall on startup.",
            "env_variable": "UNNODE_PACKAGES",
            "default_value": "",
            "user_viewable": True,
            "user_editable": True,
            "rules": "nullable|string",
            "field_type": "text"
        },
        {
            "name": "Git Repository Address",
            "description": "Git repository URL to clone during initial server setup (e.g., https://github.com/user/repo.git).",
            "env_variable": "GIT_ADDRESS",
            "default_value": "",
            "user_viewable": True,
            "user_editable": True,
            "rules": "nullable|string",
            "field_type": "text"
        },
        {
            "name": "Git Branch",
            "description": "Specific Git branch to clone during setup (leave blank for default branch).",
            "env_variable": "BRANCH",
            "default_value": "",
            "user_viewable": True,
            "user_editable": True,
            "rules": "nullable|string",
            "field_type": "text"
        },
        {
            "name": "User Upload Only",
            "description": "Set to 1 or true if you upload files manually via SFTP instead of cloning a Git repository.",
            "env_variable": "USER_UPLOAD",
            "default_value": "0",
            "user_viewable": True,
            "user_editable": True,
            "rules": "required|boolean",
            "field_type": "text"
        }
    ]
}

# 2. Python Generic Egg
python_egg = {
    "_comment": "DO NOT EDIT: FILE GENERATED AUTOMATICALLY BY PTERODACTYL PANEL - PTDL_v2",
    "meta": {
        "version": "PTDL_v2",
        "update_url": None
    },
    "exported_at": "2026-11-13T02:18:00+07:00",
    "name": "Python Generic (diaww.dev)",
    "author": "ferdiazprasida@gmail.com",
    "description": "Custom high-performance generic Python egg by diaww.dev (parkervcp style). Supports Python 2.7 and 3.7 to 3.15, custom/optional requirements.txt, auto git pull, auto dependency install, and full variable compatibility.",
    "features": None,
    "docker_images": {
        "Python 3.15 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:python_3.15",
        "Python 3.14 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:python_3.14",
        "Python 3.13 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:python_3.13",
        "Python 3.12 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:python_3.12",
        "Python 3.11 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:python_3.11",
        "Python 3.10 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:python_3.10",
        "Python 3.9 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:python_3.9",
        "Python 3.8 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:python_3.8",
        "Python 3.7 (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:python_3.7",
        "Python 2.7 (Legacy) (diaww.dev)": "ghcr.io/diaz1414/ptero-yolks:python_2.7"
    },
    "file_denylist": [],
    "startup": "echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Initializing Python runtime environment...\"; if [[ -d .git ]] && [[ \"{{AUTO_UPDATE}}\" == \"1\" ]]; then echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Updating repository via git pull...\"; git pull; fi; if [[ ! -z \"{{PY_PACKAGES}}\" ]]; then echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Installing extra packages ({{PY_PACKAGES}})...\"; pip install -U --no-cache-dir {{PY_PACKAGES}}; fi; if [[ ! -z \"{{UNPY_PACKAGES}}\" ]]; then echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Uninstalling packages ({{UNPY_PACKAGES}})...\"; pip uninstall -y {{UNPY_PACKAGES}}; fi; REQ_FILE=\"{{REQUIREMENTS_FILE}}\"; if [ -z \"${REQ_FILE}\" ]; then REQ_FILE=\"requirements.txt\"; fi; if [ -f \"/home/container/${REQ_FILE}\" ]; then echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Installing dependencies from ${REQ_FILE}...\"; pip install -U --no-cache-dir -r \"/home/container/${REQ_FILE}\"; fi; echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Booting application via python {{PY_FILE}}...\"; /usr/local/bin/python \"/home/container/{{PY_FILE}}\" {{PY_ARGS}}",
    "config": {
        "files": "{}",
        "startup": "{\r\n    \"done\": \"diaww.dev\"\r\n}",
        "stop": "^^C",
        "logs": "{}",
        "file_denylist": []
    },
    "scripts": {
        "installation": {
            "script": "#!/bin/bash\n# DIAWW.DEV - Pterodactyl Python Installation Script\n\napt update -y\napt install -y git curl ca-certificates python3 python3-pip\n\nmkdir -p /mnt/server\ncd /mnt/server\n\nif [ \"${USER_UPLOAD}\" == \"true\" ] || [ \"${USER_UPLOAD}\" == \"1\" ]; then\n    echo -e \"\\033[1;33m[DIAWW.DEV]\\033[0m USER_UPLOAD enabled. Skipping git clone.\"\n    exit 0\nfi\n\nif [ -z \"${GIT_ADDRESS}\" ]; then\n    echo -e \"\\033[1;33m[DIAWW.DEV]\\033[0m No GIT_ADDRESS specified. Creating default main.py...\"\n    if [ ! -f main.py ]; then\n        cat << 'EOF' > main.py\nimport time\nfrom datetime import datetime\n\nprint(\"[DIAWW.DEV] Python container is up and running!\")\nwhile True:\n    print(f\"[DIAWW.DEV] Server heartbeat tick: {datetime.utcnow().isoformat()}\")\n    time.sleep(30)\nEOF\n    fi\n    exit 0\nfi\n\nGIT_TARGET=\"${GIT_ADDRESS}\"\nif [ ! -z \"${GIT_USERNAME}\" ] && [ ! -z \"${GIT_ACCESS_TOKEN}\" ]; then\n    GIT_TARGET=\"https://${GIT_USERNAME}:${GIT_ACCESS_TOKEN}@$(echo -e ${GIT_ADDRESS} | cut -d/ -f3-)\"\nfi\n\necho -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Cloning repository from ${GIT_ADDRESS}...\"\nif [ -z \"${BRANCH}\" ]; then\n    git clone ${GIT_TARGET} .\nelse\n    git clone --single-branch --branch ${BRANCH} ${GIT_TARGET} .\nfi\n\nREQ_TARGET=\"${REQUIREMENTS_FILE}\"\nif [ -z \"${REQ_TARGET}\" ]; then REQ_TARGET=\"requirements.txt\"; fi\nif [ -f \"${REQ_TARGET}\" ]; then\n    echo -e \"\\033[1;36m[DIAWW.DEV]\\033[0m Installing dependencies from ${REQ_TARGET}...\"\n    pip install -U --no-cache-dir -r \"${REQ_TARGET}\"\nfi\n\necho -e \"\\033[1;32m[DIAWW.DEV]\\033[0m Installation complete!\"",
            "container": "python:3.12-slim",
            "entrypoint": "bash"
        }
    },
    "variables": [
        {
            "name": "Main Application File",
            "description": "The entrypoint Python file to execute (e.g. main.py or app.py).",
            "env_variable": "PY_FILE",
            "default_value": "main.py",
            "user_viewable": True,
            "user_editable": True,
            "rules": "required|string|max:100",
            "field_type": "text"
        },
        {
            "name": "Requirements File (Optional)",
            "description": "The requirements file to install Python dependencies from (defaults to requirements.txt). Optional: if file does not exist, it will be skipped safely.",
            "env_variable": "REQUIREMENTS_FILE",
            "default_value": "requirements.txt",
            "user_viewable": True,
            "user_editable": True,
            "rules": "nullable|string|max:100",
            "field_type": "text"
        },
        {
            "name": "Auto Update",
            "description": "Automatically perform a 'git pull' on every container start if a .git repository exists.",
            "env_variable": "AUTO_UPDATE",
            "default_value": "0",
            "user_viewable": True,
            "user_editable": True,
            "rules": "required|boolean",
            "field_type": "text"
        },
        {
            "name": "Additional Python Arguments",
            "description": "Additional CLI arguments or flags passed to the Python process.",
            "env_variable": "PY_ARGS",
            "default_value": "",
            "user_viewable": True,
            "user_editable": True,
            "rules": "nullable|string",
            "field_type": "text"
        },
        {
            "name": "Additional Pip Packages",
            "description": "Space-separated list of extra pip packages to install automatically on startup without modifying requirements.txt.",
            "env_variable": "PY_PACKAGES",
            "default_value": "",
            "user_viewable": True,
            "user_editable": True,
            "rules": "nullable|string",
            "field_type": "text"
        },
        {
            "name": "Uninstalled Pip Packages",
            "description": "Space-separated list of pip packages to uninstall on startup.",
            "env_variable": "UNPY_PACKAGES",
            "default_value": "",
            "user_viewable": True,
            "user_editable": True,
            "rules": "nullable|string",
            "field_type": "text"
        },
        {
            "name": "Git Repository Address",
            "description": "Git repository URL to clone during initial server setup (e.g., https://github.com/user/repo.git).",
            "env_variable": "GIT_ADDRESS",
            "default_value": "",
            "user_viewable": True,
            "user_editable": True,
            "rules": "nullable|string",
            "field_type": "text"
        },
        {
            "name": "Git Branch",
            "description": "Specific Git branch to clone during setup (leave blank for default branch).",
            "env_variable": "BRANCH",
            "default_value": "",
            "user_viewable": True,
            "user_editable": True,
            "rules": "nullable|string",
            "field_type": "text"
        },
        {
            "name": "User Upload Only",
            "description": "Set to 1 or true if you upload files manually via SFTP instead of cloning a Git repository.",
            "env_variable": "USER_UPLOAD",
            "default_value": "0",
            "user_viewable": True,
            "user_editable": True,
            "rules": "required|boolean",
            "field_type": "text"
        }
    ]
}

# Write eggs
with open(os.path.join(eggs_dir, "egg-nodejs-generic.json"), "w", encoding="utf-8") as f:
    json.dump(nodejs_egg, f, indent=4)
print("Updated egg-nodejs-generic.json with PACKAGE_FILE variable")

with open(os.path.join(eggs_dir, "egg-python-generic.json"), "w", encoding="utf-8") as f:
    json.dump(python_egg, f, indent=4)
print("Updated egg-python-generic.json with REQUIREMENTS_FILE variable")
