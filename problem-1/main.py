#!/usr/bin/env python3

import sqlite3
import random

DBNAME = "sqlite.db"

def main():
    update_table()

def create_table():
    conn = sqlite3.connect(DBNAME)
    cursor = conn.execute("""
        CREATE TABLE EMPLOYEE
            (ID INT PRIMARY KEY     NOT NULL,
            FIRST_NAME              TEXT,
            LAST_NAME               TEXT,
            POSITION                TEXT,
            JOB_GRADE               INT);
    """)
    
    id = 0
    for i in range(0, 1000):
        first_name = random.choice([
            'emma',
            'olivia',
            'ava',
            'isabella',
            'sophia',
            'charlotte',
            'mia',
            'amelia',
            'harper',
            'evelyn',
            'abigail',
            'emily',
            'elizabeth',
            'mila',
            'ella',
            'avery',
            'sofia',
            'camila',
            'aria',
            'scarlett',
            'victoria',
            'madison',
            'luna',
            'grace',
            'chloe',
            'penelope',
            'layla',
            'riley',
            'zoey',
            'nora',
            'lily',
            'eleanor',
            'hannah',
            'lillian',
            'addison',
            'aubrey',
            'ellie',
            'stella',
            'natalie',
            'zoe',
            'leah',
            'hazel',
            'violet',
            'aurora',
            'savannah',
            'audrey',
            'brooklyn',
            'bella',
            'claire',
            'skylar',
            'liam',
            'noah',
            'william',
            'james',
            'oliver',
            'benjamin',
            'elijah',
            'lucas',
            'mason',
            'logan',
            'alexander',
            'ethan',
            'jacob',
            'michael',
            'daniel',
            'henry',
            'jackson',
            'sebastian',
            'aiden',
            'matthew',
            'samuel',
            'david',
            'joseph',
            'carter',
            'owen',
            'wyatt',
            'john',
            'jack',
            'luke',
            'jayden',
            'dylan',
            'grayson',
            'levi',
            'isaac',
            'gabriel',
            'julian',
            'mateo',
            'anthony',
            'jaxon',
            'lincoln',
            'joshua',
            'christopher',
            'andrew',
            'theodore',
            'caleb',
            'ryan',
            'asher',
            'nathan',
            'thomas',
            'leo'
        ])

        last_name = random.choice([
            'smith',
            'johnson',
            'williams',
            'jones',
            'brown',
            'davis',
            'miller',
            'wilson',
            'moore',
            'taylor',
            'anderson',
            'thomas',
            'jackson',
            'white',
            'harris',
            'martin',
            'thompson',
            'garcia',
            'martinez',
            'robinson',
            'clark',
            'rodriguez',
            'lewis',
            'lee',
            'walker',
            'hall',
            'allen',
            'young',
            'hernandez',
            'king',
            'wright',
            'lopez',
            'hill',
            'scott',
            'green',
            'adams',
            'baker',
            'gonzalez',
            'nelson',
            'carter',
            'mitchell',
            'perez',
            'roberts',
            'turner',
            'phillips',
            'campbell',
            'parker',
            'evans',
            'edwards',
            'collins',
            'stewart',
            'sanchez',
            'morris',
            'rogers',
            'reed',
            'cook',
            'morgan',
            'bell',
            'murphy',
            'bailey',
            'rivera',
            'cooper',
            'richardson',
            'cox',
            'howard',
            'ward',
            'torres',
            'peterson',
            'gray',
            'ramirez',
            'james',
            'watson',
            'brooks',
            'kelly',
            'sanders',
            'price',
            'bennett',
            'wood',
            'barnes',
            'ross',
            'henderson',
            'coleman',
            'jenkins',
            'perry',
            'powell',
            'long',
            'patterson',
            'hughes',
            'flores',
            'washington',
            'butler',
            'simmons',
            'foster',
            'gonzales',
            'bryant',
            'alexander',
            'russell',
            'griffin',
            'diaz',
            'hayes'
        ])

        position = random.choice([
            'Assistant',
            'Associate Scientist',
            'Developer',
            'Senior Developer',
            'Architect',
            'Manager',
            'Directory',
            'Scientist',
            'Principal Investigator',
            'Lawyer',
            'Accountant',
            'Seasonal'
        ])

        job_grade = random.randint(1, 15)

        id += 1
        conn.execute(f"INSERT INTO EMPLOYEE (ID,FIRST_NAME,LAST_NAME,POSITION,JOB_GRADE) \
            VALUES ({id}, '{first_name}', '{last_name}', '{position}', {job_grade} )")

    conn.commit()
    conn.close()

def query_table():
    conn = sqlite3.connect(DBNAME)
    cursor = conn.execute("select * from EMPLOYEE")
    
    for row in cursor:
        print(row)

    conn.close()

def update_table():
    print("Updating table")

    conn = sqlite3.connect(DBNAME)
    cursor = conn.execute("select ID, FIRST_NAME, LAST_NAME from EMPLOYEE")
    
    for row in cursor:
        updated_firstname = row[1].capitalize()
        updated_lastname = row[2].capitalize()
        conn.execute("UPDATE EMPLOYEE set FIRST_NAME = :firstname, LAST_NAME = :lastname where ID = :id", dict(firstname=updated_firstname, lastname=updated_lastname, id=row[0]))

    print("Committing changes")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
    print("Done")