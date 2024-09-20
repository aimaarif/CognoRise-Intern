import streamlit as st
import random

# Function to select a random word from the word list
def select_random_word():
    word_list = ['hangman', 'python', 'streamlit', 'game', 'coding', 'challenge', 'developer']
    return random.choice(word_list)

# Function to initialize game state
def initialize_game():
    st.session_state.word = select_random_word()
    st.session_state.guessed_letters = []
    st.session_state.attempts_left = 6

# Function to display hangman figure
def display_hangman():
    hangman_images = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    st.write(hangman_images[6 - st.session_state.attempts_left])

# Function to display word state
def display_word_state():
    word = st.session_state.word
    guessed_letters = st.session_state.guessed_letters
    word_state = ''
    for letter in word:
        if letter.lower() in guessed_letters:
            word_state += letter + ' '
        else:
            word_state += '_ '
    st.write("Word: ", word_state)

# Function to check letter guess
def check_letter(guess):
    word = st.session_state.word
    if guess.lower() in word.lower():
        st.session_state.guessed_letters.append(guess.lower())
        st.success("Correct guess!")
    else:
        st.session_state.attempts_left -= 1
        st.error("Incorrect guess!")

# Function to check win/loss conditions
def check_win_loss():
    word = st.session_state.word
    guessed_letters = st.session_state.guessed_letters
    if set(word.lower()) == set(guessed_letters):
        st.success("Congratulations! You've won!")
        st.button("Play Again", on_click=initialize_game)
    elif st.session_state.attempts_left == 0:
        st.error(f"Sorry, you've lost. The word was '{word}'.")
        st.button("Play Again", on_click=initialize_game)

# Streamlit UI with styling and interactivity
def main():
    st.title("Hangman Game")

    # Initialize game state
    if 'word' not in st.session_state:
        initialize_game()

    # Display hangman figure
    display_hangman()

    # Display word state
    display_word_state()

    # Display attempts left
    st.write("Attempts left:", st.session_state.attempts_left)

    # User input for letter guess
    guess = st.text_input("Guess a letter:")
    if st.button("Check"):
        if len(guess) == 1 and guess.isalpha():
            check_letter(guess)
            check_win_loss()
        else:
            st.warning("Please enter a single letter.")

    # Play again button
    if st.button("Play Again"):
        initialize_game()

if __name__ == "__main__":
    main()
