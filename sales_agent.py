from config import swarm_client
from swarm import Agent
from agents.research_agent import transfer_to_web_search_agent
from agents.time_agent import transfer_to_get_time_agent
from agents.inventory_query_agent import transfer_to_inventory_query_agent

manager = Agent(
  name="Dispatcher Agent",
  instructions="You will handle tasks and dispatch them to your agents based on the user's request. If you encounter a question you don't know how to answer, use the research_agent to query the internet and respond based on the results.You will use Traditional Chinese when replying to users.",
  model="gpt-4o-mini",
  functions=[transfer_to_web_search_agent, 
             transfer_to_get_time_agent, 
             transfer_to_inventory_query_agent]
)

user_prompt = input("請提問：")

response = swarm_client.run(
    agent = manager,
    messages=[{"role": "user", "content": user_prompt}],
)

print(response.messages[-1]["content"])
