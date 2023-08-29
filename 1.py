'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''


from random import *
import json
phone_book = {}
def save():
    with open("contact.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phone_book, ensure_ascii=False))
    print("контакт сохранен")

def load():
    global phone_book
    with open("contact.json", "r", encoding="utf-8") as fh:
        phone_book= json.load(fh)
        print("контакты загружены")

    '''print("загрузка контакта выполнена")'''
    return phone_book

'''phone_book = {"Дядя Петя" : {"номер": [999888, 999777], "ДР":"123", "email" : "irs@mail.ru"},
              "тетя Песя" : {"номер": [999444]}}
'''

def delete():
    try:
        name = input("Введите контакт, который хотите удалить: ")
        del phone_book[name]
        print("Контакт удален")
    except:
        print("Такого контакта не существует")


    
def change():
    try:
        name = input("Введите контакт, который хотите изменить: ")
        changes = input("Выберите что хотите изменить: номер, ДР, email: ")
        
        if changes == "номер":
            num = input("Введите новое значение: ")
            num2 = input("Введите новое второго значение: ")
            if num:
                phone_book[name]['номер'] = [num]

            if num2:
                phone_book[name]['номер'].append(num2)

        
        if changes == "ДР":
            dr = input("Введите новое значение: ")
            if dr:
                phone_book[name]['ДР'] = dr
        if changes == "email":
            mail = input("Введите новое значение: ")
            if mail:
                phone_book[name]['email'] = mail
        print("Контакт изменен")
    except:
        print("Такого контакта не существует")

while True:
    command = input("Введите команду: ")

    if command == "/add":
        name = input("Введите имя контакта: ")
        num = input("Введите номер: ")
        num2 = input("Введите второй номер: ")
        b_day =input("Введите ДР: ")
        mail= input("Введите email: ")
        contact = {}
        if num:
            contact["номер"] = [num]
        if num2:
            contact["номер"].append(num2)
        if b_day:
            contact["ДР"] = b_day
        if mail:
            contact["email"] = mail
        phone_book[name] = contact
        '''
phone_book[name] = {"номер": [num, num2], "ДР":b_day, "email" : mail}'''
        print("добавлен контакт")
    elif command =="/start":
        print("Heey,это справочник контактов, здесь можно управлять своими контактами")
    elif command == "/all":
        print("Список всех контактов: ")
        print(phone_book)
    elif command == "/find":
        name= input("Введите номер или телефон для поиска: ")
        if name in phone_book:
            print(name, phone_book[name])
    elif command == "/save":
        save()
        
    elif command == "/load":
        phone_book = load()
    elif command == "/stop":
        print("работа бота остановлена")
        break
    elif command == "/delete":
        delete()
    elif command == "/change":
        change()
    elif command == "/help":
        print("/start - начало работы бота \n/load - загрузка данных из файла(внешнее хранилище)\n/all - показать все контакты\n/stop - прекращение работы бота\n/add - добавление нового контакта\n/delete - удаление контакта\n/save - сохранение контакта")
        name = input("Введите имя контакта: ")

        
        



