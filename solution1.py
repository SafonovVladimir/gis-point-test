from collections import Counter

paragraph = ["The quick brown fox",
             "jumps over the lazy dog.",
             "The dog barks,",
             "and the fox runs away."
             ]


def word_frequency(paragraph: list) -> None:
    words_dict = dict(Counter(word.lower() for line in paragraph for word in
                              line.strip(".,").split()))
    print("{")
    for word, value in words_dict.items():
        print(f"\t{word}: {value}")
    print("}")


frequency = word_frequency(paragraph)
