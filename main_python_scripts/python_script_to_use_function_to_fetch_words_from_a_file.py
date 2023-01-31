"""Function to fetch words."""
'''
The randint() function which is defined in the python random module can be used to create random strings within a range. 
The function takes two numbers as its input argument. The first input argument is the start of the range and the second input 
argument is the end of the range.
'''
import random
WORDLIST = 'wordlist.txt'
 
def get_random_word(min_word_length):
    """Get a random word from the wordlist using no extra memory."""
    num_words_processed = 0
    curr_word = None
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                print
                continue
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                curr_word = word
    return curr_word
    
print(get_random_word(28))