from dotenv import load_dotenv
from swarm import Agent, Swarm

# Load environment variables
load_dotenv()

# Initialize the Swarm client
client = Swarm()

def transfer_to_agent_b():
    return agent_b

# Define Agent A
agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

# Define Agent B
agent_b = Agent(
    name="Agent B",
    instructions="Only speak in Haikus.",
)

# Run the Swarm with Agent A
response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}],
)

# Print the last message from the response
print(response.messages[-1]["content"])