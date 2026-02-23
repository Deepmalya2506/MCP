import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def chat_session():
    """Run a chat using MCPAgent's built in conversation memory"""
    load_dotenv()
    api=os.getenv("GROQ_API_KEY")

    config_file=r"server\config_file.json"
    print("\n         Initializing Chat Room..."  )

    client=MCPClient.from_config_file(config_file)
    llm=ChatGroq(model="openai/gpt-oss-120b")

    agent=MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True
    )

    print("===========================Chat-Room================================")
    print("type 'exit' or 'quit' to quit session")
    print("type 'clear' to clear chat history")

    try:
        while True:
            user=input("\nYou: ")
            if(user.lower() in ["exit", "quit"]):
                print("Ending conversation....")
                print("....Thank You....")
                break

            elif(user.lower()=='clear'):
                agent.clear_conversation_history()
                print("Conversatino History cleaned...")
                continue

            response=await agent.run(user)
            print(f"Agent: {response}")
    except Exception as e:
        print(f"An error occured. Error reported as-> {e}")
    
    finally:
        if client and client.sessions:
            await client.close_all_sessions()
        
if __name__=="__main__":
    asyncio.run(chat_session())
            



    
