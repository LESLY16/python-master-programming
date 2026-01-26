# python-master-programming
This repository contains python scripts that belongs to the owner. So you can only clone and contribute to it.

## 🤖 NLP-Powered Chat Bot

A full-featured natural language processing (NLP) chat bot with console interface for interactive conversations.

### Features

- **Intent Classification**: Automatically detects user intent from natural language input
- **Context-Aware Responses**: Provides intelligent, relevant responses to user queries
- **Sentiment Analysis**: Analyzes emotional tone of messages (optional feature)
- **Error Handling**: Gracefully handles unrecognized inputs with fallback responses
- **Conversation History**: Tracks conversation flow for better context
- **Console Interface**: Easy-to-use command-line interface
- **Modular Design**: Clean, well-documented, and extensible codebase

### Quick Start

#### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses Python standard library only)

#### Installation

1. Clone the repository:
```bash
git clone https://github.com/LESLY16/python-master-programming.git
cd python-master-programming
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. The chatbot uses only Python standard library, so no package installation is needed!

#### Running the Chat Bot

**Option 1: Using the launcher script**
```bash
python run_chatbot.py
```

**Option 2: Run directly from the module**
```bash
python -m nlp_chatbot.console_interface
```

**Option 3: Disable sentiment analysis**
```bash
python run_chatbot.py --no-sentiment
```

#### Usage Example

```
You: Hello!
Bot: Hi there! What can I do for you?

You: What can you do?
Bot: I can:
- Have conversations with you
- Answer questions
- Provide information on various topics
- Analyze sentiment in your messages
- Help with Python-related queries

You: Tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs! 😄

You: Thanks!
Bot: Happy to help!

You: bye
Bot: Goodbye! Have a great day!
```

### Project Structure

```
nlp_chatbot/
├── __init__.py              # Package initialization
├── chatbot.py               # Core chatbot logic and intent classification
├── sentiment_analyzer.py    # Sentiment analysis module
└── console_interface.py     # Console interface for user interaction

run_chatbot.py               # Main launcher script
```

### Supported Intents

The chat bot recognizes the following intents:

- **Greetings**: "hi", "hello", "hey"
- **Farewells**: "bye", "goodbye", "exit"
- **Thanks**: "thank you", "thanks"
- **Help requests**: "help", "assist"
- **Name queries**: "what's your name", "who are you"
- **Python questions**: "python", "programming", "code"
- **Status queries**: "how are you"
- **Capabilities**: "what can you do"
- **Humor**: "tell me a joke"

### Advanced Usage

#### Using as a Python Module

```python
from nlp_chatbot import ChatBot, SentimentAnalyzer

# Initialize
bot = ChatBot()
analyzer = SentimentAnalyzer()

# Get response
user_input = "Hello! How are you?"
response = bot.generate_response(user_input)
print(response)

# Analyze sentiment
sentiment = analyzer.analyze(user_input)
print(f"Sentiment: {sentiment['sentiment']} ({sentiment['confidence']:.2f})")
```

#### Extending the Bot

To add new intents, edit `nlp_chatbot/chatbot.py`:

```python
self.intents['your_intent'] = {
    'patterns': [
        r'\byour_pattern_here\b',
    ],
    'responses': [
        "Your response here",
    ]
}
```

### Testing

Run the test suite:
```bash
cd "python tests"
pytest test_math_func.py
```

### Architecture

The chatbot uses a lightweight, rule-based NLP approach:

1. **Intent Classification**: Uses regex pattern matching to identify user intent
2. **Response Generation**: Selects appropriate responses based on classified intent
3. **Sentiment Analysis**: Rule-based sentiment scoring using keyword matching
4. **Error Handling**: Provides fallback responses for unrecognized inputs

### Future Enhancements

For production use, consider integrating:

- **Transformers Models**: Use Hugging Face transformers for advanced NLP
- **Vector Databases**: Store conversation context for better memory
- **API Integration**: Connect to external services for real-time data
- **Multi-language Support**: Add support for multiple languages
- **Voice Interface**: Add speech-to-text and text-to-speech capabilities

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### License

This project is part of the python-master-programming repository.
