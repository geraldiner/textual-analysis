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

<pre>
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
</pre>

The author has some reasoning to not exclude punctuation in the beginning because of the way the NLTK algorithm understands a list of names. 

> An important note here: people sometimes remove punctuation when doing a textual analysis, but here’s why I didn’t. Consider this commonly occurring phrase in all of the Potter books: “Harry, Ron and Hermione”. The comma here is pretty important used in conjunction with NLP. If I leave the sentence as-is, NLP reads it as NNP — , — NNP — CC — NNP , where CC is a conjunction. But, if I take out the comma, I get NNP — NNP — CC — NNP . With this input, my algorithm above would read ‘Harry Ron’ as a single noun, like ‘Uncle Vernon’.

Without the comma, 'Harry, Ron...' would become 'Harry Ron...' which my code would pick up as a single proper noun (like someone with two first names).

I'm wondering now if I could do this on the list of proper nouns. Apparently apostrophes and quotation marks are some of the most prominent `char`acters in the text. But if you've read *Heart of Darkness*, you'd know that it's probably Kurtz, who does come in second.

## How is this going to help me?
Right now I have a bunch of comments that may or may not have a movie title in them. I thought the IDs I got from Pushshift were only for top level comments, but after looking over some, it seems like some might have been replies to other comments (eg. 'I really have to see that one!').

I could try to find proper nouns here too, but movie titles can have more than two nouns in them, and I'm not sure how to handle that yet.

For now, I'll keep reading the NLTK Book and looking for other examples of textual analysis














## Other Projects

Check out other stuff I've worked on:

**Secret Santa App**: https://github.com/geraldiner/secret-santa-app

**Minute To Win It Games API & Wiki**: https://github.com/geraldiner/min-to-win

## Currently I'm:

- Working full-time at <a target="_blank" href="https://nomnomnow.com">Nom Nom</a>, migrating JavaScript to TypeScript
- Building my brand, <a target="_blank" href="https://happiandco.com">Happi & Co. Studio LLC</a>

But I'm always open to hearing about your next big thing!

## Let's get to know each other!

Connect with me:

**Twitter**: [@GeraldineDesu](https://twitter.com/geraldinedesu)

**LinkedIn**: [in/GeraldineR](https://linkedin.com/in/geraldiner)

**Email**: hello [at] geraldiner [dot] com
