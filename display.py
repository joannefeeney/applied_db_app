import applied_db

def main():
    display_menu()

    while True:
        choice = input("Enter choice: ")
        if (choice == "1"):
            country = input("Country: ")
            population = input("Population: ")
            twinned_city = input("Twinned_city: ")
            applied_db.add_city(country, population, twinned_city)
            display_menu()
        else:
            break;


def display_menu():
    print("")
    print("MENU")
    print("====")
    print("1 - Add country")
    print("2 - Find country")
    print("x- Exit")

if __name__ == "__main__":
    main()