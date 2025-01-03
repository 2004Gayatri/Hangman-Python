import random

def hangman():
    # List of words for the game
    word_list = ['python', 'hangman', 'programming', 'internship', 'challenge']
    word_to_guess = random.choice(word_list)
    guessed_word = ['_'] * len(word_to_guess)
    attempts_remaining = 6  # Limit on incorrect guesses
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("Guess the word: " + " ".join(guessed_word))

    while attempts_remaining > 0 and '_' in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts_remaining -= 1
            print(f"Wrong guess! '{guess}' is not in the word. Attempts remaining: {attempts_remaining}")

        print("Current word: " + " ".join(guessed_word))

    if '_' not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word_to_guess)
    else:
        print("\nGame over! The word was:", word_to_guess)

# Run the game
hangman()
