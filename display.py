# Python app for Applied Databases module - ATU Galway
# By Joanne Feeney

# Imports
import applied_db

# Main function
def main():
    display_menu()

    while True:
        choice = input("Enter choice: ")
        if (choice == "1"):
            ### View Cities by country
            '''country = input("Country: ")
            population = input("Population: ")
            twinned_city = input("Twinned_city: ")
            applied_db.add_city(country, population, twinned_city)
            display_menu()'''
        elif (choice == "2"):
            ### Update city population 
        elif (choice == "3"):
            ### Add new person
        elif (choice == "4"):
            ### Delete person
        elif (choice == "5"):
            ### view countries by population
        elif (choice == "6"):
            ### Show twinned cities
        elif (choice == "7"):
            ### Twin with Dublin
        elif (choice == "x"):
            print("Exiting application")
            return True
        else:
            print("Invalid choice. Please try again.")
            break


# Display menu
def display_menu():
    print("")
    print("==================================")
    print("                MENU              ")
    print("==================================")
    print("")
    print("1 - View Cities by Country")
    print("2 - Update City Population")
    print("3 - Add New Person")
    print("4 - Delete Person")
    print("5 - View Countries by Population")
    print("6 - Show twinned cities")
    print("7 - Twin with Dublin")
    print("x - Exit application")

if __name__ == "__main__":
    main()