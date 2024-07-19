#Day 1 of Hangman code below!
word_list = ['beekeeper', 'dog', 'cat', 'father', 'mother']
import random
chosen_word = random.choice(word_list).lower()
#Day 2 of Hangman code below!
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
guess = input("Guess a letter: ").lower()
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        print(f"Guessed letter: {guess}")
print(display)
#Day 3 of Hangman code below!
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
import random
word_list = ["beekeeper", "dog", "cat", "father", "mother"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display += "_"
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")
#Day 4 of Hangman code below!
