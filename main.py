from collections import UserDict
from datetime import date
from datetime import datetime

class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {}

class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phone_list = [] # create a list to accommodate multiple phone records

    def add_phone(self, phone):
        self.phone_list.append(Phone(phone)) #add phone record to a list

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value
   
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value:
            self.__value = value


class Name(Field):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value.isalpha():
            print('all good')
            self.__value = new_value
        else:
            print('Name can only contain letters.')
            raise Exception('Name can only contain letters')
            


class Phone(Field):
    def __init__(self, value):
        self.value = value

    def edit_number(self, new_number):
        self.value = new_number

class Birthday(Field):
    def __init__(self, date_of_birth):
        year_of_birth = date_of_birth.split(' ')[0]
        month_of_birth = date_of_birth.split(' ')[1]
        day_of_birth = date_of_birth.split(' ')[2]
        self.date = date(int(year_of_birth), int(month_of_birth), int(day_of_birth))

    def days_to_birthday(self):
        delta1 = datetime(date.today().year, self.date.month, self.date.day)
        delta2 = datetime(date.today().year+1, self.date.month, self.date.day)
        return ((delta1 if delta1 > datetime.today() else delta2) - datetime.today()).days

address_book = AddressBook()

def hello(user_input):
    print('How can I help you?')

def end_program(user_input):
    print('Good bye!')
    exit()

def add_contact(user_input):
    contact_name = user_input.split(' ')[2]
    contact = Record(contact_name) # create record with given name
    address_book.contacts[contact.name.value] = contact #add record to address book
    print(f'Contact {contact_name} has been added to the AddressBook.')

def add_phone(user_input):
    contact_name = user_input.split(' ')[2]
    contact_number = user_input.split(' ')[3]
    result =  list(filter(lambda name: name == contact_name, address_book.contacts.keys()))
    if len(result) > 0:
        address_book.contacts[result[0]].add_phone(contact_number)
        print(f'Number {contact_number} has been added to contact named {contact_name}')
    else:
        print(f'There is no contact {contact_name}')

def edit_phone(user_input):
    contact_name = user_input.split(' ')[2]
    contact_old_number = user_input.split(' ')[3]
    contact_new_number = user_input.split(' ')[4]
    contacts_found =  list(filter(lambda name: name == contact_name, address_book.contacts.keys()))
    if len(contacts_found) > 0:
        phone_record_found = list(filter(lambda phone_record: phone_record.value == contact_old_number, address_book.contacts[contacts_found[0]].phone_list))
        if len(phone_record_found) > 0:
            phone_record_found[0].edit_number(contact_new_number)
            print(f'Contact {contact_name} number {contact_old_number} has been changed to {contact_new_number}.')
        else:  
            print(f'Contact {contact_name} has no number {contact_old_number} therefore it cant be edited.')
    else:
        print(f'There is no contact {contact_name}')

def delete_phone(user_input):
    contact_name = user_input.split(' ')[2]
    contact_number_to_delete = user_input.split(' ')[3]
    contacts_found =  list(filter(lambda name: name == contact_name, address_book.contacts.keys()))
    if len(contacts_found) > 0:
        phone_record_found = list(filter(lambda phone_record: phone_record.value == contact_number_to_delete, address_book.contacts[contacts_found[0]].phone_list))
        if len(phone_record_found) > 0:
            address_book.contacts[contacts_found[0]].phone_list.remove(phone_record_found[0])
            print(f'Contact {contact_name} number {contact_number_to_delete} has been deleted.')
        else:  
            print(f'Contact {contact_name} has no number {contact_number_to_delete} therefore it cant be deleted.')
    else:
        print(f'There is no contact {contact_name}')

def add_birthday(user_input):
    contact_name = user_input.split(' ')[2]
    contact_birthday_year = user_input.split(' ')[3]
    contact_birthday_month = user_input.split(' ')[4]
    contact_birthday_day = user_input.split(' ')[5]
    contact_birthday = contact_birthday_year + " " + contact_birthday_month + " " + contact_birthday_day
    result =  list(filter(lambda name: name == contact_name, address_book.contacts.keys()))
    if len(result) > 0:
        address_book.contacts[result[0]].add_birthday(contact_birthday)
        print(f'Birthday {contact_birthday} has been added to contact named {contact_name}')
    else:
        print(f'There is no contact {contact_name}')

def show_phone(user_input):
    contact_name = user_input.split(' ')[2]
    result =  list(filter(lambda name: name == contact_name, address_book.contacts.keys()))
    if len(result) > 0:
        for phone_number in address_book.contacts[result[0]].phone_list:
            print(phone_number.value)
    else:
        print(f'There is no contact {contact_name}')

def show_birthday(user_input):
    contact_name = user_input.split(' ')[2]
    result =  list(filter(lambda name: name == contact_name, address_book.contacts.keys()))
    if len(result) > 0:
        if address_book.contacts[result[0]].birthday:
            print(str(address_book.contacts[result[0]].birthday.date))
            print(f'Days to birthday: {str(address_book.contacts[result[0]].birthday.days_to_birthday())}')
        else:
            print(f'You didnt add birthday to contact {contact_name}')
    else:
        print(f'There is no contact {contact_name}')

def show_all(user_input):
    print('|{:^30}|'.format('-----All contacts-----'))
    for contact_name, contact_record in address_book.contacts.items():        
        print('|{:^30}|'.format(contact_name))
        for phone_number in contact_record.phone_list:
            print('|{:^30}|'.format(phone_number.value))
        if address_book.contacts[contact_name].birthday:
            date_to_print = address_book.contacts[contact_name].birthday.date
            print('|{:^30}|'.format('Birthday'))
            print('|{:^30}|'.format(str(date_to_print)))
    print('|{:^30}|'.format('-----End of list-----'))

def unknown_command(user_input):
    print('Unknown command')

def help(user_input):
    print('Commands format:')
    print('add contact NAME')
    print('add phone NAME PHONE')
    print('edit phone NAME OLD_NUMBER NEW_NUMBER')
    print('delete phone NAME NUMBER_TO_DELETE')
    print('add birthday NAME YYYY MM DD')
    print('show phone NAME')
    print('show birthday NAME')
    print('show all')

COMMANDS = {
    'hello': hello,
    '.': end_program,
    'close': end_program,
    'good bye': end_program,
    'exit': end_program,
    'add contact': add_contact,
    'add phone': add_phone,
    'edit phone': edit_phone,
    'delete phone': delete_phone,
    'add birthday': add_birthday,
    'show phone': show_phone,
    'show birthday': show_birthday,
    'show all': show_all,
    'help': help
}

def get_handler(user_input):
    """Functions checks user input and return appropiate functions if correct command had been entered."""
    for command in COMMANDS.keys(): #iterate through commands
        if user_input.lower().startswith(command): #checks if user input starts with a knowns command
            return COMMANDS[command]
        else:
            continue
    return unknown_command #if there was no match it returns 'unknown command'

def main():
    print('Type "help" to learn about commands')
    while True:
        user_input = input('Enter your next command: ')
        handler = get_handler(user_input)
        handler(user_input)



if __name__ == '__main__':
    add_contact('add contact Marika')
    add_birthday('add birthday Marika 1990 05 20')
    add_phone('add phone Marika 123321')
    main()