import subprocess
import sys

PYTHON = sys.executable

# 1) Fetch URL and save to results.txt
ret1 = subprocess.run([PYTHON, "transfer_data.py"], check=False)
if ret1.returncode != 0:
    sys.exit(ret1.returncode)

# 2) Download images using the fetched URL
ret2 = subprocess.run([PYTHON, "download_images.py"], check=False)
if ret2.returncode != 0:
    sys.exit(ret2.returncode)

print("Pipeline completed successfully.")