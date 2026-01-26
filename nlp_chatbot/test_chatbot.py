"""
Unit tests for NLP Chat Bot module.

Tests cover:
- ChatBot intent classification
- Response generation
- Sentiment analysis
- Error handling
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nlp_chatbot import ChatBot, SentimentAnalyzer


def test_chatbot_initialization():
    """Test that ChatBot initializes correctly."""
    bot = ChatBot()
    assert bot is not None
    assert len(bot.intents) > 0
    assert len(bot.fallback_responses) > 0
    assert bot.conversation_history == []


def test_intent_classification_greeting():
    """Test greeting intent classification."""
    bot = ChatBot()
    
    # Test various greeting inputs
    assert bot.classify_intent("hello") == "greeting"
    assert bot.classify_intent("Hi there!") == "greeting"
    assert bot.classify_intent("Good morning") == "greeting"
    assert bot.classify_intent("Hey") == "greeting"


def test_intent_classification_goodbye():
    """Test goodbye intent classification."""
    bot = ChatBot()
    
    assert bot.classify_intent("bye") == "goodbye"
    assert bot.classify_intent("Goodbye!") == "goodbye"
    assert bot.classify_intent("See you later") == "goodbye"


def test_intent_classification_help():
    """Test help intent classification."""
    bot = ChatBot()
    
    assert bot.classify_intent("help me") == "help"
    assert bot.classify_intent("I need assistance") == "help"
    assert bot.classify_intent("Can you assist?") == "help"


def test_intent_classification_python():
    """Test Python-related intent classification."""
    bot = ChatBot()
    
    assert bot.classify_intent("Tell me about Python") == "python_question"
    assert bot.classify_intent("How do I write a function?") == "python_question"
    assert bot.classify_intent("What is a variable?") == "python_question"


def test_response_generation():
    """Test that bot generates responses."""
    bot = ChatBot()
    
    response = bot.generate_response("Hello")
    assert response is not None
    assert len(response) > 0
    assert isinstance(response, str)


def test_exit_command_detection():
    """Test exit command detection."""
    bot = ChatBot()
    
    assert bot.is_exit_command("bye") is True
    assert bot.is_exit_command("exit") is True
    assert bot.is_exit_command("quit") is True
    assert bot.is_exit_command("hello") is False
    assert bot.is_exit_command("help") is False


def test_conversation_history():
    """Test conversation history tracking."""
    bot = ChatBot()
    
    bot.generate_response("Hello")
    bot.generate_response("How are you?")
    
    history = bot.get_conversation_history()
    assert len(history) == 2
    assert "Hello" in history
    assert "How are you?" in history


def test_clear_history():
    """Test clearing conversation history."""
    bot = ChatBot()
    
    bot.generate_response("Hello")
    bot.generate_response("How are you?")
    
    bot.clear_history()
    assert len(bot.get_conversation_history()) == 0


def test_sentiment_analyzer_initialization():
    """Test SentimentAnalyzer initialization."""
    analyzer = SentimentAnalyzer()
    assert analyzer is not None
    assert len(analyzer.positive_words) > 0
    assert len(analyzer.negative_words) > 0


def test_sentiment_positive():
    """Test positive sentiment detection."""
    analyzer = SentimentAnalyzer()
    
    result = analyzer.analyze("I love this! It's amazing and wonderful!")
    assert result['sentiment'] == 'positive'
    assert result['score'] > 0


def test_sentiment_negative():
    """Test negative sentiment detection."""
    analyzer = SentimentAnalyzer()
    
    result = analyzer.analyze("This is terrible and awful. I hate it!")
    assert result['sentiment'] == 'negative'
    assert result['score'] < 0


def test_sentiment_neutral():
    """Test neutral sentiment detection."""
    analyzer = SentimentAnalyzer()
    
    result = analyzer.analyze("The weather is normal today.")
    assert result['sentiment'] == 'neutral'
    assert abs(result['score']) < 0.4


def test_sentiment_empty_input():
    """Test sentiment analysis with empty input."""
    analyzer = SentimentAnalyzer()
    
    result = analyzer.analyze("")
    assert result['sentiment'] == 'neutral'
    assert result['score'] == 0.0


def test_sentiment_with_negation():
    """Test sentiment analysis with negation."""
    analyzer = SentimentAnalyzer()
    
    result = analyzer.analyze("This is not good at all")
    assert result['sentiment'] == 'negative' or result['sentiment'] == 'neutral'


def test_sentiment_emoji():
    """Test emoji generation for sentiments."""
    analyzer = SentimentAnalyzer()
    
    assert analyzer.get_emoji('positive') == '😊'
    assert analyzer.get_emoji('negative') == '😞'
    assert analyzer.get_emoji('neutral') == '😐'


def test_fallback_response():
    """Test that bot provides fallback for unrecognized input."""
    bot = ChatBot()
    
    # Use nonsensical input that shouldn't match any pattern
    response = bot.generate_response("xyzabc123nonsense")
    assert response is not None
    assert len(response) > 0


def test_multiple_intents_in_input():
    """Test handling of input with multiple potential intents."""
    bot = ChatBot()
    
    # Input contains both greeting and help patterns
    response = bot.generate_response("Hello, can you help me?")
    assert response is not None
    # Should classify as greeting (first match)
    intent = bot.classify_intent("Hello, can you help me?")
    assert intent in ['greeting', 'help']


# Commands to run tests:
# pytest test_chatbot.py -v
# pytest test_chatbot.py -v -k "sentiment"
# pytest test_chatbot.py -v -k "intent"
