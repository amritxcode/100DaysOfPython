import requests

def get_weather(city):
    try:
        url =f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)

        if response.status_code != 200:
            return "N/A"
        
        data = response.json()
        return data["current_condition"][0]["temp_C"]
    except:
        return "N/A"

def get_age(name):
    try:
        url = f"https://api.agify.io/?name={name}"
        response = requests.get(url)
        
        if response.status_code != 200:
            return "N/A"
        
        data = response.json()
        return data["age"]
    except:
        return "N/A"

def get_gender(name):
    try:
        url = f"https://api.genderize.io/?name={name}"
        response = requests.get(url)

        if response.status_code != 200:
            return "N/A"
        
        data = response.json()
        return data["gender"]
    except:
        return "N/A"

def get_country(name):
    try:
        url = f"https://api.nationalize.io/?name={name}"
        response = requests.get(url)

        if response.status_code != 200:
            return "N/A"
        
        data = response.json()

        if data["country"]:
            return data["country"][0]["country_id"]
        else:
            return "N/A"
    except:
        return "N/A"
    


def show_result(name):
    age = get_age(name)
    gender = get_gender(name)
    country = get_country(name)

    print("\nResult")
    print("------------------")
    print(f"Name: {name.capitalize()}")
    print(f"Age: {age}")

    if gender != "N/A":
        print(f"Gender: {gender.capitalize()}")
    else:
        print("Gender: N/A")

    if country != "N/A":
        print(f"Country: {country.upper()}")
    else:
        print("Country: N/A")

#main_code
while True:
    print("\n--- Multi API CLI Tool ---")
    print("1. Analyze Name")
    print("2. Check Weather")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")

        if name.strip() == "":
            print("Invalid name!")
            continue

        show_result(name)

    elif choice == "2":
        city = input("Enter city: ")
        if city.strip() == "":
            print("Invalid city!")
            continue
        temp = get_weather(city)

        print("\nResult")
        print("------------------")
        print(f"City: {city.capitalize()}")
        print(f"Temperature: {temp}°C")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")