# N-gram Frequency Checker

This n-gram checker script allows you to analyze a text file, and provide you with a list of most frequently occurred ngrams of your choice.

This is specially useful if you're into speed typisting as it provides you a way to prioritize which bigrams, trigrams, etc. you want to be most familar with.

## Some Use Cases

1. You want to know which bigrams appear the most in English so you can practice those until they flow smoothly.

2. You noticed you struggle with words containing the letter 'B' by not on every word, only those where certain letters follow the letter 'B'. You can use the ngram checker to find the most frequent bigrams containing 'B'.

3. You struggle with certain words where your index finger is used back to back for two letters. You can use the ngram checker to find the most common bigrams using the letters f, g, r, t, c, or v.

## Usage

Basic usage with default bigram (length=2):

`ngram_check.py sample_text.txt`

will output something like this:

```
1 - he: 13655
2 - th: 12752
3 - in: 8244
4 - er: 8091
5 - an: 7829
6 - re: 5992
7 - nd: 5893
8 - ed: 5800
9 - on: 5162
10 - en: 5034
11 - ou: 4903
12 - hi: 4737
13 - at: 4684
14 - is: 4658
15 - ha: 4523
16 - to: 4509
17 - or: 4085
18 - as: 4009
19 - ar: 4008
20 - te: 3982
```

The numbers and ordering will vary depending on the text file you provided, so try to include text representative of copy you would normally type.

The text file should be a plain text file. You can download free ebooks from [Project Gutenberg](https://www.gutenberg.org/) . You can download books in different formats, but you'll need to convert it to plain text for this script to work.

## Advanced Usage

### Finding bigrams involving the pinky finger

`./ngram_check.py sample_text.txt --includeany q a z`