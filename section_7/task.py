import random

WORD_LIST = [
    "apple",
    "banana",
    "cherry",
    "grape",
    "lemon",
    "mango",
    "peach",
    "pear",
    "plum",
    "melon",
    "ocean",
    "river",
    "mountain",
    "forest",
    "desert",
    "island",
    "valley",
    "canyon",
    "cliff",
    "beach",
    "chair",
    "table",
    "window",
    "mirror",
    "candle",
    "pillow",
    "sofa",
    "blanket",
    "carpet",
    "ladder",
    "python",
    "coding",
    "script",
    "variable",
    "function",
    "program",
    "developer",
    "software",
    "server",
    "cloud",
    "guitar",
    "piano",
    "drums",
    "violin",
    "trumpet",
    "flute",
    "artist",
    "canvas",
    "palette",
    "studio",
]


word = random.choice(WORD_LIST)
placeholder = "_" * len(word)
lives = 6

while placeholder != word and lives != 0:
    print()
    if lives == 1:
        print(f"You have one life left!!!")
    else:
        print(f"You have {lives} lives left!!!")
    print("Word to guess: " + placeholder)
    letter = input("Guess a letter: ")
    if len(letter) != 1:
        print("You need type one charactor")
    elif letter in placeholder:
        print("You already know this word!")
    elif letter in word:
        indecies = [i for i, v in enumerate(word) if v == letter]
        buff = list(placeholder)
        for index in indecies:
            buff[index] = letter
        placeholder = "".join(buff)
        if placeholder == word:
            print("You Win!")
    else:
        lives -= 1
        print(f"You guessed {letter}, that's not in the word. You lose a life")
        if lives == 0:
            print("Hangman were dead...")
