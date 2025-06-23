# Agentic AI Assistant

This project demonstrates how to build a simple, autonomous Agentic AI assistant using LangChain, OpenAI, and external tools like weather data and Google search.

---

## Features

- 🧠 LLM-powered agent using GPT (OpenAI)
- 🔍 Real-time web search (Google Programmable Search API)
- ☁️ Live weather information
- 🧰 Modular tool-based architecture

---

## Tech Stack

- `Python 3.9+`
- `LangChain`
- `OpenAI GPT`
- `Google Custom Search API`
- `WeatherAPI`
- `Dotenv` for secret management

---

## 🌐 API Keys & Setup

Create a `.env` file in the root of the project and include:

```env
OPENAI_API_KEY=your-openai-key
GOOGLE_API_KEY=your-google-api-key
GOOGLE_CX=your-google-search-engine-id
WEATHER_API_KEY=your-weatherapi-key
```

| Key Name         | Platform                                         | Purpose                                  |
|------------------|--------------------------------------------------|------------------------------------------|
| `OPENAI_API_KEY` | [OpenAI](https://platform.openai.com/)           | GPT-4 or GPT-3.5 access                  |
| `GOOGLE_API_KEY` | [Google Cloud](https://console.cloud.google.com/) | Custom Search JSON API                   |
| `GOOGLE_CX`      | [Programmable Search](https://programmablesearchengine.google.com/) | Search Engine ID |
| `WEATHER_API_KEY`| [WeatherAPI](https://www.weatherapi.com/)        | Current weather data                     |

---

## How to Run project

```bash
git clone https://github.com/yourname/agentic-ai-assistant.git
cd agentic-ai-assistant
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # and fill in API keys
python main.py
```

---

## Project Structure

```
agentic-ai-assistant/
├── .env                    # API keys (not committed)
├── README.md
├── requirements.txt
├── main.py
├── tools/
│   ├── google_search_tool.py
│   └── weather_tool.py
└── utils/
    └── env_loader.py
```

---

## Output

```
Agent: Checking Tokyo's weather and the latest GenAI news...
Final Answer:
Tokyo's weather is cloudy, 26°C. Recent news includes Mosaicx launching an AI-native platform.
```
![image](https://github.com/user-attachments/assets/4ebfaabb-58da-4378-863d-5c99a7c0f57f)


---

## Feedback

If this project helped you, give it a ⭐ on GitHub or suggest improvements in Issues!
