import random
import re


def guess_status(lst_guess, question):
    lst_words_question = list()
    r = list()
    for i in range(len(question)):
        r.append('*')
    correct = 0
    for i in range(len(question)):
        lst_words_question.append(question[i])
    for j in lst_guess:

        matches = re.finditer(j, question)
        matches_positions = [match.start() for match in matches]

        if not len(matches_positions) == 0:
            for k in matches_positions:
                r[k] = j
                correct = correct+1
    r_final = str
    r_final = ''.join(r)
    return r_final


print('|=======================|\n| Welcome to Hangman!!! |\n|=======================|')
print("\n-----You get 7 chances to guess the mystery word-----\n")

print('To add your custom words run addWord.py \n')
name = input("Enter User Name: ")
print("\n---------WELCOME,"+name + '---------\n')
f = open("words.txt", "r")

lst_of_words = list()
for line in f:

    lst_of_words.append(line.strip())

question = random.choice(lst_of_words).lower()
len_of_word = len(question)
lst_guess = list()
print("the Length of the word is:")
status = guess_status(lst_guess, question)
print(status)

print('\n')
turns = 7
while turns > 0:
    flag = True
    prev_status = guess_status(lst_guess, question)
    while flag:

        print("Turns left:", turns, '\n')
        letter = input('Guess a letter: ').lower()
        if letter in lst_guess:

            print("Letter already Guessed")
            print("Try Again \n")
        elif letter.lower() in lst_guess:
            turns = turns+1
            print("Letter already Guessed")
            print("Try Again \n")
        else:
            flag = False
    lst_guess.append(letter)
    status = guess_status(lst_guess, question)
    if prev_status == status:
        turns = turns-1

    print("Status:", status)
    if status == question:
        print("\nCongratulations you have guessed the correct answer")
        break
    else:
        continue


if(turns == 0):
    print('You have lost')
    print("\n The correct answer was:", question)
