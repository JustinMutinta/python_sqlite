import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()


def create_new_table():
    c.execute("""CREATE TABLE employee (
                first text,
                last text,
                pay integer
                )""")


def database_input(first_name, last_name, pay):
    c.execute(f"INSERT INTO employee VALUES ('{first_name}', '{last_name}', {pay})")


def database_add_quantity(num):
    for iteration in range(num):
        first_name = input("Enter a good first name: ")
        last_name = input("Enter a good last name: ")
        pay = input("Enter their pay: ")
        database_input(first_name, last_name, pay)
        print()


def database_remove_user(first_name, last_name):
    c.execute(f"DELETE FROM employee WHERE first='{first_name}' AND last='{last_name}'")


def update_pay(first_name, pay):
    c.execute(f"UPDATE employee SET pay = {pay} WHERE first = '{first_name}'")


def output_database_contents():
    c.execute("SELECT * FROM employee")
    print(c.fetchall())


def output_single_employee(first_name):
    c.execute(f"SELECT * FROM employee WHERE first = '{first_name}'")
    print(c.fetchall())


output_database_contents()


number_choice = int(input("How many would you like to add to the database? "))


if number_choice < 1:
    print("No entries to be added")
else:
    database_add_quantity(number_choice)
    output_database_contents()


ask_to_delete = input("Would you like to delete an employee: y/n? ...")


if ask_to_delete == "y":
    first_name = input("What is their first name? ")
    last_name = input("What is their last name? ")
    database_remove_user(first_name, last_name)
    output_database_contents()
elif ask_to_delete == "n":
    print("No entries to be deleted")
else:
    print("I don't know what that is")
    pass

update_user_pay = input("Would you like to update a user's pay?...")

if update_user_pay == 'y':
    output_database_contents()
    name = input("Enter their first name: ")
    output_single_employee(name)
    new_pay = input("Enter new pay: ")
    update_pay(name, new_pay)
    output_single_employee(name)
elif update_user_pay == 'n':
    print("Moving on...")
    pass
else:
    print("I don't know what that means")
    pass


conn.commit()
conn.close()
