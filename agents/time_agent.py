from swarm import Agent
from datetime import datetime

def transfer_to_get_time_agent():
  print("\033[93m切換至 get_time_agent\033[0m")
  return get_time_agent

def get_current_time():
    return datetime.now().isoformat()

get_time_agent = Agent(
  name="get_time_agent",
  instructions="""
    取得時間 agent，專注於回答與時間相關的問題。請遵循以下原則：\n"
    "1. 當問題涉及時間時，使用 get_current_time 函數回答。\n"
    "2. 保持回答的專業與精確。
  """,
  model="gpt-4o",
  functions=[get_current_time],
)
