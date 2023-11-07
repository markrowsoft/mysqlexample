import mysql.connector
import pprint as pp
# Prompt user for input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
phone = input("Enter your phone number: ")
social = input("Enter your social security number: ")

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="myusers"
)

# Insert user input into database
mycursor = mydb.cursor()
sql = "INSERT INTO user_tb (first_name, last_name, phone, social) VALUES (%s, %s, %s, %s);"
values = (first_name, last_name, phone, social)
mycursor.execute(sql, values)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
select_sql = "select * from `user_tb` where `first_name`=%s;"
mycursor.execute(select_sql, (first_name,))
data = mycursor.fetchall()

pp.pprint(data)
mycursor.close()



