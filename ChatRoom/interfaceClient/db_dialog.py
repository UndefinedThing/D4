import sqlite3

from sqlite3 import Error
from datetime import datetime
from interfaceClient.passwords import *

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

        cur.execute("SELECT id, email, username, password, wins, looses, draws, created_at FROM Users WHERE username=?", (username,))
        user = cur.fetchone()

        cur.close()

        if (user is None):
            return "3///Aucun utilisateur ne correspond"
        elif (user is not None) and not verify_password(password, str(user[3])):
            return "3///Mot de passe incorrect"
        else :
            userInf = list(user)
            userInf.pop(3)
            return "0///"+"///".join(str(v) for v in userInf)

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
        cur.execute("SELECT id, email, username, wins, looses, draws, created_at FROM Users WHERE username=?", (newUsername,))
        user = cur.fetchone()

        dbconn.commit()
        cur.close()

        return "0///"+'///'.join(str(v) for v in user)

    except Error as e:
        print("Error while parsing database",e)