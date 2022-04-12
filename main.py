import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()


#c.execute("""CREATE TABLE employee (
 #           first text,
  #          last text,
   #         pay integer
    #        )""")

#c.execute("INSERT INTO employee VALUES ('Mary', 'Schafer', 50000)")

def database_input(first_name, last_name, pay):
    c.execute(f"INSERT INTO employee VALUES ('{first_name}', '{last_name}', {pay})")

def database_add_quantity(num):
    for iteration in range(num):
        first_name = input("Enter a good first name: ")
        last_name = input("Enter a good last name: ")
        pay = input("Enter their pay: ")
        database_input(first_name, last_name, pay)
        print()

number_choice = int(input("How many would you like to add to the database? "))

if number_choice < 0:
    pass
else:
    database_add_quantity(number_choice)

#c.execute("SELECT * FROM employee WHERE pay > 20000")
c.execute("SELECT * FROM employee")
print(c.fetchall())
conn.commit()

conn.close()