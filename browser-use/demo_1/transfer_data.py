import asyncio
import re
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from browser_use import Agent
from langchain_openai import ChatOpenAI

async def fetch_and_save(txt_path="results.txt"):
    # 1) Prompt the user via the agent
    prompt = (
        
        "Please open your browser and navigate to Amazon; once there, "
        "search for ‘latest mac book’; "
        "click on the first product in the results list; "
        "allow the product page and its images to load fully, then copy the exact URL displayed "
        "in your address bar for the product page; finally, "
        "paste that URL here as plain text only, omitting any additional commentary, "
        "explanation, or formatting."
    )
    agent = Agent(
        task=prompt,
        llm=ChatOpenAI(
            base_url="https://uat-gke-llm.hachiai.com/qwen/v1/",
            model="qwen2-5-72b-a100",
            openai_api_key="temp"
        )
    )

    # 2) Run the agent and capture its plain-text output
    result = await agent.run()
    text = str(result)

    # 3) Extract all HTTP(S) URLs and take the last one (the final results page)
    urls = re.findall(r"https?://[^\s'\"<>]+", text)
    if not urls:
        raise RuntimeError("No URL found in agent output.")
    url = urls[-1]

    # 4) Write the final URL to results.txt in your working directory
    out_path = Path(txt_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(url + "\n", encoding="utf-8")
    print(f"→ Captured final URL and saved to {out_path.resolve()}:\n{url}")
    return url

if __name__ == "__main__":
    cwd = os.getcwd()
    target_file = os.path.join(cwd, "results.txt")
    asyncio.run(fetch_and_save(txt_path=target_file))