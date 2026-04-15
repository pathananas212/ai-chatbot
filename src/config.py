import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    GROQ_API_KEY: str = os.environ.get("GROQ_API_KEY", "")
    GROQ_MODEL: str = os.environ.get("GROQ_MODEL", "llama-3.1-8b-instant")
    SYSTEM_PROMPT: str = os.environ.get("SYSTEM_PROMPT", "You are a helpful AI assistant.")
    LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls) -> None:
        if not cls.GROQ_API_KEY:
            raise EnvironmentError(
                "GROQ_API_KEY is not set. "
                "Copy .env.example to .env and add your key."
            )
