import csv
import json
import os
import pickle


# A: processes all inputs and returns in a list
def check_input(name_in, birthday_in, age_in, email_in, password_in):
    """processes all inputs and returns in a list"""
    names = name_in.split()
    for item in names:
        if not item.isalpha():
            print("\ninvalid name")
            return
    date = birthday_in.split()
    num_date = []
    for item in date:
        if not item.isnumeric():
            print("\ninvalid birthday")
            return
        else:
            num_date.append(int(item))

    year = num_date[2]

    if year < 1917 or year > 2015:
        print(year)
        print("\ninvalid birthday")
        return

    if not age_in.isnumeric():
        print("\ninvalid age")
        return

    char = email_in.find("@")
    if char == -1:
        print("\ninvalid email")
        return

    return name_in.title(), num_date, int(age_in), email_in, password_in

# C: returns data from csv file
def return_users_csv():
    """returns data from csv file"""

    stored_data = []
    with open('csv_file.csv', 'r') as file:
        reader = csv.reader(file)
        print(next(reader))
        for row in reader:
            stored_data.append(row)
        file.close()
        return stored_data

# P: returns data from pickle file
def return_users_pickle():
    """returns data from pickle file"""

    stored_data = []
    with open('pickle_file.pickle', 'rb') as file:
        try:
            while True:
                stored_data.append(pickle.load(file))
        except EOFError:
            pass
            file.close()
    return stored_data

# J: returns data from json file
def return_users_json():
    """returns data from json file"""
    with open("storage.json", "r") as file:
        #print(file.read())
        #data_j = json.loads(file.read())
        data_j = []
        return data_j


# A: collect input from user
name = input("name: ")
birthday = input("birthday (mm dd yyyy): ")
age = input("age: ")
email = input("email: ")
password = input("password: ")

# C: creates a titles for csv file data
header = ["name", "birthday", "age", "email", "password"]
# A: stores the processed data as list
more_data = check_input(name, birthday, age, email, password)

# A: creating files:
data = []
if os.stat("storage.json").st_size == 0:
    with open('storage.json', 'w') as f:
        json.dump(data, f)
        f.close()
if os.stat("csv_file.csv").st_size == 0:
    with open('csv_file.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
        f.close()
# if os.stat("pickle_file.pickle").st_size == 0:
#     with open('pickle_file.pickle', 'wb') as f:
#         pickle.dump(data, f)
#         f.close()

# A: if data meets requirements, the data is stored
if more_data is not None:
    with open("storage.json", "w") as outfile:
        if not return_users_json():
            all_data = [return_users_json(), more_data]
        else:
            all_data = [more_data]
        json.dump(all_data, outfile)
    with open('csv_file.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(more_data)
        f.close()
    with open('pickle_file.pickle', 'ab+') as f:
        pickle.dump(more_data, f)

print(return_users_pickle())

