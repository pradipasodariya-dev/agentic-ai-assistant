from utils.env_loader import load_env_keys
from langchain.agents import initialize_agent
from langchain_openai import OpenAI
from tools.google_search_tool import get_google_search_tool
from tools.weather_tool import get_weather_tool

# Load API keys
keys = load_env_keys()
llm = OpenAI(temperature=0, openai_api_key=keys["OPENAI_API_KEY"])

# Tools
tools = [
    get_google_search_tool(keys),
    get_weather_tool(keys["WEATHER_API_KEY"])
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

query = "What's the weather in Tokyo and latest GenAI news?"
response = agent.run(query)
print("Agent Response:")
print(response)
