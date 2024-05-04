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
            countrycode = input("Country Code: ")
            applied_db.view_city_by_country(id, Name, CountryCode, District, Population, latitude, longitude)
            print("Cities by Country: ")
            display_menu()
        if (choice == "2"):
            ### Update city population 
            print("TBD: ")
        if (choice == "3"):
            ### Add new person
            personID = input("ID: ")
            personname = input("Name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            city = input("City: ")
            applied_db.add_person(personID, personname, age, salary, city)
            print("Person added")
            display_menu()
        if (choice == "4"):
            ### Delete person
            print("TBD: ")
        if (choice == "5"):
            ### view countries by population
            print("TBD: ")
        if (choice == "6"):
            ### Show twinned cities
            print("TBD: ")
        if (choice == "7"):
            ### Twin with Dublin
            print("TBD: ")
        if (choice == "x"):
            print("Exiting application")
            return True
        else:
            print("Invalid choice. Please try again")
            break
            '''country = input("Country: ")
            population = input("Population: ")
            twinned_city = input("Twinned_city: ")
            applied_db.add_city(country, population, twinned_city)
            display_menu()'''

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