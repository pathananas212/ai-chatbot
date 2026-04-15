from groq import Groq, APIConnectionError, AuthenticationError, RateLimitError

from src.config import Config
from src.logger import get_logger

logger = get_logger(__name__)


class Chatbot:
    def __init__(self) -> None:
        Config.validate()
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.model = Config.GROQ_MODEL
        self.history: list[dict] = [
            {"role": "system", "content": Config.SYSTEM_PROMPT}
        ]
        logger.info("Chatbot initialized with model: %s", self.model)

    def chat(self, user_input: str) -> str:
        self.history.append({"role": "user", "content": user_input})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.history,
            )
        except AuthenticationError:
            logger.error("Invalid GROQ_API_KEY. Check your .env file.")
            raise
        except RateLimitError:
            logger.warning("Rate limit hit. Please wait before retrying.")
            raise
        except APIConnectionError as e:
            logger.error("Could not connect to Groq API: %s", e)
            raise

        reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
        logger.debug("Response received (%d chars)", len(reply))
        return reply

    def reset(self) -> None:
        self.history = [{"role": "system", "content": Config.SYSTEM_PROMPT}]
        logger.info("Conversation history cleared.")
