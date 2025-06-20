import random
print("Wellcome to the hangman game")
logo = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       '''
print("Hangman")
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# List of random words
world_list = ["aardvark",
        "baboon",
        "camel",
        "cat",
        "dog",
        "sun",
        "run",
        "book",
        "tree",
        "ball",
        "fish",
        "milk",
        "bed",
        "toy",
        "chair",
        "box",
        "red",
        "big",
        "jump",
        "cake",
        "star",
        "hand",
        "hat"]
lives = 6
word=random.choice(world_list)
print(word)

placeholder = ""
for position in range(len(word)):
    placeholder += " _ "
print(placeholder)
game_over=False
correct_number = []

Game loop
while not game_over:
    print("*****************************{lives}//6 LIFE LFET*************************")
    user_input = input("Guess a latter: ")

    #User Already Guessed Number
    if user_input in correct_number:
        print(f"You have already guessed {user_input}")
    display =" "
    for num in word:
        if num ==user_input:
            display += num
            correct_number.append(user_input)
        elif num in correct_number:
            display += num
        else:
            display += "_"
    print(display)


    if word not in user_input:
        lives -= 1
        print(f"You guessed {user_input}, that is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("*************************IT WAS {user_input} //YOU LOSE************************************** ")

    if "_" not in display:
        game_over = True
        print("*****************************YOU WON****************************************")

    print(stages[lives])