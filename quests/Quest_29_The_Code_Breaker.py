secret_code = 42
max_attempts = 3
attempt = 0

while attempt < max_attempts:
    attempt = attempt + 1
    guess = int(input(f"Attempt {attempt}/{max_attempts} — Enter the secret code: "))

    if guess == secret_code:
        print(f"Correct! You cracked the code in {attempt} attempt(s). You may pass!")
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"Wrong! You have {remaining} attempt(s) remaining.")
        else:
            print(f"Wrong! You have failed. The secret code was {secret_code}.")

