word_list = ['beekeeper', 'dog', 'cat', 'father', 'mother']
import random
chosen_word = random.choice(word_list).lower()
guess = input("Guess a lettter: ").lower
for letter in chosen_word:
  if letter == guess:
      print("Right")
  else:
      print("Wrong")
