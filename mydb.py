import mysql.connector
dataBase = mysql.connector.connect(
    host ='localhost',
    user = 'devuser',
    passwd = 'devpass',
    database = 'CRMAPP',

)
# creating a cursor object
cursor = dataBase.cursor()

# create a database


print("lets see")