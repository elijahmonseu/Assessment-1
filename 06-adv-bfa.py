correct_password = "AdvBFATest2"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    entered = input("Enter the password: ")
    if entered == correct_password:
        print("Access granted.")
        break
    attempts += 1
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"Wrong password. {remaining} attempts remaining.")
    else:
        print("Maximum attempts reached. Authorities have been alerted.")