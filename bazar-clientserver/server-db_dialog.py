import sqlite3
from sqlite3 import Error
from datetime import datetime

from server-passwords import *

def checkConn(dbconn):
    try:
        cur = dbconn.cursor()
        cur.execute("SELECT * FROM `Users`")

        user = cur.fetchall()

        return "OK"
    except Error as e:
        return e

def create_connection(db_file):
    dbconn = None
    try:
        dbconn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return dbconn

def usersConnection(dbconn, username, password) :

    try:
        cur = dbconn.cursor()

        cur.execute("SELECT * FROM Users WHERE username=?", (username,))
        user = cur.fetchone()
        
        cur.close()

        if (user is None):
            return "Aucun utilisateur ne correspond"
        elif (user is not None) and not verify_password(password, str(user[3])):
            return "Mot de passe incorrect"
        else :
            return '.'.join(str(v) for v in user)

    except Error as e:
        print("Error while parsing database",e)

def userRegister(dbconn, newMail, newUsername, passwd) :
    try:
        cur = dbconn.cursor()
        query = "INSERT INTO Users (Email, Username, Password, Created_at, Updated_at) VALUES (?, ?, ?, ?, ?)"

        cur.execute("SELECT * FROM Users WHERE Email=?", (newMail,))
        mailTaken = cur.fetchone()

        cur.execute("SELECT * FROM Users WHERE Username=?", (newUsername,))
        usernameTaken = cur.fetchone()

        if (mailTaken is not None):
            cur.close()
            return "1///Mail already taken"
        if (usernameTaken is not None):
            cur.close()
            return "2///Username already taken"

        timestamp = datetime.now()
        cur.execute(query, (newMail, newUsername, hash_password(passwd), timestamp, timestamp,))
        cur.execute("SELECT * FROM Users WHERE username=?", (newUsername,))
        user = cur.fetchone()

        print(user[2])

        dbconn.commit()
        cur.close()

        return "0///"+'///'.join(str(v) for v in user)

    except Error as e:
        print("Error while parsing database",e)

def select_all(dbconn, table):
    try:
        cur = dbconn.cursor()
        sql_query = """select * from %s"""
        cur.execute(sql_query % (table))

        rows = cur.fetchall()

        for row in rows:
            print(row)
        
        cur.close()
    except Error as e:
        print("Error while parsing database",e)
