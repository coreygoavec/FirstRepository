import random
import time

# Main loop to ask the user if they want to play
while True:
    play_again = input("Would you like to play Powerball? (yes/no): ").lower()

    if play_again != 'yes':
        print("Goodbye!")
        break  # Exit the loop if the user doesn't want to play

    # Display a message to the user
    print("Generating your Powerball number:")

    # Generate and display five random numbers with delays
    for _ in range(5):
        number = random.randint(1, 69)
        print(number, end="  ", flush=True)  # Use end=" " to keep numbers on the same line
        time.sleep(1)  # Add a delay of 1 second

    # Generate and display the Powerball number with a longer delay and four spaces
    powerball_number = random.randint(1, 26)
    print(f"    {powerball_number}")
    time.sleep(2)  # Add a longer delay of 2 seconds

    # Ask if the user wants to play again
    play_again = input("Would you like to play again? (yes/no): ").lower()

    if play_again != 'yes':
        print("Goodbye!")
        break  # Exit the loop if the user doesn't want to play again
