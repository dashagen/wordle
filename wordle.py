#!/usr/bin/python
import random

### Terminal printing Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKGRAY = '\033[97m'
    OKDGRAY = '\033[90m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


### Load 5 letter words
word_list = []
f = open("5_letter_words.txt")
for w in f:
    word_list.append(w.rstrip().upper())


### pick a word
answer = random.choice(word_list)


### Guessing begins
guess = ""
book  = [ ];

print(" ")

while (guess != answer):

    # ask for input
    guess = input(bcolors.OKGRAY + "input your guess please! ").upper()

    # tell the answer if asked
    if guess == "TELL ME":
        print("ansewr is "+ answer)
        break

    # ask again if not the right length
    if len(guess) != 5:
        continue

    # ask again if not a word
    if guess not in word_list:
        continue

    # Check matching situations
    check = ""

    for i in range(5):
        if guess[i] == answer[i]:
            check = check + bcolors.OKGREEN + guess[i]
        else:
            if guess[i] in answer:
                check = check + bcolors.WARNING + guess[i]
            else:
                check = check + bcolors.OKDGRAY + guess[i] 

    # append new guess
    book.append(check)
            
    # print all guesses
    for chk in book:
        print(chk)

