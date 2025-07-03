


This pipeline starts with transfer_data.py, which asks an AI agent to guide you through your browser, copy the product page URL, and save it into results.txt.

Next, download_images.py reads that URL, scrapes every <img> tag on the page, and downloads each image into a timestamped folder.

Finally, run_pipeline.py runs those two scripts in order—first fetching the URL, then downloading the images—using a single command.

Each script prints its progress and handles errors, so you always know what’s happening.

Together, they automate the entire workflow of grabbing a product link and pulling down all its images.





```
uv venv --python 3.11.13
```
```
.venv\Scripts\activate
```
```
uv pip install -r requirements.txt
```
```
uv pip install browser-use
```
```
uv run playwright install
```
