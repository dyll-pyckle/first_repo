import random
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

list_of_words = [
    "apple", "grape", "stone", "water", "cloud", "light", "dream", "smile", 
    "chair", "table", "bread", "plant", "green", "river", "ocean", "storm", 
    "dance", "music", "voice", "laugh", "heart", "spark", "flame", "bliss", 
    "peace", "magic", "story", "world", "flora", "fauna", "sunny", "rainy", 
    "windy", "clear", "snowy", "petal", "leafy", "roots", "spice", "sugar",
    "amber", "pearl", "coral", "ivory", "onyx", "velvet", "linen", "silk", 
    "wool", "cotton"
]
tries = 0
choice1 = input("Do you want to 1. choose a word or 2. have it randomly selected for you? (enter 1 or 2): ")
if choice1 == "1":
    chosen_word = input("Enter your word: ").lower().strip()
else:
    chosen_word = random.choice(list_of_words)
wrong_letters = []

length = len(chosen_word)

hidden_list = list("_"*length)
hangmanpics_index = 0

found_list = []
guessed_letters = set()
won = False

while hangmanpics_index < 6 and not won:
    print("\n" + HANGMANPICS[hangmanpics_index])
    print(" ".join(hidden_list))
    if wrong_letters:
        print(f"Wrong guesses: {' '.join(wrong_letters)}")

    while True:
        choice = input("\nWhich letter do you guess? ").lower().strip()
        if len(choice) != 1 or not choice.isalpha():
            print("Please enter a single letter (a-z)!")
            continue
        if choice in guessed_letters:
            print(f"You already guessed '{choice}'!")
            continue
        guessed_letters.add(choice)
        break

    if choice in chosen_word:
        print("Good guess!")
        for idx, letter in enumerate(chosen_word):
            if letter == choice:
                hidden_list[idx] = choice
        print(" ".join(hidden_list))
    else:
        
        print("Wrong guess!")
        wrong_letters.append(choice)
        hangmanpics_index += 1
        
    if hangmanpics_index == 6:
        print(HANGMANPICS[6])
        print("you lose!")
        break
    if hidden_list == list(chosen_word):
        print("you win!")
        won = True
print(f"the word was {chosen_word}.")
