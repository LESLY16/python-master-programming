#!/usr/bin/env python3
"""
Simple launcher script for the NLP Chat Bot.

This script can be run from the repository root to start the chat bot.
"""

import sys
import os

# Add the repository root to the Python path
repo_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, repo_root)

# Import and run the console interface
from nlp_chatbot.console_interface import main

if __name__ == '__main__':
    main()
