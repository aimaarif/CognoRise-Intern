import streamlit as st
import random

# Function to simulate dice rolls
def roll_dice(num_sides, num_rolls):
    results = [random.randint(1, num_sides) for _ in range(num_rolls)]
    return results

# Streamlit UI with styling and interactivity
def main():
    st.title("Dice Rolling Simulator")

    # User input for number of sides and number of rolls
    num_sides = st.number_input("Number of sides on the dice:", min_value=2, value=6)
    num_rolls = st.number_input("Number of rolls:", min_value=1, value=1)

    # Roll dice button
    if st.button("Roll Dice"):
        results = roll_dice(num_sides, num_rolls)

        # Display results
        st.write(f"Results of rolling a {num_sides}-sided dice {num_rolls} times:")
        st.write(results)

if __name__ == "__main__":
    main()
