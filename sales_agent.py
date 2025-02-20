import os
from datetime import datetime
from dotenv import load_dotenv
from swarm import Agent, Swarm
from tavily import TavilyClient
load_dotenv()

client = Swarm()
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query):
  print("\033[93m開始查詢:\033[0m", query)
  response = tavily_client.search(query)
  return response

def transfer_to_research_agent():
  print("\033[93m切換至 Research Agent\033[0m")
  return research_agent

manager = Agent(
  name="Dispatcher Agent",
  instructions="You will handle tasks and dispatch them to your agents based on the user's request. If you encounter a question you don't know how to answer, use the research_agent to query the internet and respond based on the results.You will use Traditional Chinese when replying to users.",
  model="gpt-4o-mini",
  functions=[transfer_to_research_agent]
)

research_agent = Agent(
  name="Research Agent",
  instructions="你是一個研究型 agent，專注於為用戶搜尋並整理網路上最相關、最可靠的資訊。請遵循以下原則：\n"
    "1. 當問題涉及最新資訊、特殊細節或內部資料不足以解答時，再使用 search_web 函數進行網路查詢。\n"
    "2. 在進行網路查詢前，請先評估是否可根據已有知識直接回答，如資訊充足則直接回答，不調用 search_web。\n"
    "3. 僅在查詢能顯著提升答案準確性或完整性時，才調用 search_web，避免不必要的網路請求。\n"
    "4. 請使用繁體中文回答問題，並保持回答的專業與精確。",
  model="gpt-4o",
  functions=[search_web],
)

user_prompt = input("請提問：")

response = client.run(
    agent = manager,
    messages=[{"role": "user", "content": user_prompt}],
)

# Print the last message from the response
print(response.messages[-1]["content"])