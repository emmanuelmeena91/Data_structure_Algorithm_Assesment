import string

def word_frequency(sentence):
    frequency = {}
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.lower().split()

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


# Testing the function
sentence = "This is a car. This car is a test."
result = word_frequency(sentence)
print(result)