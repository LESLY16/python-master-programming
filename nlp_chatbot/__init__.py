"""
NLP-powered Chat Bot Module

This module provides a full-featured natural language processing chat bot
that can interact with users via console interface.
"""

from .chatbot import ChatBot
from .sentiment_analyzer import SentimentAnalyzer

__all__ = ['ChatBot', 'SentimentAnalyzer']
__version__ = '1.0.0'
