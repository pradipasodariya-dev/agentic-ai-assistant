# Agentic AI Assistant

This is a self-contained, LangChain-powered autonomous agent that uses:

- 🔍 Google Search (via SerpAPI)
- ☁️ Live Weather API
- 🧠 GPT (OpenAI)

## 🚀 How to Run

```bash
git clone https://github.com/<yourname>/agentic-ai-assistant.git
cd agentic-ai-assistant
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add your API keys
python main.py
