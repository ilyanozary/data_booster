# text_augment.py - Text Augmentation Module

import random
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

def augment_text(text):
    """
    Applies text augmentation techniques to generate variations of the given text.
    Techniques used:
    1. Synonym replacement
    2. Random word deletion
    
    Args:
        text (str): The input text to augment.
    
    Returns:
        list: A list of augmented text variations.
    """
    words = text.split()
    augmented_texts = []
    
    # Synonym replacement
    new_words = []
    for word in words:
        synonyms = wordnet.synsets(word)
        if synonyms:
            new_words.append(synonyms[0].lemmas()[0].name())  # Replace with first synonym found
        else:
            new_words.append(word)
    augmented_texts.append(" ".join(new_words))
    
    # Random word deletion
    if len(words) > 3:
        idx = random.randint(0, len(words)-1)
        new_sentence = " ".join([words[i] for i in range(len(words)) if i != idx])
        augmented_texts.append(new_sentence)
    
    return augmented_texts