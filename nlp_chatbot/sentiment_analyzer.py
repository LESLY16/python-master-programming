"""
Sentiment Analysis Module

This module provides sentiment analysis capabilities for chat messages.
It analyzes the emotional tone of user inputs.
"""

import re
from typing import Dict, Tuple


class SentimentAnalyzer:
    """
    Simple rule-based sentiment analyzer for text.
    
    Classifies text as positive, negative, or neutral based on
    keyword matching and basic pattern recognition.
    """
    
    def __init__(self):
        """Initialize sentiment analyzer with word lists."""
        # Positive words
        self.positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic',
            'love', 'like', 'enjoy', 'happy', 'pleased', 'satisfied', 'awesome',
            'brilliant', 'perfect', 'beautiful', 'best', 'incredible', 'nice',
            'positive', 'glad', 'delighted', 'thrilled', 'excited', 'cool',
            'super', 'marvelous', 'outstanding', 'fabulous', 'thank', 'thanks'
        }
        
        # Negative words
        self.negative_words = {
            'bad', 'terrible', 'awful', 'horrible', 'poor', 'worst', 'hate',
            'dislike', 'angry', 'sad', 'unhappy', 'disappointed', 'frustrated',
            'annoyed', 'upset', 'disgusted', 'pathetic', 'useless', 'waste',
            'fail', 'failed', 'failure', 'wrong', 'error', 'problem', 'issue',
            'difficult', 'hard', 'negative', 'boring', 'dull', 'stupid'
        }
        
        # Intensifiers
        self.intensifiers = {
            'very', 'really', 'extremely', 'absolutely', 'completely',
            'totally', 'incredibly', 'highly', 'super', 'too'
        }
        
        # Negations
        self.negations = {
            'not', 'no', 'never', 'neither', 'nobody', 'nothing',
            'nowhere', 'hardly', 'barely', 'scarcely', "don't", "doesn't",
            "didn't", "won't", "wouldn't", "can't", "cannot", "couldn't"
        }
    
    def analyze(self, text: str) -> Dict[str, any]:
        """
        Analyze sentiment of the given text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary with sentiment label, score, and confidence
        """
        if not text or not text.strip():
            return {
                'sentiment': 'neutral',
                'score': 0.0,
                'confidence': 0.0
            }
        
        # Tokenize and clean text
        words = self._tokenize(text.lower())
        
        # Calculate sentiment score
        score, details = self._calculate_sentiment_score(words)
        
        # Determine sentiment label
        if score > 0.3:
            sentiment = 'positive'
        elif score < -0.3:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        # Calculate confidence
        confidence = min(abs(score), 1.0)
        
        return {
            'sentiment': sentiment,
            'score': score,
            'confidence': confidence,
            'details': details
        }
    
    def _tokenize(self, text: str) -> list:
        """
        Tokenize text into words.
        
        Args:
            text: Input text
            
        Returns:
            List of words
        """
        # Remove punctuation and split
        words = re.findall(r'\b\w+\b', text.lower())
        return words
    
    def _calculate_sentiment_score(self, words: list) -> Tuple[float, dict]:
        """
        Calculate sentiment score from words.
        
        Args:
            words: List of words
            
        Returns:
            Tuple of (score, details_dict)
        """
        positive_count = 0
        negative_count = 0
        intensifier_multiplier = 1.0
        negation_active = False
        
        details = {
            'positive_words_found': [],
            'negative_words_found': [],
            'negations_found': []
        }
        
        for i, word in enumerate(words):
            # Check for intensifiers
            if word in self.intensifiers:
                intensifier_multiplier = 1.5
                continue
            
            # Check for negations
            if word in self.negations:
                negation_active = True
                details['negations_found'].append(word)
                continue
            
            # Check sentiment words
            if word in self.positive_words:
                score = 1.0 * intensifier_multiplier
                if negation_active:
                    negative_count += score
                    details['negative_words_found'].append(f"NOT {word}")
                else:
                    positive_count += score
                    details['positive_words_found'].append(word)
                intensifier_multiplier = 1.0
                negation_active = False
                
            elif word in self.negative_words:
                score = 1.0 * intensifier_multiplier
                if negation_active:
                    positive_count += score
                    details['positive_words_found'].append(f"NOT {word}")
                else:
                    negative_count += score
                    details['negative_words_found'].append(word)
                intensifier_multiplier = 1.0
                negation_active = False
            else:
                # Reset negation if we encounter non-sentiment word
                if negation_active and i > 0:
                    negation_active = False
                intensifier_multiplier = 1.0
        
        # Calculate final score
        total_sentiment_words = positive_count + negative_count
        if total_sentiment_words > 0:
            score = (positive_count - negative_count) / total_sentiment_words
        else:
            score = 0.0
        
        return score, details
    
    def get_emoji(self, sentiment: str) -> str:
        """
        Get emoji representation for sentiment.
        
        Args:
            sentiment: Sentiment label
            
        Returns:
            Emoji string
        """
        emoji_map = {
            'positive': '😊',
            'negative': '😞',
            'neutral': '😐'
        }
        return emoji_map.get(sentiment, '🤖')
