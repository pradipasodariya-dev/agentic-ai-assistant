from langchain.agents import Tool
from serpapi import GoogleSearch

def google_search(query, api_key, cse_id):
    params = {
        "q": query,
        "api_key": api_key,
        "engine": "google",
        "cx": cse_id
    }
    search = GoogleSearch(params)
    result = search.get_dict()
    return result.get("organic_results", [{}])[0].get("snippet", "No results found.")

def get_google_search_tool(keys):
    return Tool(
        name="GoogleSearch",
        func=lambda q: google_search(q, keys["GOOGLE_API_KEY"], keys["GOOGLE_CX"]),
        description="Search current information on Google"
    )
