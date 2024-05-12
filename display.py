# Python app for Applied Databases module - ATU Galway
# By Joanne Feeney

# Imports
import applied_db as applied_db

# Defining integer conditions
def get_numerical(message:str,error:str="Invalid input. Please enter a number")->int:
    while True: # Loop until numerical input entered
        user_input = input(message)
        if user_input.isdigit():
            user_input = int(user_input)
            break
        else:
            print(error)
    return user_input

# Defining input conditions
def get_input_value(message:str,
                    numerical:bool=False,
                    select_from:list=[],
                    error:str="Invalid input. Please enter a number")->str:
    while True: # Loop until get a valid value
        user_input = input(message).strip()
        temp_user_input = user_input
        if '.' in user_input:
            temp_user_input = user_input.replace('.', '')

        if numerical:
            if temp_user_input.isdigit():
                break
            else:
                print(error)
        else:
            user_input = user_input.strip().lower()
            if select_from == [] and user_input != '':
                break
            elif user_input in select_from:
                break
            elif user_input == '':
                continue
            else:
                print(error)

    return user_input

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

# Main function
def main():
    display_menu()

    while True:
        choice = input("Enter choice: ")
        if (choice == "1"):
            ### View cities by country
            country_code = input("Country Code: ")
            applied_db.view_city_by_country(country_code)
            if len(applied_db.result_city_list) == 0:
                if len(applied_db.result_country_list[0]) == 0:
                    print("No countries found for: " + country_code)
                else:
                    print("No cities found for country: " + country_code)
            else:
                print(applied_db.result_city_list[0][2])
                display_menu()

        elif (choice == "2"):
            ### Update city population 
            city_id = get_input_value(message="Enter a city ID: ",numerical = True)
            applied_db.get_city(city_id=city_id)

            feedback,old_population,_ = applied_db.get_city(city_id=city_id)
            if feedback == '':
                print("No city found with ID = {city_id}")
            else:
                print(feedback)
                old_population = int(old_population)

                user_input = get_input_value(message="[I]ncrease/[D]ecrease Population: ",numerical = False,select_from = ['i','d'],error = "Invalid input. Please enter I or D")
                user_input = user_input.upper()

                amount = get_input_value(message="Enter Population {['Increase','Decrease'][['I','D'].index(user_input)]}: ",numerical = True,error="Invalid input. Please enter the amount")
                amount = int(amount)
                if user_input == 'I':
                    new_population = old_population + amount
                else:
                    new_population = old_population - amount

                print("Old Population: {old_population} \n New Population: {new_population}")
                applied_db.update_city_pop(city_id=city_id,new_population=new_population)
                display_menu()

        elif (choice == "3"):
            ### Add new person
            print("Enter person details: ")
            personID = get_input_value(message='ID: ',numerical = True,error = "Invalid input. Please enter a number")
            personname = get_input_value(message='Name: ',numerical = False,error = "Invalid input")
            age = get_input_value(message='Age: ',numerical = True,error = "Invalid input. Please enter a number")
            salary = get_input_value(message='Salary: ',numerical = True,error = "Invalid input. Please enter a number")
            city = get_input_value(message='City: ',numerical = True,error = "Invalid input. Please enter a number")

            # Person_details
            applied_db.add_person(personID=personID,
                                   personname=personname,
                                   age=age,
                                   salary=salary,
                                   city=city)
            display_menu()

        elif (choice == "4"):
            ### Delete person
            person_id = get_input_value(message="Enter person ID to be deleted: ",
                numerical = True,error = "Invalid input. Please enter person ID"
            )
            applied_db.delete_person(personID=person_id)

            print(person_id)
            display_menu()

        elif (choice == "5"):
            ### View countries by population
            operation = get_input_value(message="Enter either < or > or = ",numerical = False,
                select_from = ['>','<','='],error = "Invalid input, please choose one operation < or > or ="
            )
            population = get_input_value(message="Enter Population: ",numerical = True,
                error = "Invalid input, please enter a number"
            )

            print(applied_db.view_country_by_pop(population))
            display_menu()

        elif (choice == "6"):
            ### Show twinned cities
            twinned_cities = applied_db.show_twin_cities('Name')
            if twinned_cities == []:
                print("No twinned cities found")
            else:
                print("Twinned Cities")
                print("--------------")
                for city in twinned_cities:
                    print("{city[0]} <-> {city[1]}")
                    display_menu()
                    
        elif (choice == "7"):
            ### Twin with Dublin
            city_id = get_input_value(message="Enter ID of City to twin with Dublin: " ,numerical = True)

            feedback,_,city_details = applied_db.get_city(city_id=city_id)
            
            # Check if city exists in MySQL
            if feedback == '':
                print("Error. City ID does not exist in MySQL database")
            elif city_details["Name"] == "Dublin":
                print("Dublin can not be twinned with itself")
            else:
                neo4j_cities= applied_db.get_neo4j_cities()
                # Check if dublin exists in Neo4j
                dublin_id = applied_db.get_city_id(city_name="Dublin")
                if dublin_id not in neo4j_cities:
                    print("Error. Dublin does not exist in Neo4J database")
                else:
                    # Check if city is in Neo4j
                    if str(city_id) in neo4j_cities or int(city_id) in neo4j_cities:
                        # Check if city is already twinned with Dublin
                        already_twinned = applied_db.neo4j_twinned_with(city_name="Dublin")
                        if city_id in already_twinned:
                            print("City ID is already twinned with Dublin")
                        else:
                            # Twin the city
                            if applied_db.twin_with_dub(city_id=city_id):
                                print("Dublin is now twinned with selected city")
                                display_menu()

        elif (choice == "x"):
            print("Exiting application")
            return True
        
        else:
            print("Invalid choice. Please try again")
            break

if __name__ == "__main__":
    main()