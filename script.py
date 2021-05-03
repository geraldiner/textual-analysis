import nltk
from collections import Counter


def read_text():
    with open("corpus/heart_of_darkness.txt", "r", encoding="utf-8") as f:
        book = f.read()
    f.close()
    return book


def tokenize_text(book):
    return nltk.word_tokenize(book)


def tag_text(tokenize):
    return nltk.pos_tag(tokenize)


def find_proper_nouns(tagged_text):
    proper_nouns = []
    i = 0
    while i < len(tagged_text):
        if tagged_text[i][1] == "NNP":
            if tagged_text[i + 1][1] == "NNP":
                proper_nouns.append(
                    tagged_text[i][0].lower() + " " + tagged_text[i + 1][0].lower()
                )
                i += 1  # extra increment added to the i counter to skip the next word
            else:
                proper_nouns.append(tagged_text[i][0].lower())
        i += 1  # increment the i counter
    return proper_nouns


def summarize_text(proper_nouns, top_num):
    return dict(Counter(proper_nouns).most_common(top_num))


book = read_text()
tokenize = tokenize_text(book)
tagged = tag_text(tokenize)
proper_nouns = find_proper_nouns(tagged)
top_num = summarize_text(proper_nouns, 50)

with open("heart_of_darkness_counts.txt", "a", encoding="utf-8") as outputFile:
    for x in top_num:
        outputFile.write(x + ": " + str(top_num[x]) + "\n")
outputFile.close()
