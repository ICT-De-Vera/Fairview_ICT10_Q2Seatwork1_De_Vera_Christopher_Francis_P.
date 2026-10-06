from pyscript import document, display
# dictionary of country nicknames
nicknames = {
    "philippines": "Pearl of the Orient Seas",
    "thailand": "Land of Smiles",
    "vietnam": "Land of the Ascending Dragon",
    "singapore": "The Lion City",
    "indonesia": "Emerald of the Equator",
    "malaysia": "Truly Asia",
    "myanmar": "The Golden Land",
    "burma": "The Golden Land",
    "laos": "Land of a Million Elephants",
    "cambodia": "Kingdom of Wonder",
    "brunei": "Abode of Peace",
    "timor leste": "The Rising Sun",
    "east timor": "The Rising Sun",
}

display("=== SOUTHEAST ASIA NICKNAME LOOKUP ===")
display("Type 'exit' when you want to stop.\n")

# main loop
while True:
    choice = input("Enter a country: ")

    # cleanup input
    clean_choice = choice.lower().strip()

    # stop loop if user types exit
    if clean_choice == "exit":
        display("Bye!")
        break

    # check if user typed nothing
    if clean_choice == "":
        display("Please type a country name.")
        continue

    # search in dictionary
    if clean_choice in nicknames:
        display(f"Result: {choice.title()} is known as '{nicknames[clean_choice]}'\n")
    else:
        display("Not found! Try another SEA country like Philippines or Thaila
