# Task 1 Hangman Game
# Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time.
# Simplified Scope:
# ● Use a small list of 5 predefined words (no need to use a file or API).
# ● Limit incorrect guesses to 6.
# ● Basic console input/output — no graphics or audio.
# Key Concepts Used: random, while loop, if-else, strings, lists.



import random

words = ["apple", "python", "house", "flower", "computer"]

secret_word = random.choice(words)

guessed_letters = []

lives = 6 # 6 time user try 

print("🎮 Welcome to Hangman!")
print("Guess the hidden word!")

# game loop , game will run 6 times
while lives > 0:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Lives Left:", lives)

    # When user guessed whole letter
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    # 
    guess = input("Enter a letter: ").lower()

    # Check if the user already guessed the letter
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    # Its save the letter into guessed
    guessed_letters.append(guess)

    # When user enter thr correct word
    if guess in secret_word:
        print("User Guess Correct ✅ ")
    else:
        print("User Guess Wrong ❌ ")
        lives -= 1


if lives == 0:
    print("\n💀 Game Over!")
    print("The word was:", secret_word)