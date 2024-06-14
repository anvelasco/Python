import mysql.connector
myDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "LivenTheBar!2024",
    database = "pythonx")
print(myDB)
myCur = myDB.cursor()
sql = "INSERT INTO user (userID, name, email, usrType) VALUES (%s,%s,%s,%s)"
val = ("1526","John","john@example.com","PRO")
myCur.execute(sql, val)
myDB.commit()
myCur.execute("SELECT * FROM user")
result = myCur.fetchall()
for i in result:
    print(i)
myDB.close()

