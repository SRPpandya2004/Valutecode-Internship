
#1. Write a program to count word frequencies in a given text.

def count_word_frequencies(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        word = word.strip('.,!?";:')
        freq[word] = freq.get(word, 0) + 1

    return freq


# Example usage
text = "How are you,what are you doing? How are you?"
frequencies = count_word_frequencies(text)
print(frequencies)
