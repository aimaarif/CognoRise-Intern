import streamlit as st
import time

# Function to convert hours:minutes:seconds to seconds
def convert_to_seconds(time_str):
    if time_str:
        parts = time_str.split(':')
        if len(parts) == 3:
            h, m, s = map(int, parts)
            return h * 3600 + m * 60 + s
        else:
            st.warning("Invalid format! Please enter the duration in HH:MM:SS format.")
            return 0
    else:
        return 0


# Function to format time as HH:MM:SS
def format_time(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)

# Streamlit UI with styling and interactivity
def main():
    st.title("Countdown Timer")

    # User input for countdown duration
    duration_str = st.text_input("Enter countdown duration (in HH:MM:SS format):", value="00:05:00")
    duration_seconds = convert_to_seconds(duration_str)

    if st.button("Start Countdown"):
        start_time = time.time()

        # Create a placeholder for displaying countdown
        countdown_placeholder = st.empty()

        while True:
            elapsed_time = time.time() - start_time
            remaining_time = max(duration_seconds - elapsed_time, 0)

            # Update countdown placeholder
            countdown_placeholder.write("Time remaining: " + format_time(remaining_time))

            if remaining_time == 0:
                st.success("Countdown completed!")
                break

            time.sleep(1)  # Update every second

if __name__ == "__main__":
    main()
