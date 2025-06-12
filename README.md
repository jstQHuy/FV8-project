#  FV8 Setup Guide

## Contents
- [1.1 Environment & Requirements](#11-environment--requirements)
- [1.2 Installation Steps](#12-installation-steps)
- [Notes](#-notes)

---

## 1.1 Environment & Requirements

### Operating System
- Ubuntu 20.04 (recommended)

### Software
- Docker
- Python ≥ 3.10
- Chromium (patched for FV8)

### Hardware
- Disk space: > 50GB
- RAM: ≥ 8GB

### Dataset
- 90 malicious extensions (D2)
- 100 benign extensions (D3)

---

## 1.2 Installation Steps

### Clone the repository
```bash
git clone https://github.com/wspr-ncsu/FV8.git
cd FV8
```

### Install dependencies
```bash
pip install -r scripts/requirements.txt
```

### Set up Docker
```bash
export DOCKER_BUILDKIT=0
python scripts/vv8-cli.py setup
```

### Install patched Chromium
```bash
sudo dpkg -i deb_files/chromium-browser-stable_122.0.6261.111-1_amd64.deb
```

### Step 5: Verify installation
```bash
chromium-browser-stable --headless \
  --no-sandbox --disable-gpu \
  --disable-features=NetworkService \
  --js-flags='--no-lazy' https://google.com
```

### Start crawler
```bash
python crawler_queue_tranco.py
```

---

## Notes

- All logs are stored in **MongoDB** (`raw_logs`) and **PostgreSQL** (`logfile`, `mega_features`, `mega_usages`, etc.)
- Use **Flower UI** at `localhost:5555` to monitor crawling jobs.
