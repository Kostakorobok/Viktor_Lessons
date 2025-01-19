logo = """
▗▖ ▗▖▗▄▄▄▖▗▖    ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖    ▗▄▄▄▖▗▄▖      ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖ ▗▄▄▖
▐▌ ▐▌▐▌   ▐▌   ▐▌   ▐▌ ▐▌▐▛▚▞▜▌▐▌         █ ▐▌ ▐▌    ▐▌     █    █    █  ▐▌   ▐▌   
▐▌ ▐▌▐▛▀▀▘▐▌   ▐▌   ▐▌ ▐▌▐▌  ▐▌▐▛▀▀▘      █ ▐▌ ▐▌    ▐▌     █    █    █  ▐▛▀▀▘ ▝▀▚▖
▐▙█▟▌▐▙▄▄▖▐▙▄▄▖▝▚▄▄▖▝▚▄▞▘▐▌  ▐▌▐▙▄▄▖      █ ▝▚▄▞▘    ▝▚▄▄▖▗▄█▄▖  █  ▗▄█▄▖▐▙▄▄▖▗▄▄▞▘
                                                                                                                                                                   
"""

print(logo)

app_on = True

available_memory = 0
cities = {}

print(f"This application will store information about some cities")

while(app_on):
    counter = 0
    user_choice = str(input("(1) View the Database\n(2) Enter new database\n(3) Exit\n"))
    if user_choice == "1":
        print(cities)
    elif user_choice == "2":
        cities = {}
        available_memory = int(input(f"Enter the number of cities you want to enter into database:\n"))
        while(available_memory > 0):
            city_temp = input(f"Enter the name of city number {counter + 1}:\n")
            country_temp = input(f"What country {city_temp} is in?\n")
            population_temp = input(f"Enter the population of the {city_temp}:\n")
            fact_temp = input(f"Enter an interesting fact about {city_temp}:\n")

            cities[city_temp] = country_temp, population_temp, fact_temp
            available_memory -= 1
            counter += 1
        else:
            print("Memory full.\n")
    elif user_choice == "3":
        app_on = False
        print("Thank you for using the app. Good bye.")
    else:
        print("Wrong input, try again.")
        



    
