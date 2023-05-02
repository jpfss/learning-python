# -*- coding: utf-8 -*-

# =============================================================================
# mysql
# =============================================================================
import pymysql

# Open database connection
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : %s " % data)

# disconnect from server
db.close()
# =============================================================================
# Creating Database Table
# =============================================================================
# Open database connection
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()
# =============================================================================
# INSERT Operation
# =============================================================================
# Open database connection
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()

# insert其他格式

# Open database connection
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
   LAST_NAME, AGE, SEX, INCOME) \
   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
    ('Mac', 'Mohan', 20, 'M', 2000)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
# =============================================================================
# READ Operation
# =============================================================================
# Open database connection
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM EMPLOYEE \
      WHERE INCOME > '%d'" % (1000)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # Now print fetched result
        print("fname = %s,lname = %s,age = %d,sex = %s,income = %d" %
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# disconnect from server
db.close()
# =============================================================================
# Update Operation
# =============================================================================
# Open database connection
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1
WHERE SEX = '%c'" % ('M')
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
# =============================================================================
# DELETE Operation
# =============================================================================
# Open database connection
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
# =============================================================================
# Performing Transactions
# =============================================================================
# Atomicity − Either a transaction completes or nothing happens at all.
# Consistency − A transaction must start in a consistent state and leave the system in a consistent state.
# Isolation − Intermediate results of a transaction are not visible outside the current transaction
# Durability − Once a transaction was committed, the effects are persistent, even after a system failure
# Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
# =============================================================================
# COMMIT Operation
# =============================================================================
db.commit()
# =============================================================================
# ROLLBACK Operation
# =============================================================================
db.rollback()
# =============================================================================
# Disconnecting Database
# =============================================================================
db.close()
