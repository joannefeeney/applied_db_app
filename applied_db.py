# Python app for Applied Databases module - ATU Galway
# By Joanne Feeney


# Imports
import pymysql
import pymysql.cursors


# 1 View cities by country function
def view_city_by_country(country_name:str)->None:
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj", cursorclass=pymysql.cursors.DictCursor)

    sql_query = "SELECT * FROM {country_table} WHERE Name LIKE '%{name}%'"

    with db:
        cursor = db.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        if len(results) == 0:
                return None

    # Using the country code to get the cities data from the city table
    sql_query = "SELECT * FROM {city_table} WHERE CountryCode LIKE '{countrycode}'"
    
    with db:
        cursor = db.cursor()
        results = cursor.fetchall()
        if len(results) == 0:
                return None
        try:    
            cursor.execute(sql_query)
        except pymysql.err.InterfaceError as e:
            print("Error: {e}")

def get_city(city_id:str)-> list:
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj", cursorclass=pymysql.cursors.DictCursor)

    # SQL query 
    sql_query = "SELECT * FROM {city_table} WHERE ID = {city_id}"

    with db:
        cursor = db.cursor()
        cursor.execute(sql_query)
        # Get the city details
        try:
            city_details = cursor.fetchone()
        # Print(city_details['Name'])
            if city_details is None:
                return ['','','']
            else:
                old_population = city_details["Population"]
                lines = ['','']
                for key in city_details.keys():
                    return  ["DISPLAY TABLE TO BE CREATED JF"]
            
        except pymysql.err.OperationalError as Er:
            print('Error: {Er}')
        
        except Exception as Er:
            print("Error in get_city : {Er} ")

def get_city_id(city_name:str)-> str:
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj", cursorclass=pymysql.cursors.DictCursor)

    # SQL query to retrieve city details
    sql_query = "SELECT * FROM {city_table} WHERE Name = '{city_name}'"

    with db:
        cursor = db.cursor()
        cursor.execute(sql_query)

        try:
        # Get the city details
            city_details = cursor.fetchone()
            if city_details is None:
                return ''
            else:
            # Return the city id
                return city_details['ID']
        
        except Exception as Er:
            print("Error in get_city id : {Er} ")

# 2 Update city population function
def update_city_pop(city_id:str,new_population:int)->None:
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj", cursorclass=pymysql.cursors.DictCursor)

    sql_query = "SELECT * FROM {city_table} WHERE ID = {city_id}"

    with db:
        cursor = db.cursor()
        cursor.execute(sql_query)

        try:
            # Update city population
            update_sql_query = "UPDATE {city_table} SET Population = {new_population} WHERE ID = {city_id}"
            cursor.execute(update_sql_query)
            # Retrieve city details after update
            cursor.execute(sql_query)
            city_details = cursor.fetchone()

            print(create_display_table(lines=lines))
            pymysql.commit()

        except Exception as Er:
            print("Error into get_city : {Er} ")

# 3 Add person function
def add_person(personID:str, personname:str, age:str, salary:str, city:str) -> None:
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj", cursorclass=pymysql.cursors.DictCursor)
    
    with db:
        cursor = db.cursor()
        cursor.execute(sql_query)
        try:
            ready_to_insert = True
            # Check if the person exists
            sql_query = "SELECT * FROM {person_table} WHERE personID LIKE '{personID}'"
            cursor.execute(sql_query)
            results = cursor.fetchall()
            if len(results) != 0:
                print("Error: Person ID {personID} already exists")
                ready_to_insert = False
            # Check if the city exists
            sql_query = "SELECT * FROM {self.table_city} WHERE ID LIKE '{city}'"
            cursor.execute(sql_query)
            results = cursor.fetchall()
            if len(results) == 0:
                print("Error: City ID {city} does not exist")
                ready_to_insert = False

            # SQL query to insert new person
            if ready_to_insert:
                sql_query = "ALTER TABLE {person_table} DISABLE KEYS"
                # Execute(sql_query)
                sql_query = '''
                    INSERT INTO {person_table} (personID,personname,age,salary,city) VALUES ({personID}, 
                '{personname}', {age}, {salary}, {city})'''
                cursor.execute(sql_query)
                sql_query = "ALTER TABLE {person_table} ENABLE KEYS"
                # Execute(sql_query)
                pymysql.commit()
        except Exception as Er:
            print(Er)

    def show_person(person) -> str:
        try:
            sql_query = "SELECT * FROM {person_table}"
            cursor = self.connection.cursor()
            cursor.execute(sql_query)
            results = cursor.fetchall()
            lines = []
            if len(results) == 0:
                return ''
        except Exception as Er:
            print("Error: {Er}")
            return ''

# 4 Delete person function
def delete_person(personID:str):
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj", cursorclass=pymysql.cursors.DictCursor)

    with db:
        cursor = db.cursor()
        # SQL query to delete person
    try:
        sql_query = "SELECT * FROM {person_table} WHERE personID = '{personID}'"
        cursor.execute(sql_query)
            # Get the city details
        person_details = cursor.fetchone()
        if person_details is None:
            print("Person ID not found")
        else:
            sql_query = "DELETE FROM {person_table} WHERE personID = {personID}"
            cursor.execute(sql_query)
            pymysql.commit()
            print("Person ID: {personID} deleted")

    except pymysql.err.ProgrammingError as Er:
        print("Error: {Er}")
    except pymysql.err.OperationalError as Er:
        print("Error: {Er}")
    except pymysql.err.IntegrityError as Er:
        print("Error: Can't delete Person ID: {personID}")
    except Exception as Er:
        print(Er)

# 5 View countries by population function
def view_country_by_pop(population:str):
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj", cursorclass=pymysql.cursors.DictCursor)

    with db:
        cursor = db.cursor()

    # Get country code by country name from the table
    try:
        population = int(population)
        sql_query = "SELECT * FROM {table_country} WHERE Population {population}"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        if len(results) == 0:
            return ''
        else:
            return create_display_table(lines=lines)
    except Exception as Er:
        print("Error in (view_country_by_pop func): {Er}")
        return ''

# 6 Show twinned cities function
def show_twin_cities(Name) -> list:
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj", cursorclass=pymysql.cursors.DictCursor)

    with db:
        cursor = db.cursor()

    try:
            if twinned_cities == []:
                    result = ("MATCH (a)-[r:TWINNED_WITH]->(b) RETURN a, r, b")

                    # Print the results
                    for record in result:
                        return twinned_cities
    except Exception as Er:
        print("Error in (show_twin_cities): {Er}")

# 7 Twin with Dublin function
def twin_with_dub(city_name:str="Dublin") -> list:
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj", cursorclass=pymysql.cursors.DictCursor)

    with db:
        cursor = db.cursor()
        try:
            twinned_with_city = []
            with ("MATCH (d:City), (c:City) WHERE d.name = $name AND EXISTS((d)-[:TWINNED_WITH]->(c)) RETURN c.name AS name, c.cid AS id"):
                # Print the result
                for record in twinned_with_city:
                    twinned_with_city.append(record['id'])
            
            return twinned_with_city
        except Exception as Er:
            print("Error in (neo4j_twinned_with func): {Er}")

def twin_with_dub(city_id:str):
        try:
            dublin_id = get_city_id(city_name='Dublin')
            # Create a session
            with self.neo4j_connection.session() as session:
                run("MATCH (c1:City {cid: $cid1}), (c2:City {cid: $cid2}) CREATE (c1)-[:TWINNED_WITH]->(c2)", cid1=cid1, cid2=cid2)
                
                return True
        except Exception as Er:
            print("Error in (twin_with_dub func): {Er}")
            return False