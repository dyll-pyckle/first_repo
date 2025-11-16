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
while True:
    choice1 = input("Enter 1 to choose your own word, or 2 for a random word: ")
    if choice1 == "1":
        chosen_word = input("Enter your word: ").lower().strip()
        break
    elif choice1 == "2":
        chosen_word = random.choice(list_of_words)
        break
    else:
        print(f"Sorry, {choice1} was not an option. please try again.")
        continue
wrong_letters = []
length = len(chosen_word)
hidden_list = list("_"*length)
hangmanpics_index = 0
guessed_letters = set()
won = False

while hangmanpics_index < 6 and not won:
    print("\n" + HANGMANPICS[hangmanpics_index])
    print(" ".join(hidden_list))
    if wrong_letters:
        print(f"Wrong guesses: {' '.join(wrong_letters)}")
            
    while True:
        choice = input("\nWhich letter do you guess?: ").lower().strip()
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
        print("You lose!")
        break
    if hidden_list == list(chosen_word):
        print("You win!")
        won = True
        break
print(f"The word was {chosen_word}.")