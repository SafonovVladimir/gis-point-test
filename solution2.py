from collections import Counter

paragraph = ["The quick brown fox",
             "jumps over the lazy dog.",
             "The dog barks,",
             "and the fox runs away."
             ]


def word_frequency(paragraph: list) -> dict:
    return (dict(Counter(word.lower() for line in paragraph
                         for word in line.strip(".,").split())))


frequency = word_frequency(paragraph)
print(frequency)
