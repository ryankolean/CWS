def spin_words(sentence):
    words = sentence.split(" ")
    for idx, w in enumerate(words):
        if len(w) > 4:
            words[idx] = w[::-1]
    return " ".join(words)