<div align="center">

# ⚡ DIAWW.DEV Ptero-Yolks

**High-Performance Custom Docker Images for Pterodactyl Panel**

[![GitHub Actions Build](https://img.shields.io/badge/GitHub_Actions-Automated_Build-blue?logo=githubactions&logoColor=white)](https://github.com/diaz1414/ptero-yolks/actions)
[![Registry](https://img.shields.io/badge/GHCR-ghcr.io%2Fdiaz1414%2Fptero--yolks-2ea44f?logo=docker&logoColor=white)](https://github.com/diaz1414/ptero-yolks/pkgs/container/ptero-yolks)
[![Maintainer](https://img.shields.io/badge/Maintainer-ferdiazprasida%40gmail.com-blueviolet?logo=gmail&logoColor=white)](mailto:ferdiazprasida@gmail.com)
[![Website](https://img.shields.io/badge/Website-diaww.my.id-orange)](https://diaww.my.id)
[![Architecture](https://img.shields.io/badge/Architecture-linux%2Famd64-success)](#)

</div>

---

## 📖 Ringkasan

Repository **`ptero-yolks`** menyediakan koleksi custom Docker images dan Pterodactyl Generic Eggs siap pakai yang dioptimalkan khusus untuk menjalankan berbagai bot Discord, aplikasi web, microservices, dan skrip berbasis **Node.js**, **Python**, dan **Bun** di **Pterodactyl Panel**.

Semua image dibangun di atas basis resmi Docker Hub Debian slim paling stabil (`-slim` / `-debian`), arsitektur native `linux/amd64` (sangat cepat di-build), dilengkapi paket esensial (`ffmpeg`, `imagemagick`, `git`, `curl`, `build-essential`, `python3` untuk node-gyp, `typescript`, `ts-node`, `iproute2`, `zip/unzip`).

- **Brand:** `diaww.dev` ([https://diaww.my.id](https://diaww.my.id))
- **Maintainer:** `ferdiazprasida@gmail.com`
- **GitHub Repository:** [https://github.com/diaz1414/ptero-yolks](https://github.com/diaz1414/ptero-yolks)
- **Container Registry:** `ghcr.io/diaz1414/ptero-yolks:<tag>`

---

## 📦 Daftar Image Aktif (23 Images)

Semua image dapat ditarik langsung melalui GitHub Container Registry (GHCR):

### 🥟 Bun Runtimes (5 Images Cepat)

| Versi | Docker Hub Base | Tag GHCR | Arsitektur | Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| **Bun Latest** | `oven/bun:debian` | `ghcr.io/diaz1414/ptero-yolks:bun_latest` | `linux/amd64` | Production Default / Latest Stable |
| **Bun 1.3** | `oven/bun:1.3-debian` | `ghcr.io/diaz1414/ptero-yolks:bun_1.3` | `linux/amd64` | Fullstack Dev + Bun.SQL |
| **Bun 1.2** | `oven/bun:1.2-debian` | `ghcr.io/diaz1414/ptero-yolks:bun_1.2` | `linux/amd64` | Stable Release |
| **Bun 1.1** | `oven/bun:1.1-debian` | `ghcr.io/diaz1414/ptero-yolks:bun_1.1` | `linux/amd64` | Maintenance / LTS |
| **Bun Canary** | `oven/bun:canary-debian` | `ghcr.io/diaz1414/ptero-yolks:bun_canary` | `linux/amd64` | Bleeding Edge / Nightly |

### 🟢 Node.js Runtimes (8 Images Modern)

| Versi | Docker Hub Base | Tag GHCR | Arsitektur | Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| **Node.js 26** | `node:26-slim` | `ghcr.io/diaz1414/ptero-yolks:nodejs_26` | `linux/amd64` | Future / Next-Gen |
| **Node.js 25** | `node:25-slim` | `ghcr.io/diaz1414/ptero-yolks:nodejs_25` | `linux/amd64` | Current / Latest |
| **Node.js 24** | `node:24-slim` | `ghcr.io/diaz1414/ptero-yolks:nodejs_24` | `linux/amd64` | Active LTS |
| **Node.js 23** | `node:23-slim` | `ghcr.io/diaz1414/ptero-yolks:nodejs_23` | `linux/amd64` | Current Release |
| **Node.js 22** | `node:22-slim` | `ghcr.io/diaz1414/ptero-yolks:nodejs_22` | `linux/amd64` | Active LTS (Rekomendasi) |
| **Node.js 21** | `node:21-slim` | `ghcr.io/diaz1414/ptero-yolks:nodejs_21` | `linux/amd64` | Stable Release |
| **Node.js 20** | `node:20-slim` | `ghcr.io/diaz1414/ptero-yolks:nodejs_20` | `linux/amd64` | Maintenance LTS |
| **Node.js 18** | `node:18-slim` | `ghcr.io/diaz1414/ptero-yolks:nodejs_18` | `linux/amd64` | Maintenance LTS |

### 🐍 Python Runtimes (10 Images)

| Versi | Docker Hub Base | Tag GHCR | Arsitektur | Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| **Python 3.15** | `python:3.15-slim` | `ghcr.io/diaz1414/ptero-yolks:python_3.15` | `linux/amd64` | Future / Experimental |
| **Python 3.14** | `python:3.14-slim` | `ghcr.io/diaz1414/ptero-yolks:python_3.14` | `linux/amd64` | Development |
| **Python 3.13** | `python:3.13-slim` | `ghcr.io/diaz1414/ptero-yolks:python_3.13` | `linux/amd64` | Latest Stable |
| **Python 3.12** | `python:3.12-slim` | `ghcr.io/diaz1414/ptero-yolks:python_3.12` | `linux/amd64` | Stable / Rekomendasi |
| **Python 3.11** | `python:3.11-slim` | `ghcr.io/diaz1414/ptero-yolks:python_3.11` | `linux/amd64` | Stable |
| **Python 3.10** | `python:3.10-slim` | `ghcr.io/diaz1414/ptero-yolks:python_3.10` | `linux/amd64` | Stable |
| **Python 3.9** | `python:3.9-slim` | `ghcr.io/diaz1414/ptero-yolks:python_3.9` | `linux/amd64` | Security Support |
| **Python 3.8** | `python:3.8-slim` | `ghcr.io/diaz1414/ptero-yolks:python_3.8` | `linux/amd64` | Security Support |
| **Python 3.7** | `python:3.7-slim` | `ghcr.io/diaz1414/ptero-yolks:python_3.7` | `linux/amd64` | Legacy Python 3 |
| **Python 2.7** | `python:2.7-slim` | `ghcr.io/diaz1414/ptero-yolks:python_2.7` | `linux/amd64` | Legacy Python 2 |

---

## 🗂️ Struktur Direktori Repository

```text
.
├── .github/
│   └── workflows/
│       └── build-yolks.yml         # Matrix workflow build & push 23 image otomatis ke GHCR
├── eggs/
│   ├── egg-bun.json                # Pterodactyl Egg PTDL_v2 untuk Bun (1.1, 1.2, 1.3, Latest, Canary)
│   ├── egg-nodejs-generic.json     # Pterodactyl Egg PTDL_v2 untuk Node.js (18 s/d 26)
│   └── egg-python-generic.json     # Pterodactyl Egg PTDL_v2 untuk Python (2.7, 3.7 s/d 3.15)
├── bun/
│   ├── 1.1/     (Dockerfile, entrypoint.sh)
│   ├── 1.2/     (Dockerfile, entrypoint.sh)
│   ├── 1.3/     (Dockerfile, entrypoint.sh)
│   ├── latest/  (Dockerfile, entrypoint.sh)
│   └── canary/  (Dockerfile, entrypoint.sh)
├── nodejs/
│   ├── 18/  (Dockerfile, entrypoint.sh)
│   ├── 20/  (Dockerfile, entrypoint.sh)
│   ├── 21/  (Dockerfile, entrypoint.sh)
│   ├── 22/  (Dockerfile, entrypoint.sh)
│   ├── 23/  (Dockerfile, entrypoint.sh)
│   ├── 24/  (Dockerfile, entrypoint.sh)
│   ├── 25/  (Dockerfile, entrypoint.sh)
│   └── 26/  (Dockerfile, entrypoint.sh)
├── python/
│   ├── 2.7/  (Dockerfile, entrypoint.sh)
│   ├── 3.7/  (Dockerfile, entrypoint.sh)
│   ├── 3.8/  (Dockerfile, entrypoint.sh)
│   ├── 3.9/  (Dockerfile, entrypoint.sh)
│   ├── 3.10/ (Dockerfile, entrypoint.sh)
│   ├── 3.11/ (Dockerfile, entrypoint.sh)
│   ├── 3.12/ (Dockerfile, entrypoint.sh)
│   ├── 3.13/ (Dockerfile, entrypoint.sh)
│   ├── 3.14/ (Dockerfile, entrypoint.sh)
│   └── 3.15/ (Dockerfile, entrypoint.sh)
├── .gitattributes
├── .gitignore
└── README.md
```

---

## 📥 Cara Impor Egg JSON ke Pterodactyl Panel

1. **Unduh File Egg:**
   Unduh file yang Anda butuhkan dari folder `eggs/`:
   - [eggs/egg-bun.json](eggs/egg-bun.json) (untuk Bun Runtime)
   - [eggs/egg-nodejs-generic.json](eggs/egg-nodejs-generic.json) (untuk Node.js)
   - [eggs/egg-python-generic.json](eggs/egg-python-generic.json) (untuk Python)
2. **Buka Admin Panel Pterodactyl:**
   Login ke Pterodactyl Panel Anda dengan akun Administrator.
3. **Masuk ke Pengaturan Nests:**
   Pada menu navigasi samping, klik **Nests** (`/admin/nests`).
4. **Pilih Nest Tujuan:**
   Pilih Nest yang sudah ada atau buat Nest baru.
5. **Klik Tombol Import Egg:**
   Di halaman detail Nest, klik tombol biru **Import Egg**.
6. **Unggah File:**
   - Pilih file `egg-bun.json`, `egg-nodejs-generic.json`, atau `egg-python-generic.json`.
   - Pilih Nest yang dituju.
   - Klik **Import**.
7. **Pilih Versi Docker Image di Server:**
   - Di tab **Startup** server, pilih dropdown **Docker Image** sesuai versi yang Anda inginkan (misal Bun Latest/1.3/1.2/1.1/Canary, Node.js 22, atau Python 3.12).

---

## 📞 Dukungan & Kontak

- **Maintainer:** Ferdiaz Prasida
- **Email:** [ferdiazprasida@gmail.com](mailto:ferdiazprasida@gmail.com)
- **Website:** [https://diaww.my.id](https://diaww.my.id)
- **GitHub:** [@diaz1414](https://github.com/diaz1414)

---

<div align="center">
  <sub>Dibuat dengan ❤️ dan standar rekayasa terbaik untuk komunitas Pterodactyl Panel oleh <b>diaww.dev</b></sub>
</div>
