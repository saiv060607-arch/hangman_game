import random

# List of words
words = ["python", "apple", "college", "computer", "program"]

# Select a random word
word = random.choice(words)

# Create empty guessed word
guessed = ["_"] * len(word)

# Number of chances
chances = 6

print("Welcome to Hangman Game!")

while chances > 0:

    print("\nWord:", " ".join(guessed))
    print("Chances left:", chances)

    guess = input("Guess a letter: ").lower()

    if guess in word:

        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess

    else:
        print("Wrong guess!")
        chances = chances - 1

    # Check whether the word is completed
    if "_" not in guessed:
        print("\nCongratulations! You won!")
        print("The word was:", word)
        break

if chances == 0:
    print("\nGame Over!")
    print("The correct word was:", word)
