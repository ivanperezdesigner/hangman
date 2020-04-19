import random
from random_words import RandomWords
rw = RandomWords()
word = rw.random_word()

hidden = word
corr_word = ''
all_letters = ''
wrong_word = ''
tries = 0


print("H A N G M A N")
while True:
    inp = input('Type "play" to play the game, "exit" to quit: ')
    if inp == 'play':
        break
    elif inp == 'exit':
        exit()

while tries < 8:
    print(word)  # For testing
    result = ''
    for l in hidden:
        if l in corr_word:
            result += l
        else:
            result += '-'
    print()
    print('{}'.format(result))

    while True:
        user_letter = input('Input a letter: ')
        all_letters += user_letter
        break
    if len(user_letter) > 1:
        print('You should print a single letter')
    elif not user_letter.isalpha():
        print('It is not an ASCII lowercase letter')
    elif not user_letter.islower():
        print('It is not an ASCII lowercase letter')
    elif user_letter in corr_word:
        print('You already typed this letter')
    elif user_letter not in hidden:
        if user_letter in wrong_word:
            print('You already typed this letter')
        else:
            print('No such letter in the word')
            tries += 1
            print('You have', 8 - tries, 'tries')
        wrong_word += user_letter
    elif user_letter in corr_word:
        print('No improvements')
    else:
        corr_word += user_letter

    if result == hidden:
        print('You guessed the word!')
        print('You survived!')
        break
    if tries == 8:
        print('You are hanged! the word is', word)
