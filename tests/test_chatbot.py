import os
import pytest
from unittest.mock import MagicMock, patch


@pytest.fixture(autouse=True)
def set_env(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "test-key")
    monkeypatch.setenv("GROQ_MODEL", "llama-3.1-8b-instant")
    monkeypatch.setenv("SYSTEM_PROMPT", "You are a helpful assistant.")


def _make_mock_response(content: str):
    message = MagicMock()
    message.content = content
    choice = MagicMock()
    choice.message = message
    response = MagicMock()
    response.choices = [choice]
    return response


@patch("src.chatbot.Groq")
def test_chat_returns_reply(mock_groq_cls):
    mock_client = MagicMock()
    mock_groq_cls.return_value = mock_client
    mock_client.chat.completions.create.return_value = _make_mock_response("Hello!")

    from src.chatbot import Chatbot
    bot = Chatbot()
    reply = bot.chat("Hi")

    assert reply == "Hello!"


@patch("src.chatbot.Groq")
def test_history_grows_with_each_turn(mock_groq_cls):
    mock_client = MagicMock()
    mock_groq_cls.return_value = mock_client
    mock_client.chat.completions.create.return_value = _make_mock_response("Hi there!")

    from src.chatbot import Chatbot
    bot = Chatbot()
    initial_len = len(bot.history)  # system prompt only
    bot.chat("Hello")

    # system + user + assistant
    assert len(bot.history) == initial_len + 2


@patch("src.chatbot.Groq")
def test_reset_clears_history(mock_groq_cls):
    mock_client = MagicMock()
    mock_groq_cls.return_value = mock_client
    mock_client.chat.completions.create.return_value = _make_mock_response("Hi!")

    from src.chatbot import Chatbot
    bot = Chatbot()
    bot.chat("Hello")
    bot.reset()

    assert len(bot.history) == 1  # only system prompt remains
    assert bot.history[0]["role"] == "system"


def test_missing_api_key_raises(monkeypatch):
    monkeypatch.delenv("GROQ_API_KEY", raising=False)

    # Reload config so it picks up the missing env var
    import importlib
    import src.config as cfg_module
    importlib.reload(cfg_module)

    with pytest.raises(EnvironmentError, match="GROQ_API_KEY"):
        cfg_module.Config.validate()

    # Restore for other tests
    importlib.reload(cfg_module)
