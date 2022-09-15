challenge_input = [
    "The daily diary of the American dream",
    "For the sky and the sea, and the sea and the sky",
    "Three grey geese in a green field grazing, Grey were the geese and green was the grazing.",
    "But a better butter makes a batter better.",
    "His soul swooned slowly as he heard the snow falling faintly through the universe and faintly falling, like the descent of their last end, upon all the living and the dead.",
    "Whisper words of wisdom, let it be.",
    "They paved paradise and put up a parking lot.",
    "So what we gonna have, dessert or disaster?",
]


stop_words = [
    "i",
    "a",
    "about",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "com",
    "for",
    "from",
    "how",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "was",
    "what",
    "when",
    "where",
    "who",
    "will",
    "with",
]


def alit(sentence):
    alit = []
    words = sentence.split()
    words = [w.lower() for w in words if w.lower() not in stop_words]
    for i, word in enumerate(words[:-1], start=1):
        if word[0] == words[i][0]:
            if word not in alit:
                alit.append(word)
            if words[i] not in alit:
                alit.append(words[i])
    return alit


for sentence in challenge_input:
    print(alit(sentence))
