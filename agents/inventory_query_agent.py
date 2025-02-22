import os
from swarm import Agent
from tinydb import TinyDB

# 確保目錄存在
data_dir = '../data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

inventory_db = TinyDB('./data/inventory_db.json')

def transfer_to_inventory_query_agent():
    print("\033[93m切換至 InventoryQueryAgent\033[0m")
    return inventory_query_agent

def fetch_inventory_items(query):
    print("\033[93m開始查詢庫存:\033[0m", query)
    return inventory_db.all()

inventory_query_agent = Agent(
    name="InventoryQueryAgent",
    instructions="""
      你是一個庫存查詢管理代理，負責協助管理和查詢庫存數據。
      當接收到查詢條件時，請根據條件從庫存資料庫中返回相應的庫存項目。
      請確保查詢結果準確並提供必要的庫存資訊。
    """,
    model="gpt-4o",
    functions=[fetch_inventory_items],
)
