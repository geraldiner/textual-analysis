# Textual Analysis

This is a continuation from my [last venture](https://github.com/geraldiner/python-test) into learning more Python to figure out how to handle my Magical Movies project.

tldr; I want to take the list of magical movies as suggested by Redditors, watch them, and see how 'magical' they actually turn out to be.

I followed this [tutorial about textual analysis](https://medium.com/agatha-codes/using-textual-analysis-to-quantify-a-cast-of-characters-4f3baecdb5c) with the [Natural Language Toolkit](https://www.nltk.org/).

The tutorial walked me through the ultimate goal of counting the number of times a character appears in a text. They used *Harry Potter and the Sorcerer's Stone*, and I decided to use *Heart of Darkness*.

To do this, we had to:
1. Read the text - taken from [Project Gutenberg](https://www.gutenberg.org/)

2. 'Tokenize' the text - break the text into individual words and punctuation (basically a `split` function)

3. 'Tag' the text - associate each of the tokenized words with a tag (part of speech, punctuation, etc.) for the NLTK algorithm

4. Find the proper nouns based on the tags in the previous step. 

There was a good point brought up that some proper nouns actually came as two words, so we had to add some tests to check what the next word was.

5. Finally, count the number of times each proper noun existed in the list.

6. I added the extra step of printing the results to a text file that was easier to read.

```markdown
’: 135
kurtz: 50
project gutenberg-tm: 48
mr. kurtz: 47
‘: 34
project gutenberg: 27
foundation: 23
’ ‘: 21
’ “: 16
united: 15
kurtz ’: 14
literary archive: 13
license: 9
well: 9
don ’: 8
europe: 8
did: 8
* *: 7
my: 7
ah: 7
```