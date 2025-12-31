import asyncio
import os
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient  
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

async def main():
    client = MultiServerMCPClient({
        "calculator": {
            "transport": "http",
            "url": "http://localhost:8000/mcp",
        }
    })

    tools = await client.get_tools()

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0
    )

    agent = create_agent(
        llm,
        tools,
        system_prompt="""You are a helpful assistant that will use calculator tool to perform 
        arithmetic operations like addition, subtraction, multiplication, and division.
        For any user query not related to calculations, 
        respond only if you are sure of the answer.""",
    )

    user_input = "What is (10 + 2) * 7 and machine learning?"

    result = await agent.ainvoke(
    {"messages": [{"role": "user", "content": user_input}]}
    )

    for message in result["messages"]:
        print(message.pretty_print())

if __name__ == "__main__":
    asyncio.run(main())
