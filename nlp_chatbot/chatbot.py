"""
Core Chat Bot Implementation

This module contains the main ChatBot class that handles:
- Intent classification
- Response generation
- Conversation flow management
- Error handling
"""

import re
import random
from typing import Dict, List, Optional, Tuple


class ChatBot:
    """
    NLP-powered chat bot for console interactions.
    
    Features:
    - Intent classification based on keywords and patterns
    - Context-aware responses
    - Error handling with fallback messages
    - Extensible intent/response system
    """
    
    def __init__(self):
        """Initialize the chat bot with predefined intents and responses."""
        self.conversation_history: List[str] = []
        self.context: Dict[str, any] = {}
        
        # Define intents with patterns and responses
        self.intents = {
            'greeting': {
                'patterns': [
                    r'\b(hi|hello|hey|greetings|good morning|good afternoon|good evening)\b',
                ],
                'responses': [
                    "Hello! How can I help you today?",
                    "Hi there! What can I do for you?",
                    "Greetings! How may I assist you?",
                    "Hey! Nice to meet you. What would you like to know?"
                ]
            },
            'goodbye': {
                'patterns': [
                    r'\b(bye|goodbye|see you|farewell|exit|quit)\b',
                ],
                'responses': [
                    "Goodbye! Have a great day!",
                    "See you later! Take care!",
                    "Farewell! It was nice talking to you.",
                    "Bye! Feel free to come back anytime!"
                ]
            },
            'thanks': {
                'patterns': [
                    r'\b(thank|thanks|thx|appreciate)\b',
                ],
                'responses': [
                    "You're welcome!",
                    "Happy to help!",
                    "My pleasure!",
                    "Anytime! Glad I could assist."
                ]
            },
            'help': {
                'patterns': [
                    r'\b(help|assist|support|guide)\b',
                ],
                'responses': [
                    "I can help you with various topics! You can ask me about:\n"
                    "- General questions\n"
                    "- Programming concepts\n"
                    "- Python tips\n"
                    "- Or just chat with me!",
                    "Sure! I'm here to help. What would you like to know about?"
                ]
            },
            'name_query': {
                'patterns': [
                    r'\b(what.*your name|who are you|your name)\b',
                ],
                'responses': [
                    "I'm an NLP-powered chat bot created to assist you!",
                    "You can call me ChatBot. I'm here to help you with various queries.",
                    "I'm an AI assistant designed to have conversations and answer questions."
                ]
            },
            'python_question': {
                'patterns': [
                    r'\b(python|programming|code|script|function|class|variable)\b',
                ],
                'responses': [
                    "Python is a versatile programming language! What specifically would you like to know?",
                    "I can help with Python questions. Could you be more specific?",
                    "Python programming is great! What aspect interests you?"
                ]
            },
            'weather': {
                'patterns': [
                    r'\b(weather|temperature|rain|sunny|cloudy)\b',
                ],
                'responses': [
                    "I don't have access to real-time weather data, but I can chat about weather in general!",
                    "For current weather information, I'd recommend checking a weather service. Is there anything else I can help with?"
                ]
            },
            'capabilities': {
                'patterns': [
                    r'\b(what can you do|your capabilities|your features|what do you know)\b',
                ],
                'responses': [
                    "I can:\n"
                    "- Have conversations with you\n"
                    "- Answer questions\n"
                    "- Provide information on various topics\n"
                    "- Analyze sentiment in your messages\n"
                    "- Help with Python-related queries",
                    "I'm designed to chat, answer questions, and provide helpful information. Try asking me something!"
                ]
            },
            'how_are_you': {
                'patterns': [
                    r'\b(how are you|how do you do|how\'s it going|what\'s up)\b',
                ],
                'responses': [
                    "I'm doing great, thanks for asking! How about you?",
                    "I'm functioning perfectly! How can I help you today?",
                    "All systems operational! What brings you here?"
                ]
            },
            'joke': {
                'patterns': [
                    r'\b(joke|funny|laugh|humor)\b',
                ],
                'responses': [
                    "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
                    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
                    "Why did the Python programmer not respond to my email? He was still waiting for the import to complete!"
                ]
            }
        }
        
        # Fallback responses when no intent is matched
        self.fallback_responses = [
            "I'm not quite sure I understand. Could you rephrase that?",
            "Interesting! Tell me more about that.",
            "I'm still learning. Could you ask that in a different way?",
            "That's an interesting point. What else would you like to know?",
            "I don't have information about that yet. Can I help with something else?"
        ]
    
    def classify_intent(self, user_input: str) -> Optional[str]:
        """
        Classify user input into an intent category.
        
        Args:
            user_input: The user's message
            
        Returns:
            Intent name if matched, None otherwise
        """
        user_input_lower = user_input.lower()
        
        # Check each intent's patterns
        for intent_name, intent_data in self.intents.items():
            for pattern in intent_data['patterns']:
                if re.search(pattern, user_input_lower, re.IGNORECASE):
                    return intent_name
        
        return None
    
    def generate_response(self, user_input: str) -> str:
        """
        Generate a response based on user input.
        
        Args:
            user_input: The user's message
            
        Returns:
            Bot's response
        """
        # Add to conversation history
        self.conversation_history.append(user_input)
        
        # Classify intent
        intent = self.classify_intent(user_input)
        
        # Generate response based on intent
        if intent:
            response = random.choice(self.intents[intent]['responses'])
        else:
            response = random.choice(self.fallback_responses)
        
        return response
    
    def is_exit_command(self, user_input: str) -> bool:
        """
        Check if user wants to exit the conversation.
        
        Args:
            user_input: The user's message
            
        Returns:
            True if exit command detected
        """
        exit_patterns = [
            r'\b(exit|quit|bye|goodbye)\b'
        ]
        
        user_input_lower = user_input.lower()
        for pattern in exit_patterns:
            if re.search(pattern, user_input_lower):
                return True
        return False
    
    def get_conversation_history(self) -> List[str]:
        """
        Get the conversation history.
        
        Returns:
            List of user inputs
        """
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []
        self.context = {}
