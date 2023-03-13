from collections import UserDict
from datetime import datetime
import re
import pickle


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def generator(self):
        for name, datas in self.data.items():
            yield (f'Subscriber\'s {name} - {datas}')

    def iterator(self, N):
        iter = self.generator()
        try:
            if N > len(self.data):
                raise Error
        except:
            print(f'Records less than {N}')
        i = 0
        for i in range(N):
            try:
                print(next(iter))
                i += 1
            except StopIteration:
                pass


    def search_record(self, request):
        for key, value in self.data.items():
            if request in key or request in str(value):
                return (f'According to your request was found: {key} - {value}')
            else:
                return (f'Nothing found for your request')


    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            save_data = pickle.load(file)
        return save_data


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.birthday = birthday
        print(f'A new contact has been created for the subscriber {self.name}')
        if phone == None:
            self.phone_list = []
        else:
            self.phone_list = [phone]
            print(f'A phone number {self.phone_list} has been added to the contact {self.name}')


    def add_phone(self, phone_number):
        if phone_number not in self.phone_list:
            self.phone_list.append(phone_number)
            print(f'A new phone number {phone_number} has been added to the contact {self.name}')
        else:
            print(f'Entered number {phone_number} already exists')


    def delete_phone(self, phone_number):
        for ph in self.phone_list:
            if ph == phone_number:
                self.phone_list.remove(ph)
                print(f'Number {ph} has been deleted')
            else:
                print(f'Entered number {phone_number} not found')


    def edit_phone(self, phone_number, new_phone_number):
        for ph in self.phone_list:
            if ph == phone_number:
                self.phone_list.remove(ph)
                self.phone_list.append(new_phone_number)
                print(f'The number {ph} has been changed to {new_phone_number}')
            else:
                print(f'Entered number {phone_number} not found')


    def days_to_birthday(self, birthday):
        today = datetime.today()
        birthday = birthday.split('.')
        birthday = ' '.join(birthday)
        user_db = datetime.strptime(birthday, '%d %m %Y')
        user_db = user_db.replace(year=today.year)
        if user_db.date() < datetime.now().date():
            user_db = user_db.replace(year=today.year + 1)
        deltatime = user_db.date() - datetime.now().date()
        return (f'Until the birthday {deltatime.days} days.')


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    def __init__(self, name):
        pass


class Phone(Field):
    def __init__(self, phone = None):
        pass

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        phone = re.sub(r'[-|)|(|+| |]', '', phone)
        phone = phone.strip()
        self.__phone = phone


class Birthday(Field):
    def __init__(self, birthday=None):
        pass

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        if birthday == datetime.strptime(birthday, "%d.%m.%Y"):
            self.__birthday = birthday


class Error(Exception):
    pass

