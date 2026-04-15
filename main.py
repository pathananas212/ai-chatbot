from src.chatbot import Chatbot
from src.logger import get_logger

logger = get_logger(__name__)

COMMANDS = {
    "/quit": "Exit the chatbot",
    "/reset": "Clear conversation history",
    "/help": "Show available commands",
}


def print_help() -> None:
    print("\nAvailable commands:")
    for cmd, desc in COMMANDS.items():
        print(f"  {cmd:10} — {desc}")
    print()


def main() -> None:
    print("=" * 50)
    print("  AI Chatbot  |  Powered by Groq")
    print("  Type /help for commands, /quit to exit")
    print("=" * 50)

    try:
        bot = Chatbot()
    except EnvironmentError as e:
        print(f"\nConfiguration error: {e}\n")
        return

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input == "/quit":
            print("Goodbye!")
            break
        elif user_input == "/reset":
            bot.reset()
            print("Conversation reset.")
            continue
        elif user_input == "/help":
            print_help()
            continue

        try:
            reply = bot.chat(user_input)
            print(f"\nAssistant: {reply}")
        except Exception as e:
            print(f"\nError: {e}")
            logger.exception("Unexpected error during chat")


if __name__ == "__main__":
    main()
