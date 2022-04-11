import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()


#c.execute("""CREATE TABLE employee (
 #           first text,
  #          last text,
   #         pay integer
    #        )""")

#c.execute("INSERT INTO employee VALUES ('Mary', 'Schafer', 50000)")

c.execute("SELECT * FROM employee WHERE last='Schafer'")
print(c.fetchall())
conn.commit()

conn.close()