from swarm import Agent
from config import tavily_client

def transfer_to_web_search_agent():
  print("\033[93m切換至 web_search_agent\033[0m")
  return web_search_agent

def search_web(query):
  print("\033[93m開始查詢:\033[0m", query)
  response = tavily_client.search(query)
  return response

web_search_agent = Agent(
  name="web_search_agent",
  instructions="""
    你是一個研究型 agent，專注於為用戶搜尋並整理網路上最相關、最可靠的資訊。請遵循以下原則：\n"
    "1. 當問題涉及最新資訊、特殊細節或內部資料不足以解答時，再使用 search_web 函數進行網路查詢。\n"
    "2. 在進行網路查詢前，請先評估是否可根據已有知識直接回答，如資訊充足則直接回答，不調用 search_web。\n"
    "3. 僅在查詢能顯著提升答案準確性或完整性時，才調用 search_web，避免不必要的網路請求。\n"
    "4. 請使用繁體中文回答問題，並保持回答的專業與精確。
  """,
  model="gpt-4o",
  functions=[search_web],
)
