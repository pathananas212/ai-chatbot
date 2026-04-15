# AI Chatbot

A production-ready AI chatbot built with Python and the [Groq API](https://console.groq.com), featuring full conversation memory, clean architecture, and a CI pipeline.

## Features

- Conversation memory across the full session
- Configurable model and system prompt via `.env`
- Clean command interface (`/help`, `/reset`, `/quit`)
- Proper error handling for API errors (auth, rate limit, connection)
- Structured logging
- Docker support
- Unit tests with pytest
- GitHub Actions CI

## Project Structure

```
ai-chatbot/
├── src/
│   ├── chatbot.py      # Core chatbot logic
│   ├── config.py       # Environment-based configuration
│   └── logger.py       # Logging setup
├── tests/
│   └── test_chatbot.py # Unit tests
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions CI
├── main.py             # Entry point & CLI
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
├── .env.example
└── .gitignore
```

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/pathananas212/ai-chatbot.git
cd ai-chatbot
```

**2. Create your `.env` file**
```bash
cp .env.example .env
```
Edit `.env` and add your Groq API key (get one free at https://console.groq.com).

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run**
```bash
python main.py
```

## Docker

```bash
docker build -t ai-chatbot .
docker run -it --env-file .env ai-chatbot
```

## Testing

```bash
pip install -r requirements-dev.txt
pytest tests/ -v --cov=src
```

## Configuration

| Variable        | Default                      | Description                  |
|-----------------|------------------------------|------------------------------|
| `GROQ_API_KEY`  | *(required)*                 | Your Groq API key            |
| `GROQ_MODEL`    | `llama-3.1-8b-instant`       | Model to use                 |
| `SYSTEM_PROMPT` | `You are a helpful AI assistant.` | Bot persona / instructions |
| `LOG_LEVEL`     | `INFO`                       | Logging verbosity            |

## Commands

| Command  | Description               |
|----------|---------------------------|
| `/help`  | Show available commands   |
| `/reset` | Clear conversation memory |
| `/quit`  | Exit the chatbot          |
