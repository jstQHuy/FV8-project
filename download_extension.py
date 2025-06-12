import os
import requests
import zipfile
import io
TXT_FILE = "list.txt"  # File .txt chứa danh sách extension ID, mỗi dòng 1 ID
OUT_DIR = "../D2"  # Thư mục lưu .crx và mã nguồn đã giải nén
CHROME_VER = "122.0.6261.111"
HEADERS = {
    "User-Agent": f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{CHROME_VER} Safari/537.36"
}
# Tạo thư mục nếu chưa có
os.makedirs(OUT_DIR, exist_ok=True)

# Đọc danh sách ID
with open(TXT_FILE, encoding="utf-8") as f:
    extension_ids = [line.strip() for line in f if line.strip()]

success = 0
for eid in extension_ids:
    print(f"Dang tai", end=" ")
    url = (
        "https://clients2.google.com/service/update2/crx?"
        f"response=redirect&acceptformat=crx2,crx3&prodversion={CHROME_VER}&x=id%3D{eid}%26uc"
    )
    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        if r.status_code != 200 or len(r.content) < 100:
            print(f"Bo qua (HTTP {r.status_code})")
            continue
        ext_dir = os.path.join(OUT_DIR, eid)
        os.makedirs(ext_dir, exist_ok=True)
        crx_path = os.path.join(ext_dir, f"{eid}.crx")
        with open(crx_path, "wb") as f:
            f.write(r.content)
        # Giải nén .crx 
        pkg = io.BytesIO(r.content[16:])
        with zipfile.ZipFile(pkg) as z:
            z.extractall(ext_dir)
        print(" THÀNH CÔNG")
        success += 1
    except Exception as e:
        print(f"Failed: {e}")

print(f"\n Succes {success}/{len(extension_ids)} extension.")

