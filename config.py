import os
from dotenv import load_dotenv
from tavily import TavilyClient
from swarm import Swarm
load_dotenv()
swarm_client = Swarm()
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
