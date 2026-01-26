# NLP Chat Bot Quick Reference

## Project Overview
A full-featured natural language processing chat bot with console interface, implementing intent classification, sentiment analysis, and conversational AI.

## Installation & Setup
```bash
# Clone repository
git clone https://github.com/LESLY16/python-master-programming.git
cd python-master-programming

# No external dependencies required - uses Python standard library only!
```

## Running the Chat Bot

### Method 1: Using launcher script
```bash
python run_chatbot.py
```

### Method 2: Direct module execution
```bash
python -m nlp_chatbot.console_interface
```

### Method 3: Disable sentiment analysis
```bash
python run_chatbot.py --no-sentiment
```

## Features

### ✅ Implemented
- **Intent Classification**: 10+ predefined intents (greeting, farewell, help, Python questions, jokes, etc.)
- **Response Generation**: Context-aware responses with fallback handling
- **Sentiment Analysis**: Real-time emotion detection (positive/negative/neutral)
- **Conversation History**: Tracks user inputs throughout the session
- **Error Handling**: Graceful fallback for unrecognized inputs
- **Console Interface**: Clean, user-friendly terminal interface
- **Exit Commands**: Multiple ways to exit (bye, goodbye, exit, quit)
- **Statistics**: Conversation metrics at end of session

### 🎯 Supported Intents
- Greetings: "hello", "hi", "hey"
- Farewells: "bye", "goodbye", "exit"
- Thanks: "thank you", "thanks"
- Help: "help", "assistance", "guide"
- Name queries: "what's your name", "who are you"
- Python questions: mentions of "python", "programming", "code"
- Status queries: "how are you"
- Capabilities: "what can you do"
- Jokes: "tell me a joke"
- Weather: mentions of "weather", "temperature"

## Testing

### Run chatbot tests
```bash
pytest nlp_chatbot/test_chatbot.py -v
```

### Test coverage
- 18 unit tests
- Intent classification tests
- Response generation tests
- Sentiment analysis tests
- Conversation history tests
- Exit command detection tests

## Code Structure

```
nlp_chatbot/
├── __init__.py              # Package initialization
├── chatbot.py               # Core bot logic (intent classification, responses)
├── sentiment_analyzer.py    # Sentiment analysis engine
├── console_interface.py     # Terminal UI
└── test_chatbot.py          # Unit tests

run_chatbot.py               # Main launcher script
.gitignore                   # Excludes __pycache__ and build artifacts
README.md                    # Comprehensive documentation
requirements.txt             # Dependency notes
```

## Usage as Python Module

```python
from nlp_chatbot import ChatBot, SentimentAnalyzer

# Initialize
bot = ChatBot()
analyzer = SentimentAnalyzer()

# Generate response
response = bot.generate_response("Hello!")
print(response)  # Prints greeting response

# Analyze sentiment
sentiment = analyzer.analyze("I love this!")
print(sentiment)  # {'sentiment': 'positive', 'score': 1.0, 'confidence': 1.0, ...}

# Check exit
if bot.is_exit_command("bye"):
    print("User wants to exit")

# Get history
history = bot.get_conversation_history()
```

## Extending the Bot

### Add new intent
Edit `nlp_chatbot/chatbot.py`:

```python
self.intents['new_intent'] = {
    'patterns': [
        r'\byour_keyword_here\b',
    ],
    'responses': [
        "Your response here",
        "Alternative response",
    ]
}
```

### Add sentiment words
Edit `nlp_chatbot/sentiment_analyzer.py`:

```python
self.positive_words.add('excellent')
self.negative_words.add('disappointing')
```

## Architecture Details

### Intent Classification
- Uses regex pattern matching for robust text analysis
- Case-insensitive matching
- Word boundary detection for accuracy
- First-match priority

### Sentiment Analysis
- Rule-based keyword matching
- Handles negations ("not good" → negative)
- Detects intensifiers ("very good" → stronger positive)
- Confidence scoring based on word counts

### Response Generation
- Random selection from predefined responses
- Fallback responses for unrecognized input
- Maintains conversation context

## Security
- ✅ CodeQL analysis: 0 vulnerabilities found
- Uses only standard library (no external attack surface)
- No network calls or external APIs
- No file system modifications
- No sensitive data storage

## Performance
- Lightweight: < 1MB total size
- Fast response time: < 10ms per interaction
- No dependencies to install
- Works on Python 3.7+

## Demo Output

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║           NLP-Powered Chat Bot v1.0                       ║
║           Console Interface                               ║
║                                                           ║
║   Type your messages and press Enter to chat              ║
║   Type 'exit', 'quit', or 'bye' to end the conversation  ║
║   Type 'help' to see what I can do                        ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

Bot: Hello! I'm ready to chat. How can I help you today?

You: hello there!
Bot: Hi there! What can I do for you?

You: what can you do?
Bot: I can:
- Have conversations with you
- Answer questions
- Provide information on various topics
- Analyze sentiment in your messages
- Help with Python-related queries

You: i love this bot!
[Sentiment detected: positive 😊]
Bot: Interesting! Tell me more about that.

You: thanks!
[Sentiment detected: positive 😊]
Bot: Happy to help!

You: bye
Bot: Goodbye! Have a great day!

Conversation stats: 5 messages exchanged.
```

## Future Enhancements

For production deployment, consider:
- Hugging Face Transformers for advanced NLP
- GPT/BERT models for better understanding
- Vector databases for conversation memory
- REST API interface
- Multi-language support
- Voice interface (speech-to-text/text-to-speech)
- Context persistence across sessions
- User preference learning
- Integration with external APIs

## Contributing
Contributions are welcome! This is part of the python-master-programming repository.

## License
Part of the LESLY16/python-master-programming repository.
