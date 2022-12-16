import sys
import sqlite3  

def print_menu():  
    print ('\nPlease select from the following items:')  
    print('1. Add new contact')  
    print('2. Display contacts')  
    print('3. Edit contacts')  
    print('4. Delete contacts')
    print('5. Find contacts')
    print('0. Exit the program')

def addcontact():
    while True:  
        name = input("What is the person's first name?: ") 
        if len(name) != 0:  
            break  
        else:  
            print("Please enter the contact's name")     
    while True:  
        surname = input("What is the person's surname name?: ")  
        if len(surname) != 0:  
            break  
        else:  
            print("Please enter the surname")    
    while True:  
        num = input("What is the person's phone number? (only digits allowed): ")  
        if not num.isdigit():  
            print("Please enter only digits")  
            continue  
        elif len(num) != 10:  
            print("Please enter 10-digits phone number with no comma, no spaces, no punctuation")  
            continue  
        else:  
            break  
    cursor.execute('''INSERT INTO phonebook (name, surname, phone_number) VALUES (?,?,?)''',
                                                                         (name, surname, num))  
    conn.commit()      
    print("New contact " + surname + ' ' + name + " was added to the phonebook table")

def displaybook():
    cursor.execute("SELECT surname, name, phone_number FROM phonebook ORDER BY surname")
    results = cursor.fetchall()
    print(results)

def key_pair_reception(str):
    print ("\nPlease select the key field for " + str + " (from 1 to 3)")  
    print('1. Name')  
    print('2. Surname')  
    print('3. Phone_number')  
    print('0. Return to the Main menu')
    n = int(input('Your choice: '))
    if n == 1:  
        field = "name"
    elif n == 2:  
        field = "surname"
    elif n == 3:  
        field = "phone_number"
    else:
        return None
    keyword = input("\nPlease enter the key value: " + field + " = ")
    keypair = field + "='" + keyword + "'"
    return keypair

def editcontacts():
    s = key_pair_reception('searching')
    u = key_pair_reception('updating')
    if s != None:
        sql = "UPDATE phonebook SET " + u + " WHERE " + s
        cursor.execute(sql)
        conn.commit()
        print("The records with " + s + " are deleted.\n")

def deletecontacts():
    s = key_pair_reception('searching')
    if s != None:
        sql = 'DELETE FROM phonebook WHERE ' + s
        cursor.execute(sql)
        conn.commit()
        print("The records with " + s + " are deleted.\n")

def findcontacts():
    s = key_pair_reception('searching')
    if s != None:
        sql = 'SELECT surname, name, phone_number FROM phonebook WHERE ' + s + ' ORDER BY surname'
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)

# Основная программа
print ('\nWELCOME TO THE PHONE DIRECTORY')
conn = sqlite3.connect('my.db')  
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook (
                id integer PRIMARY KEY,
                name text NOT NULL,
                surname text,
                phone_number text)''');
m = -1  
while m != 0:
    print_menu()  
    m = int(input('Your choice: '))  
    if m == 1:  
        addcontact()
        continue
    elif m == 2:  
        displaybook()
        continue
    elif m == 3:  
        editcontacts()
        continue
    elif m == 4:  
        deletecontacts()
        continue
    elif m == 5:  
        findcontacts()
        continue
    elif m == 0:  
        print('The program is completed.\n')
        conn.close()
        sys.exit(0)  
    else:  
        print('Please follow instructions')
