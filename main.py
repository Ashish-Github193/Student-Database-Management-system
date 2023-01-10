from sqlite3 import connect
import indian_names
from random import *
import os
import eel

eel.init("web")

database = connect(os.getcwd() + "\\database\\Database.DB")
cursor = database.cursor()

@eel.expose
def reset_database():
    try:
        cursor.execute("DROP TABLE STUDENTS_1_year")
        cursor.execute("DROP TABLE STUDENTS_2_year")
        cursor.execute("DROP TABLE STUDENTS_3_year")
        database.commit()
        return "Deleted all records"
    except:
        return "No existing table found."

@eel.expose
def add_data(data):
    year=data[0]
    first_name=data[1]
    last_name=data[2]
    roll_no=data[3]
    age=data[4]
    gender=data[5]
    dept=data[6]

    HEAD = "INSERT INTO "
    MIDDLE = "STUDENTS_" + str(year) + "_year "
    TAIL = f"(FIRST_NAME, LAST_NAME, ROLL_NO, AGE, GENDER, DEPT, YEAR) values ('{first_name}', '{last_name}', '{roll_no}', '{age}', '{gender}', '{dept}', '{year}');"

    command = HEAD + MIDDLE + TAIL
    print(command)
    cursor.execute(command)
    database.commit()

@eel.expose
def show_data(data):
    year=data[0]
    first_name=data[1]
    last_name=data[2]
    roll_no=data[3]
    age=data[4]
    gender=data[5]
    dept=data[6]

    command = "SELECT * FROM "
    index = 0
    if (not year == "--"):
        command += "STUDENTS_" + str(year) + "_year"
        
        if (not first_name == "--"):
            if index == 0:
                command += " Where("
                index += 1
                command += " FIRST_NAME == \"" + str(first_name) + "\""
            else:
                command += " FIRST_NAME == \"" + str(first_name) + "\""

        if (not last_name == "--"):
            if index == 0:
                command += " Where("
                index += 1
                command += " LAST_NAME == \"" + str(last_name) + "\""
            else:
                command += " and LAST_NAME == \"" + str(last_name) + "\""

        if (not roll_no == "--"):
            if index == 0:
                command += " Where("
                index += 1
                command += " ROLL_NO == \"" + str(roll_no) + "\""
            else:
                command += " and ROLL_NO == \"" + str(roll_no) + "\""


        if (not age == "--"):
            if index == 0:
                command += " Where("
                index += 1
                command += " AGE == \"" + str(age) + "\""
            else:
                command += " and AGE == \"" + str(age) + "\""


        if (not gender == "--"):
            if index == 0:
                command += " Where("
                index += 1
                command += " GENDER == \"" + str(gender) + "\""
            else:
                command += " and GENDER == \"" + str(gender) + "\""
            
        if (not dept == "--"):
            if index == 0:
                command += " Where("
                index += 1
                command += " DEPT == \"" + str(dept) + "\""
            else:
                command += " and DEPT == \"" + str(dept) + "\""

        command += ")"
        print (command)
        cursor.execute(command)

        data_packed = []
        for row in cursor:
            data_packed.append(row)
    
        return data_packed
    else:
        return "Year is important to show any record."


@eel.expose
def delete_data(data):
    year=data[0]
    first_name=data[1]
    last_name=data[2]
    roll_no=data[3]
    age=data[4]
    gender=data[5]
    dept=data[6]

    command = "DELETE FROM "
    index = 0
    if (not year == "--"):
        command += "STUDENTS_" + str(year) + "_year"
        
        if (not first_name == "--"):
            if index == 0:
                command += " Where("
                index += 1
                command += " FIRST_NAME == \"" + str(first_name) + "\""
            else:
                command += " FIRST_NAME == \"" + str(first_name) + "\""

        if (not last_name == "--"):
            if index == 0:
                command += " Where("
                index += 1
                command += " LAST_NAME == \"" + str(last_name) + "\""
            else:
                command += " and LAST_NAME == \"" + str(last_name) + "\""

        if (not roll_no == "--"):
            if index == 0:
                command += " Where("
                index += 1
                command += " ROLL_NO == \"" + str(roll_no) + "\""
            else:
                command += " and ROLL_NO == \"" + str(roll_no) + "\""


        if (not age == "--"):
            if index == 0:
                command += " Where("
                index += 1
                command += " AGE == \"" + str(age) + "\""
            else:
                command += " and AGE == \"" + str(age) + "\""


        if (not gender == "--"):
            if index == 0:
                command += " Where("
                index += 1
                command += " GENDER == \"" + str(gender) + "\""
            else:
                command += " and GENDER == \"" + str(gender) + "\""
            
        if (not dept == "--"):
            if index == 0:
                command += " Where("
                index += 1
                command += " DEPT == \"" + str(dept) + "\""
            else:
                command += " and DEPT == \"" + str(dept) + "\""

        command += ")"
        print (command)
        cursor.execute(command)
        database.commit()
    
        return str(cursor.rowcount) + " rows deleted from table " + "STUDENTS_" + str(year) + "_year"
    else:
        return "Year is important to Delete any record."


@eel.expose
def FillRandomData (length):
    try:
        cursor.execute ("DROP TABLE STUDENTS_1_year;")
        cursor.execute ("DROP TABLE STUDENTS_2_year;")
        cursor.execute ("DROP TABLE STUDENTS_3_year;")
    except:
        pass
    
    roll_num_s = 1000
    roll_index = 1
    roll_num = 1
    Dept_list = ["BCA", "CE", "ECE"]
    genders = ["Male", "Female"]
    gender_index = 0
    Age_lim = [17, 25]
    years = [1, 2, 3]
    
    cursor.execute (f"""CREATE TABLE STUDENTS_1_year (FIRST_NAME CHAR(25) NOT NULL, LAST_NAME CHAR(25) NOT NULL, ROLL_NO INT NOT NULL, AGE INT NOT NULL, GENDER CHAR(6) NOT NULL, DEPT CHAR(20) NOT NULL, YEAR INT NOT NULL);""")
    cursor.execute (f"""CREATE TABLE STUDENTS_2_year (FIRST_NAME CHAR(25) NOT NULL, LAST_NAME CHAR(25) NOT NULL, ROLL_NO INT NOT NULL, AGE INT NOT NULL, GENDER CHAR(6) NOT NULL, DEPT CHAR(20) NOT NULL, YEAR INT NOT NULL);""")
    cursor.execute (f"""CREATE TABLE STUDENTS_3_year (FIRST_NAME CHAR(25) NOT NULL, LAST_NAME CHAR(25) NOT NULL, ROLL_NO INT NOT NULL, AGE INT NOT NULL, GENDER CHAR(6) NOT NULL, DEPT CHAR(20) NOT NULL, YEAR INT NOT NULL);""")
    database.commit()
    for year in years:
        roll_num_s = randint(1000, 9999)
        roll_num_s *= 1000
        for index, dept in enumerate(Dept_list):
            roll_index = ((index+1)*10)+1
            for i in range(length):
                roll_num = roll_num_s + roll_index
                roll_index += 1
                if year == 1:
                    cursor.execute(f"""INSERT INTO STUDENTS_1_year (FIRST_NAME, LAST_NAME, ROLL_NO, AGE, GENDER, DEPT, YEAR) 
                    VALUES ('{indian_names.get_first_name(gender=genders[gender_index].lower())}',
                        '{indian_names.get_last_name()}',
                        '{roll_num}',
                        '{randint(Age_lim[0], Age_lim[1])}',
                        '{genders[gender_index]}',
                        '{dept}',
                        '{year}');""")
                elif year == 2:
                    cursor.execute(f"""INSERT INTO STUDENTS_2_year (FIRST_NAME, LAST_NAME, ROLL_NO, AGE, GENDER, DEPT, YEAR) 
                    VALUES ('{indian_names.get_first_name(gender=genders[gender_index].lower())}',
                        '{indian_names.get_last_name()}',
                        '{roll_num}',
                        '{randint(Age_lim[0], Age_lim[1])}',
                        '{genders[gender_index]}',
                        '{dept}',
                        '{year}');""")
                elif year == 3:
                    cursor.execute(f"""INSERT INTO STUDENTS_3_year (FIRST_NAME, LAST_NAME, ROLL_NO, AGE, GENDER, DEPT, YEAR) 
                    VALUES ('{indian_names.get_first_name(gender=genders[gender_index].lower())}',
                        '{indian_names.get_last_name()}',
                        '{roll_num}',
                        '{randint(Age_lim[0], Age_lim[1])}',
                        '{genders[gender_index]}',
                        '{dept}',
                        '{year}');""")

                if gender_index:
                    gender_index = 0
                else:
                    gender_index = 1
    database.commit()
    return "Generated and Saved New Data"

eel.start("index.html", mode="default")