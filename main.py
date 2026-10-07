from pyscript import document, display

# Function to look up a country's nickname
def lookup_country():
    country = document.getElementById("country-input").value.strip().lower()

    if country == "philippines":
        display("Pearl of the Orient Seas")
    elif country == "thailand":
        display("Land of Smiles")
    elif country == "vietnam":
        display("Land of the Ascending Dragon")
    elif country == "singapore":
        display("The Lion City")
    elif country == "indonesia":
        display("Emerald of the Equator")
    elif country == "malaysia":
        display("Truly Asia")
    elif country == "myanmar":
        display("The Golden Land")
    elif country == "burma":
        display("The Golden Land")
    elif country == "laos":
        display("Land of a Million Elephants")
    elif country == "cambodia":
        display("Kingdom of Wonder")
    elif country == "brunei":
        display("Abode of Peace")
    elif country == "timor leste" or country == "east timor":
        display("The Rising Sun")
    else:
        display("Country not found.")


