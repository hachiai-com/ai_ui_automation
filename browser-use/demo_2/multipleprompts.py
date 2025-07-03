import asyncio
import json
import os
from dotenv import load_dotenv
from browser_use import Agent
from langchain_openai import ChatOpenAI

load_dotenv()

async def run_prompt(entry):
    try:
        agent = Agent(
            task=entry["task"],
            llm=ChatOpenAI(
                base_url="https://uat-gke-llm.hachiai.com/qwen/v1/",
                model=entry.get("model", "qwen2-5-72b-a100"),
                openai_api_key=os.getenv("OPENAI_API_KEY")
            )
        )
        print(f"\n {entry['task']}")
        await agent.run()
    except Exception as e:
        print(f" Failed on {entry['task']!r}: {e}")
    

async def main():
    with open("prompts.json", "r") as f:
        prompts = json.load(f)

    for entry in prompts:
        await run_prompt(entry)

if __name__ == "__main__":
    asyncio.run(main())
