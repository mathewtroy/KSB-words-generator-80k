try:
    import nltk
    nltk.download('words', quiet=True)
    from nltk.corpus import words
except ImportError:
    print("Please install the NLTK library by running 'pip install nltk'")
    exit()

import random

# Get the list of English words
word_list = words.words()

# Filter words with length between 3 and 7 letters and convert to uppercase
filtered_words = [word.upper() for word in word_list if 3 <= len(word) <= 8]

# Remove duplicates and shuffle the list
unique_words = list(set(filtered_words))
random.shuffle(unique_words)

# Select up to 80,000 words
selected_words = unique_words[:80000]

# Write the words to 'test.txt' in the specified format
with open('test.txt', 'w') as f:
    f.write('popular_keywords = [\n')
    for word in selected_words:
        f.write(f'    "{word}",\n')
    f.write(']')
