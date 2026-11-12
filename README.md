<div align="center">

# ⚡ DIAWW.DEV Yolks

**High-Performance Custom Docker Images for Pterodactyl Panel**

[![GitHub Actions Build](https://img.shields.io/badge/GitHub_Actions-Automated_Build-blue?logo=githubactions&logoColor=white)](https://github.com/DIAWWDEV/yolks/actions)
[![Registry](https://img.shields.io/badge/GHCR-ghcr.io%2FDIAWWDEV%2Fyolks-2ea44f?logo=docker&logoColor=white)](https://github.com/DIAWWDEV/yolks/pkgs/container/yolks)
[![Maintainer](https://img.shields.io/badge/Maintainer-ferdiazprasida%40gmail.com-blueviolet?logo=gmail&logoColor=white)](mailto:ferdiazprasida@gmail.com)
[![Website](https://img.shields.io/badge/Website-diaww.my.id-orange)](https://diaww.my.id)
[![Architecture](https://img.shields.io/badge/Architectures-amd64%20%7C%20arm64-success)](#)

</div>

---

## 📖 Ringkasan

Repository **`yolks`** ini menyediakan koleksi custom Docker images dan Pterodactyl Generic Eggs siap pakai yang dioptimalkan khusus untuk menjalankan berbagai bot Discord, aplikasi web, microservices, dan skrip berbasis **Node.js** dan **Python** di **Pterodactyl Panel**.

Semua image dibangun di atas basis resmi Docker Hub Debian slim paling stabil (`-slim`), multi-arsitektur (`linux/amd64` dan `linux/arm64`), dilengkapi paket esensial (`ffmpeg`, `git`, `curl`, `build-essential`, `python3` untuk node-gyp, `iproute2`, `zip/unzip`), serta sistem penanganan repositori arsip otomatis untuk rilis legacy (seperti Debian Buster/Stretch).

- **Brand:** `diaww.dev` ([https://diaww.my.id](https://diaww.my.id))
- **Maintainer:** `ferdiazprasida@gmail.com`
- **GitHub Repository:** [https://github.com/DIAWWDEV/yolks](https://github.com/DIAWWDEV/yolks)
- **Container Registry:** `ghcr.io/DIAWWDEV/yolks:<tag>`

---

## 📦 Daftar Lengkap 23 Docker Image

Semua image dapat ditarik langsung melalui GitHub Container Registry (GHCR):

### 🟢 Node.js Runtimes (13 Images)

| Versi | Docker Hub Base | Tag GHCR | Arsitektur | Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| **Node.js 26** | `node:26-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_26` | `amd64`, `arm64` | Future / Next-Gen |
| **Node.js 25** | `node:25-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_25` | `amd64`, `arm64` | Current / Latest |
| **Node.js 24** | `node:24-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_24` | `amd64`, `arm64` | Active LTS |
| **Node.js 23** | `node:23-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_23` | `amd64`, `arm64` | Odd Release |
| **Node.js 22** | `node:22-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_22` | `amd64`, `arm64` | Active LTS |
| **Node.js 21** | `node:21-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_21` | `amd64`, `arm64` | Odd Release |
| **Node.js 20** | `node:20-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_20` | `amd64`, `arm64` | Maintenance LTS |
| **Node.js 19** | `node:19-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_19` | `amd64`, `arm64` | Odd Release |
| **Node.js 18** | `node:18-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_18` | `amd64`, `arm64` | Maintenance LTS |
| **Node.js 17** | `node:17-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_17` | `amd64`, `arm64` | Odd Release |
| **Node.js 16** | `node:16-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_16` | `amd64`, `arm64` | Legacy LTS |
| **Node.js 15** | `node:15-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_15` | `amd64`, `arm64` | Legacy Archive |
| **Node.js 14** | `node:14-slim` | `ghcr.io/DIAWWDEV/yolks:nodejs_14` | `amd64`, `arm64` | Legacy Archive |

### 🐍 Python Runtimes (10 Images)

| Versi | Docker Hub Base | Tag GHCR | Arsitektur | Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| **Python 3.15** | `python:3.15-slim` | `ghcr.io/DIAWWDEV/yolks:python_3.15` | `amd64`, `arm64` | Future / Experimental |
| **Python 3.14** | `python:3.14-slim` | `ghcr.io/DIAWWDEV/yolks:python_3.14` | `amd64`, `arm64` | Pre-Release / Development |
| **Python 3.13** | `python:3.13-slim` | `ghcr.io/DIAWWDEV/yolks:python_3.13` | `amd64`, `arm64` | Latest Stable |
| **Python 3.12** | `python:3.12-slim` | `ghcr.io/DIAWWDEV/yolks:python_3.12` | `amd64`, `arm64` | Stable / Recommended |
| **Python 3.11** | `python:3.11-slim` | `ghcr.io/DIAWWDEV/yolks:python_3.11` | `amd64`, `arm64` | Stable |
| **Python 3.10** | `python:3.10-slim` | `ghcr.io/DIAWWDEV/yolks:python_3.10` | `amd64`, `arm64` | Stable |
| **Python 3.9** | `python:3.9-slim` | `ghcr.io/DIAWWDEV/yolks:python_3.9` | `amd64`, `arm64` | Security Support |
| **Python 3.8** | `python:3.8-slim` | `ghcr.io/DIAWWDEV/yolks:python_3.8` | `amd64`, `arm64` | Security Support |
| **Python 3.7** | `python:3.7-slim` | `ghcr.io/DIAWWDEV/yolks:python_3.7` | `amd64`, `arm64` | Legacy Archive |
| **Python 2.7** | `python:2.7-slim` | `ghcr.io/DIAWWDEV/yolks:python_2.7` | `amd64`, `arm64` | Legacy Python 2 |

---

## 🗂️ Struktur Direktori Repository

```text
.
├── .github/
│   └── workflows/
│       └── build-yolks.yml         # Matrix workflow build & push 23 image otomatis ke GHCR
├── eggs/
│   ├── egg-nodejs-generic.json     # Pterodactyl Egg PTDL_v2 untuk Node.js (14 - 26)
│   └── egg-python-generic.json     # Pterodactyl Egg PTDL_v2 untuk Python (2.7, 3.7 - 3.15)
├── nodejs/
│   ├── 14/  (Dockerfile, entrypoint.sh)
│   ├── 15/  (Dockerfile, entrypoint.sh)
│   ├── 16/  (Dockerfile, entrypoint.sh)
│   ├── 17/  (Dockerfile, entrypoint.sh)
│   ├── 18/  (Dockerfile, entrypoint.sh)
│   ├── 19/  (Dockerfile, entrypoint.sh)
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

## ✨ Fitur Utama Image & Egg

1. **User Non-Root Aman:**
   Semua container berjalan di bawah akun pengguna non-root `container` (`/home/container`), sesuai dengan standar keamanan Pterodactyl Panel.
2. **Paket Bawaan Lengkap:**
   - Multimedia: `ffmpeg`
   - Network & Transfer: `curl`, `ca-certificates`, `iproute2`
   - Development & Kompilasi: `git`, `build-essential`, `python3` (khusus image Node.js untuk `node-gyp`)
   - Arsip & Utilitas: `tzdata`, `zip`, `unzip`
3. **Kompatibilitas Debian Legacy:**
   Deteksi otomatis Debian Buster/Stretch pada rilis legacy (`node:14`, `node:15`, `python:2.7`, `python:3.7`) yang mengalihkan URL repo ke `archive.debian.org` dan menjalankan `apt-get update --allow-releaseinfo-change` sehingga proses build tidak pernah gagal.
4. **Branding Banner Konsol & Logging Bersih:**
   Setiap container saat boot mencetak banner profesional:
   ```text
   ====================================================
     ⚡ RUNTIME CONTAINER BY DIAWW.DEV
     🌐 Web: https://diaww.my.id | ✉️ ferdiazprasida@gmail.com
   ====================================================
   ```
5. **Konversi Variabel Pterodactyl Dinamis:**
   File `entrypoint.sh` secara otomatis mengonversi variabel startup Pterodactyl `{{VARIABLE}}` menjadi format bash `${VARIABLE}` lalu mengeksekusinya dengan log command `diaww.dev:/home/container$ ...`.
6. **Egg PTDL_v2 Otomatis:**
   - Mendukung **Auto Update** (`git pull` otomatis pada saat server dinyalakan).
   - Mendukung **Auto Install** dependensi (`package.json` untuk Node.js, `requirements.txt` untuk Python).
   - Mendukung **Dynamic Extra Packages** (`NODE_PACKAGES` / `PY_PACKAGES`) tanpa perlu mengubah image Docker.
   - Mendukung kustomisasi berkas utama (`MAIN_FILE` / `PY_FILE`) dan argumen tambahan (`ARGS`).

---

## 🔓 Cara Mengubah Visibilitas Package GHCR Menjadi Public

Secara bawaan, GitHub Container Registry (GHCR) membuat package yang baru di-push berstatus **Private**. Agar node Pterodactyl (Wings) dapat menarik (pull) image tanpa kendala autentikasi `unauthorized`, ubah visibilitas package menjadi **Public**:

1. Buka profil akun GitHub atau organisasi Anda di peramban:
   `https://github.com/DIAWWDEV?tab=packages` (atau buka halaman repository `yolks`, lalu klik menu **Packages** di sidebar kanan).
2. Klik package bernama **`yolks`**.
3. Di sebelah kanan atas halaman package, klik tombol **Package settings**.
4. Gulir ke bawah hingga bagian **Danger Zone**.
5. Pada bagian **Change visibility**, klik tombol **Change visibility**.
6. Pilih opsi **Public**, ketik nama package `yolks` untuk konfirmasi, lalu klik **I understand the consequences, change package visibility.**
7. Selesai! Sekarang semua tag `ghcr.io/diawwdev/yolks:...` dapat di-pull oleh server mana pun tanpa login token.

---

## 📥 Cara Impor Egg JSON ke Pterodactyl Panel

1. **Unduh File Egg:**
   Unduh file yang Anda butuhkan dari folder `eggs/`:
   - [eggs/egg-nodejs-generic.json](eggs/egg-nodejs-generic.json) (untuk Node.js)
   - [eggs/egg-python-generic.json](eggs/egg-python-generic.json) (untuk Python)
2. **Buka Admin Panel Pterodactyl:**
   Login ke Pterodactyl Panel Anda dengan akun Administrator.
3. **Masuk ke Pengaturan Nests:**
   Pada menu navigasi samping, klik **Nests** (`/admin/nests`).
4. **Pilih Nest Tujuan:**
   Pilih Nest yang sudah ada (misalnya `Generic` atau `Nodejs/Python`) atau buat Nest baru dengan mengklik **Create New**.
5. **Klik Tombol Import Egg:**
   Di halaman detail Nest, klik tombol biru **Import Egg**.
6. **Unggah File:**
   - Pilih file `egg-nodejs-generic.json` atau `egg-python-generic.json` yang telah diunduh.
   - Pilih Nest yang dituju.
   - Klik **Import**.
7. **Pilih Versi Docker Image di Server:**
   - Saat membuat server baru (atau melalui tab **Startup** pada server yang sudah ada), Anda dapat memilih salah satu dari daftar versi Docker yang telah disediakan di dropdown **Docker Image** (dari Node.js 14 s/d 26, atau Python 2.7 s/d 3.15).

---

## 🚀 Menjalankan Build Manual (Workflow Dispatch)

Jika Anda ingin memicu build ulang seluruh 23 image tanpa melakukan push kode baru:

1. Buka tab **Actions** di repositori GitHub `yolks`:
   `https://github.com/DIAWWDEV/yolks/actions`
2. Klik workflow **Build and Push Yolks** pada daftar di sebelah kiri.
3. Klik tombol **Run workflow** di sebelah kanan atas.
4. Pilih branch `main`, lalu klik **Run workflow**.

GitHub Actions akan menjalankan proses build matrix untuk seluruh 23 image secara paralel dengan cache GitHub Actions teroptimasi.

---

## 📞 Dukungan & Kontak

- **Maintainer:** Ferdiaz Prasida
- **Email:** [ferdiazprasida@gmail.com](mailto:ferdiazprasida@gmail.com)
- **Website:** [https://diaww.my.id](https://diaww.my.id)
- **GitHub:** [@DIAWWDEV](https://github.com/DIAWWDEV)

---

<div align="center">
  <sub>Dibuat dengan ❤️ dan standar rekayasa terbaik untuk komunitas Pterodactyl Panel oleh <b>diaww.dev</b></sub>
</div>
