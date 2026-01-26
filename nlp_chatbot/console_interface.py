#!/usr/bin/env python3
"""
Console Interface for NLP Chat Bot

This script provides a console-based interface for interacting with the chat bot.
Users can type messages and receive responses in real-time.
"""

import sys
from nlp_chatbot import ChatBot, SentimentAnalyzer


def print_banner():
    """Display welcome banner."""
    banner = """
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
    """
    print(banner)


def print_separator():
    """Print a separator line."""
    print("-" * 60)


def run_chatbot(enable_sentiment: bool = True):
    """
    Run the chat bot in console mode.
    
    Args:
        enable_sentiment: Whether to enable sentiment analysis
    """
    print_banner()
    
    # Initialize bot and analyzer
    bot = ChatBot()
    sentiment_analyzer = SentimentAnalyzer() if enable_sentiment else None
    
    print("Bot: Hello! I'm ready to chat. How can I help you today?\n")
    
    conversation_count = 0
    
    try:
        while True:
            # Get user input
            try:
                user_input = input("You: ").strip()
            except EOFError:
                # Handle Ctrl+D
                print("\n\nBot: Goodbye! Have a great day!")
                break
            
            # Skip empty inputs
            if not user_input:
                continue
            
            conversation_count += 1
            
            # Check for exit command
            if bot.is_exit_command(user_input):
                print("\nBot: " + bot.generate_response(user_input))
                print(f"\nConversation stats: {conversation_count} messages exchanged.")
                break
            
            # Perform sentiment analysis if enabled
            if sentiment_analyzer:
                sentiment_result = sentiment_analyzer.analyze(user_input)
                sentiment_label = sentiment_result['sentiment']
                emoji = sentiment_analyzer.get_emoji(sentiment_label)
                
                # Show sentiment only if it's notably positive or negative
                if sentiment_result['confidence'] > 0.5:
                    print(f"[Sentiment detected: {sentiment_label} {emoji}]")
            
            # Generate and display response
            response = bot.generate_response(user_input)
            print(f"\nBot: {response}\n")
    
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\nBot: Conversation interrupted. Goodbye!")
        print(f"Conversation stats: {conversation_count} messages exchanged.")
    
    except Exception as e:
        print(f"\n\nError occurred: {str(e)}")
        print("Bot: Sorry, I encountered an error. Please try again.")
        sys.exit(1)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='NLP-Powered Chat Bot Console Interface',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python console_interface.py                  # Run with sentiment analysis
  python console_interface.py --no-sentiment   # Run without sentiment analysis
        """
    )
    
    parser.add_argument(
        '--no-sentiment',
        action='store_true',
        help='Disable sentiment analysis'
    )
    
    args = parser.parse_args()
    
    # Run the chatbot
    run_chatbot(enable_sentiment=not args.no_sentiment)


if __name__ == '__main__':
    main()
