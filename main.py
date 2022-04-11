import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()


#c.execute("""CREATE TABLE employee (
 #           first text,
  #          last text,
   #         pay integer
    #        )""")

#c.execute("INSERT INTO employee VALUES ('Mary', 'Schafer', 50000)")

for num in range(2):
    first_name = input("What is a good first name: ")
    last_name = input("What is a good last name: ")
    pay = input("Enter their pay: ")
    c.execute(f"INSERT INTO employee VALUES ('{first_name}', '{last_name}', {pay})")
    print()


c.execute("SELECT * FROM employee")
print(c.fetchall())
conn.commit()

conn.close()