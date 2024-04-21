# Python app for Applied Databases module - ATU Galway
# By Joanne Feeney


# Imports
import pymysql

import ("C:\Users\appDB\Documents\applied_db_app\appDBproj_MySql.sql") as db1
import ("C:\Users\appDB\Documents\applied_db_app\appDBCity_Neo4j.sql") as db2

def main():
    name = input("Enter subject: ")
    teacher = input("Enter teacher: ")
    lc = input("Enter on Leaving Cert 1/0: ")

    try:
        num2DB.add_subject(name, teacher, lc)
    except pymysql.err.ProgrammingError as e:
        print("Programming Error:", e)
    except pymysql.err.IntegrityError as e:
        print("Subject", name, "already exists")
    except Exception as e:
        print("ERROR", e)


if __name__ == "__main__":
    main()


