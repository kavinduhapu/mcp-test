from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

import asyncio
import dotenv

dotenv.load_dotenv()
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
# model = ChatOpenAI(model="gpt-4o")
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

async def main():

    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": ["/home/kavindu-hapuarachchi/data-science-projects/mcp-test/math_server.py"],
                "transport": "stdio",
            },
            "weather": {
                # Make sure you start your weather server on port 8000
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            }
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent(model, tools)
    math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
    weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})

    print(math_response)
    print(weather_response)


# Run the async function
asyncio.run(main())