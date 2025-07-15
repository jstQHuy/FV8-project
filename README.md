#  FV8 Setup Guide

## Contents
- [1.1 Environment & Requirements](#11-environment--requirements)
- [1.2 Installation Steps](#12-installation-steps)
- [Notes](#notes)
- [Demo Video](#demo-video)

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


### Crawler Execution Flow

To automate crawling hundreds of extensions across multiple URLs, FV8 uses two key components: a shell script (`queue.sh`) and a Python script (`crawler_queue.py`).

####  `queue.sh`
- Launches multiple `tmux` sessions in parallel.
- Each session runs `crawler_queue.py` on a slice of the URL list.
- Example loop:

```bash
for i in {0..11}
do
    tmux new-session -d -s queue-$i "python3 crawler_queue.py -i ALL_EXTENSIONS_D2 -s $i -e $((i+1))"
done
```

####  `crawler_queue.py`
- Reads extension folders from `INDIR` and maps them to URL targets.
- Uses Chromium headless to run each extension on 12 URLs.
- Applies `--js-flags='--no-lazy'` to force early execution of all scripts.
- Logs are generated and sent to both MongoDB and PostgreSQL.

Key logic (simplified):

```python
cmd = f"python3 ./scripts/vv8-cli.py crawl -pp Mfeatures --no-headless --show-chrome-log \
  --disable-screenshot --disable-artifact-collection --disable-har --disable-gpu \
  --disable-features=NetworkService --js-flags='--no-lazy' {flag_ext1} {flag_ext2} {timeout} -u {url} -o stdout"
```

This approach ensures scalable and reproducible forced execution of real-world extensions in an isolated and monitored environment.

---


## Notes

- All logs are stored in **MongoDB** (`raw_logs`) and **PostgreSQL** (`logfile`, `mega_features`, `mega_usages`, etc.)
- Use **Flower UI** at `localhost:5555` to monitor crawling jobs.

---

## Demo Video

[![Watch the demo](https://img.youtube.com/vi/MyNGjmM5i_o/0.jpg)](https://www.youtube.com/watch?v=MyNGjmM5i_o)
