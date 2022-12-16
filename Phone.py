import sys
import sqlite3  

def print_menu():  
    print ('\nПожалуйста выберете действие:')  
    print('1. Добавить контакт')  
    print('2. Показать все контакты')  
    print('3. Редактировать контакт')  
    print('4. Удалить контакт')
    print('5. Найти контакт')
    print('0. Выйти из справочника')

def addcontact():
    while True:  
        name = input("Как фамилия человека?: ") 
        if len(name) != 0:  
            break  
        else:  
            print("Пожалуйста, введите имя контакта")     
    while True:  
        surname = input("Как имя человека: ")  
        if len(surname) != 0:  
            break  
        else:  
            print("Пожалуйста, введите фамилию")    
    while True:  
        num = input("Какой номер телефона у человека? (допускаются только цифры): ")  
        if not num.isdigit():  
            print("Пожалуйста, вводите только цифры")  
            continue  
        elif len(num) != 10:  
            print("Введите 10-значный номер телефона без запятых, пробелов и знаков препинания.")  
            continue  
        else:  
            break  
    cursor.execute('''INSERT INTO phonebook (name, surname, phone_number) VALUES (?,?,?)''',
                                                                         (name, surname, num))  
    conn.commit()      
    print("Новый контакт " + surname + ' ' + name + " добавлен в таблицу телефонной книги")

def displaybook():
    cursor.execute("SELECT surname, name, phone_number FROM phonebook ORDER BY surname")
    results = cursor.fetchall()
    print(results)

def key_pair_reception(str):
    print ("\nПожалуйста сделайте выбор " + str + " (от 1 до 3)")  
    print('1. Имя')  
    print('2. Фамилия')  
    print('3. Телефонный номер')  
    print('0. Возврат в меню')
    n = int(input('Ваш выбор: '))
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
print ('\nДОБРО ПОЖАЛОВАТЬ В ТЕЛЕФОННЫЙ СПРАВОЧНИК')
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
    m = int(input('Ваш выбор: '))  
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
        print('Вы завершили работу со справочником.\n')
        conn.close()
        sys.exit(0)  
    else:  
        print('Please follow instructions')
