import os
import sys
import requests
from urllib.parse import urljoin, urlparse, unquote
from bs4 import BeautifulSoup
from datetime import datetime

def download_images_from_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc.replace("www.", "")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = f"{domain}_{ts}"
    os.makedirs(folder, exist_ok=True)
    print(f"→ Created folder: {folder}")

    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    seen, count = set(), 0
    img_tags = soup.find_all("img")
    print(f"→ Found {len(img_tags)} images; downloading…")

    for img in img_tags:
        src = img.get("src") or img.get("data-src") or img.get("data-lazy-src")
        if not src or src.startswith("data:"):
            continue
        img_url = urljoin(url, src)
        if img_url in seen:
            continue
        seen.add(img_url)

        path = unquote(urlparse(img_url).path)
        ext = os.path.splitext(path)[1].lower()
        if ext not in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}:
            try:
                head = requests.head(img_url, timeout=5)
                ctype = head.headers.get("content-type", "")
                ext = (
                    ".jpg" if "jpeg" in ctype else
                    ".png" if "png" in ctype else
                    ".gif" if "gif" in ctype else
                    ".webp" if "webp" in ctype else
                    ""
                )
            except:
                ext = ""

        count += 1
        fn = f"img_{count:03d}{ext}"
        save_path = os.path.join(folder, fn)
        try:
            r = requests.get(img_url, stream=True, timeout=10)
            r.raise_for_status()
            with open(save_path, "wb") as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            print(f"[{count}] Saved {fn}")
        except Exception as e:
            print(f"[{count}]  {img_url}: {e}")

    print(f"Done. {count} images saved to `{folder}`.")

if __name__ == "__main__":
    txt = sys.argv[1] if len(sys.argv) > 1 else "results.txt"
    try:
        with open(txt, "r", encoding="utf-8") as f:
            url = next(line.strip() for line in f if line.strip())
    except Exception:
        print(f" Could not read URL from {txt}")
        sys.exit(1)
    download_images_from_url(url)