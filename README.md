# Find-the-number-game
This Python code implements a number guessing game where the computer selects a random number between 1 and 50, and the user tries to guess it.Here’s a detailed description of the code: <br><br>Code Breakdown:-
<br><br>1. Importing the random module:-<br><br>import random<br><br>The random module is imported to generate a random number for the computer.<br><br>2. Generating a random number:-<br><br>computer = random.randint(1, 50)
<br><br>The randint function from the random module generates a random integer between 1 and 50 inclusive. This is the number the user will try to guess.<br><br>3. Initializing variables:-<br><br>user_input = -1
guess = 0<br><br>"user_input" is initialized to -1, ensuring it doesn't accidentally match the computer's number on the first iteration.<br>
"guess" is initialized to 0 to keep track of the number of attempts the user makes.<br><br>4. Guessing loop:-<br><br>The while loop runs as long as the user_input does not match the computer's number.<br>
Inside the loop, guess is incremented by 1 to count each attempt.<br>
The user is prompted to input their guess with input("Guess the number: "), which is then converted to an integer and stored in user_input.<br>
If the user's guess (user_input) is less than the computer's number, a message "Your guess is too low" is printed.<br>
If the user's guess is greater than the computer's number, a message "Your guess is too high" is printed.<br><br>
6. Ending the game:-<br><br>print(f"You guessed the number in {guess} tries")<br><br>Once the while loop ends (i.e., the user's guess matches the computer's number), a message is printed displaying the total number of guesses it took for the user to guess the number correctly.<br><br><br>Example Output:-<br><br>Guess the number: 25<br>
Your guess is too low<br>
Guess the number: 37<br>
Your guess is too high<br>
Guess the number: 30<br>
Your guess is too low<br>
Guess the number: 32<br>
You guessed the number in 4 tries<br><br>
In this interaction, the user guessed the number correctly in 4 tries.









