secret_word = "hydrogen"
guess_count = 0
guess_limit = 4

while guess_count < guess_limit:
    guess_input = str(input(f"Guess the Element right: "))
    guess_count += 1
    if guess_input.lower() == secret_word:
        print(f"You WON! Your guess is Right.")
        break
else:
    print(f"Sorry, you lost!")
