from config import swarm_client
from swarm import Agent
from agents.research_agent import transfer_to_web_search_agent
from agents.time_agent import transfer_to_get_time_agent
from agents.inventory_query_agent import transfer_to_inventory_query_agent

manager = Agent(
  name="Dispatcher Agent",
  instructions="""
你是一位 Dispatcher Agent，負責根據使用者的請求分派任務給適合的子代理。請根據以下邏輯操作：

1.**若問題與商品無關，請直接拒絕回答，並告知無法提供相關資訊。**
2. 若問題涉及時間（例如查詢當前時間、商品上架時間等），請先調用 Time Agent 獲取準確時間，再轉交 Inventory Agent 處理後續查詢。
3. 若問題涉及商品描述或有部分內容無法理解，請調用 Web Search Agent 進行網路搜尋，並以搜尋結果中的第一筆資訊作為回應。
4. 若問題與庫存查詢相關（如庫存數量、尺寸、顏色、商品名稱等），請交由 Inventory Agent 處理，**若沒有商品描述或是尺寸訊息請調用 Web Search Agent 進行網路搜尋，並以搜尋結果中的第一筆資訊作為回應**。

請務必以繁體中文回答，並根據上下文靈活選擇使用哪個子代理，以提供最精確的回應。
      """,
  model="gpt-4o-mini",
  functions=[transfer_to_web_search_agent, 
             transfer_to_get_time_agent, 
             transfer_to_inventory_query_agent]
)

conversation_history = [{"role": "system", "content": manager.instructions}]
try:
  while True:
      user_prompt = input("請提問：")
      if user_prompt.strip() == "exit": break
      if user_prompt.strip() == "": continue
      # 加入使用者訊息到對話歷史中
      conversation_history.append({"role": "user", "content": user_prompt})
      
      # 呼叫 swarm_client.run 並傳入完整的對話歷史，讓 Agent 具有上下文
      response = swarm_client.run(agent=manager, messages=conversation_history)
      reply = response.messages[-1]["content"]
      
      # 將 Agent 回覆也記錄進對話歷史中
      conversation_history.append({"role": "assistant", "content": reply})
      print("Agent 回應：", reply)
except EOFError:
  print("謝謝使用！")