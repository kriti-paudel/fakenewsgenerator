import random
subjects = [
    "Sandeep Lamichhane",
    "Rohit Paudel",
    "A Group of Monleys",
    "Prime Minister KP OLI",
    "Bus Driver From Pokhara",
]

actions = [
    "Player",
    "cancels",
    "dances with",
    "eats",
    "declares war on"

]

places_or_things=[
    "at pokhara",
    "during NPL match",
    "inside parliament",
    "at 17 bens",
    "a plate of samosa"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip()
    if user_input == "no":
        break

print("\nThanks for using the Fake News Headline Generator. Have a fun day")

