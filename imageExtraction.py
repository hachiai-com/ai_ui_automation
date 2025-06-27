import asyncio
from dotenv import load_dotenv
load_dotenv()

from browser_use import Agent
from langchain_openai import ChatOpenAI

async def main():
    # agent = Agent(
    #     task=(
    #         "Go to www.mobilelive.ai/, look for images and suggest their ALT tags. look for page source if necessary."
    #     ),
    #     llm=ChatOpenAI(
    #         base_url="https://uat-gke-llm.hachiai.com/qwen/v1/",
    #         model="qwen2-5-72b-a100",
    #         openai_api_key="temp"
    #     )
    # )
    agent = Agent(
        task=(
            "1. Go to https://www.mobilelive.ai/ in the browser\n"
            "2. Wait 5 seconds for complete page loading\n"
            "3. Slowly scroll through the entire page from top to bottom\n"
            "4. Right-click anywhere and select 'Inspect' or press F12 to open developer tools\n"
            "5. In the Elements/Inspector tab, use Ctrl+F to search for 'img' tags\n"
            "6. Also search for 'background-image' in the Elements tab\n"
            "7. Document every image you find with:\n"
            "   - Image source URL\n"
            "   - Current ALT text (if present)\n"
            "   - Image dimensions and location on page\n"
            "   - Suggested ALT text based on image content/context\n"
            "8. Take screenshots of the images if needed for better analysis\n"
            "9. Provide a final summary report of all images found and ALT tag recommendations"
        ),
        llm=ChatOpenAI(
            base_url="https://openrouter.ai/api/v1",
            model="deepseek/deepseek-chat-v3-0324:free",
            openai_api_key="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"
        )
    )

    await agent.run()

asyncio.run(main())
