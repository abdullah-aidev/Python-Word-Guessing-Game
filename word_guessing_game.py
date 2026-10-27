import random

# Step 1: Store five words in a list
words = ["python", "apple", "computer", "coding", "program"]

# Step 2: Select a random word
secret_word = random.choice(words)

# Step 3: Initialize game variables
attempts = 6
guessed_letters = []

print("================================")
print("   WELCOME TO WORD GUESS GAME")
print("================================")

print("Guess the hidden word!")
print("The word contains", len(secret_word), "letters.")
print("You have 6 incorrect guesses available.")

# Step 4: Main game loop
while attempts > 0:

    # Display the current word progress
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Step 5: Check if the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word!")
        print("The hidden word was:", secret_word)
        break

    # Step 6: Get input from the player
    guess = input("Guess a letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Save the guessed letter
    guessed_letters.append(guess)

    # Step 7: Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")
        print("Incorrect guesses remaining:", attempts)

# Step 8: End the game if attempts run out
if attempts == 0:
    print("\nGame Over!")
    print("The hidden word was:", secret_word)

print("\nThanks for playing!")
