#!/usr/bin/python
import random

### Terminal printing Colors
class bcolors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    GRAY = '\033[97m'
    DGRAY = '\033[90m'
    YELLOW = '\033[93m'
    WHITE = '\033[37m'
    BLACK = '\033[30m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

### Function to print keyboard
def keyboard():
    for l in alphabet:
        if l == "A":
            print("\n", end= " ")
        elif l == "Z":
            print("\n", end= "  ")

        if (status[l] == 0):
            print(bcolors.WHITE + l ,end=" ")
        elif (status[l] == 1):
            print(bcolors.GREEN + l ,end=" ")
        elif (status[l] == 2):
            print(bcolors.YELLOW + l ,end=" ")
        elif (status[l] == 3):
            print(bcolors.DGRAY + l ,end=" ")
    print()
    print()


### Function to print guesses
def print_guess():

    for i in range(len(guess_book)):

        chk = check_book[i]
        gus = guess_book[i]

        for j in range(5):
            if (chk[j] == 0):
                print(bcolors.WHITE + gus[j] ,end=" ")
            elif (chk[j] == 1):
                print(bcolors.GREEN + gus[j] ,end=" ")
            elif (chk[j] == 2):
                print(bcolors.YELLOW + gus[j] ,end=" ")
            elif (chk[j] == 3):
                print(bcolors.DGRAY + gus[j] ,end=" ")
        print()
    print()


### Load 5 letter words
f = open("common_5_letter_words.txt")
word_list = [w.rstrip().upper() for w in f]

### pick a word
answer = random.choice(word_list)

### Create status check
alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM";
status = dict(zip(alphabet, [0]*26))


### Guessing begins
guess = ""

guess_book  = [ ];
check_book  = [ ];


while (guess != answer):

    # ask for input
    guess = input(bcolors.GRAY + "Input your guess please! ").upper()

    # tell the answer if asked
    if guess == "TELL ME":
        print("The ansewr is " + bcolors.GREEN + answer)
        break

    # ask again if not the right length
    if len(guess) != 5:
        continue

    # ask again if not a word
    if guess not in word_list:
        continue

    # Check matching situations
    check = [0]*5

    for i in range(5):
        if guess[i] == answer[i]:
            check[i] = 1
            status[guess[i]] = 1
        else:
            if guess[i] in answer:
                check[i] = 2
                if status[guess[i]] != 1:
                    status[guess[i]] = 2
            else:
                check[i] = 3
                status[guess[i]] = 3

    # append new guess
    check_book.append(check)
    guess_book.append(guess)
            
    # print all guesses
    print_guess()

    # Show keyboard
    keyboard()

