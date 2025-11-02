quiz = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Finland": "Helsinki"
}

for country, capital in quiz.items():
    answer = input(f"What is the capital of {country}? ")
    if answer.strip().lower() == capital.lower():
        print("Correct!")
    else:
        print(f"Wrong!")
