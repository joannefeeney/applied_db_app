# Python app for Applied Databases module - ATU Galway
# By Joanne Feeney


# Imports
import pymysql
import pymysql.cursors

# 3 Add person function
def add_person(personID, personname, age, salary, city):
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj_MySql", cursorclass=pymysql.cursors.DictCursor)

    sql = "INSERT INTO person_table VALUES (%s, %s, %s, %s, %s)"
    
    with db:
        try:
            cursor = db.cursor()
            cursor.execute(sql, (personID, personname, age, salary, city))
            db.commit()
        except pymysql.err.IntegrityError as a:
            print(a)
        except pymysql.err.InternalError as a:
            print (a)
        except Exception as e:
            print(a)

# 1 View cities by country function
def view_city_by_country(ID, Name, CountryCode, District, Population, latitude, longitude):
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj_MySql", cursorclass=pymysql.cursors.DictCursor)

    sql = """
    SELECT ID, Name, CountryCode, District, Population, latitude, longitude
    FROM city_table
    WHERE CountryCode = %s
    """

    with db:
        cursor = db.cursor()
        cursor.execute(sql, (ID, Name, CountryCode, District, Population, latitude, longitude))
        return cursor.fetchall()
        cursor.close()
        return results


'''sql =
            select ct.country, ct.population, ct.twinned_city
            from city_table ct
            inner join country_table cot
                on ct.country = cot.country
            where name like %s

    with db:
        cursor = db.cursor()
        cursor.execute(sql, ("%"+country+"%"))
        return cursor.fetchall()'''


'''# 2 Update city population function
def update_city_pop(population):
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj_MySql", cursorclass=pymysql.cursors.DictCursor)

    sql = ...

# 4 Delete person function
def delete_person(personID, personname, age, salary, city):
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj_MySql", cursorclass=pymysql.cursors.DictCursor)

    sql = "DELETE person from person_table VALUES (%s, %s, %s, %s, %s)"

    ...

# 5 View countries by population function
def view_country_by_pop(ID, Name, CountryCode, District, Population, latitude, longitude):
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj_MySql", cursorclass=pymysql.cursors.DictCursor)

    sql = ...

# 6 Show twinned cities function
def show_twin_cities(ID, Name, CountryCode, District, Population, latitude, longitude):
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj_MySql", cursorclass=pymysql.cursors.DictCursor)

    sql = 

# 7 Twin with Dublin function
def twin_with_dub(ID, Name, CountryCode, District, Population, latitude, longitude):
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBproj_MySql", cursorclass=pymysql.cursors.DictCursor)

    sql = '''
