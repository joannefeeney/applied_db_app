# Python app for Applied Databases module - ATU Galway
# By Joanne Feeney


# Imports
import pymysql
import pymysql.cursors

import appDBproj_MySql
import appDBCity_Neo4j

# def add_person(person):
    

def add_city(country, population, twinned_city):
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBCity_Neo4j", cursorclass=pymysql.cursors.DictCursor)

    sql = "INSERT INTO person_table VALUES (%s, %s, %s)"

    with db:
        try:
            cursor = db.cursor()
            cursor.execute(sql, (country, population, twinned_city))
            db.commit()
        except pymysql.err.IntegrityError as e:
            print(e)
        except pymysql.err.InternalError as e:
            print (e)
        except Exception as e:
            print(e)

def find_city(country):
    db = pymysql.connect(host="localhost", user="root", password="root", db="appDBCity_Neo4j", cursorclass=pymysql.cursors.DictCursor)

    sql = '''
            select ct.country, ct.population, ct.twinned_city
            from city_table ct
            inner join country_table cot
                on ct.country = cot.country
            where surname like %s
          '''
    with db:
        cursor = db.cursor()
        cursor.execute(sql, ("%"+country+"%"))
        return cursor.fetchall()




