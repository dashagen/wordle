#!/usr/bin/python
import random
import os
import numpy as np
import pandas as pd


## match pattern
def match_pattern(answer, guess):
    
    pattern = ""

    for i in range(5):
        if guess[i] == answer[i]:
            pattern = pattern + "2"
        elif guess[i] in answer:
            pattern = pattern + "1"
        else:
            pattern = pattern + "0"

    return(pattern)


### Load 5 letter words
f = open("./simple_5_letter_words.txt")
word_list = [w.rstrip().upper() for w in f]

### A random sample of word list as test list
test_list = word_list


### Initialize full patterns
full_patterns = [""] * len(word_list)

top5_word = []


### Find 5 openers in sequence
for i in range(5):

    print(i)

    ##initialize opener scores
    opener_scores = []

    ## Get opener score for each word in wordlist
    for opener in word_list:

        # get match pattern of each word in test_list for the specific opener
        patterns = [match_pattern(x, opener) for x in test_list]

        # combine with patterns based on previous found openers
        new_full_patterns = [ full_patterns[i] + patterns[i] for i in range(len(test_list))]


        ## Calculate the score by using the freq table trick
        ##  - Basically it's the expected number of guesses if a random word
        ##    from the test_list is chosen as the answer, aka expected 
        ##    number of words matching the pattern

        # Frequency table of new full patterns
        pat_counts = pd.Series(new_full_patterns).value_counts()

        # calculate score
        score = sum( [ x*x for x in pat_counts] )

        # append to list
        opener_scores.append(score)


    ## Sort opener by score
    df = pd.DataFrame( {"word":word_list, "score":opener_scores})
    ndf = df.iloc[(df['score']).argsort()]
    ndf = ndf.set_index(pd.Index(range(len(ndf))))

    ## Get the best opener (smallest score)
    new_word = ndf.word[0]
    print(new_word)

    top5_word.append(new_word);

    ## update full patterns
    patterns = [match_pattern(x, new_word) for x in test_list]
    full_patterns = [ full_patterns[i] + patterns[i] for i in range(len(test_list))]

print(top5_word)

