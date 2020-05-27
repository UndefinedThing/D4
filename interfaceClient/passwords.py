###################################
#       INTALLS : - passlib       #
###################################
from passlib.hash import pbkdf2_sha512

inf = "$pbkdf2-sha512$95846$"

def hash_password(password):
    try:
        hashed_password = pbkdf2_sha512.using(salt_size=16, rounds=95846).hash(password)

        print(hashed_password[21:])

        return hashed_password[21:]

    except Exception as e:
        print(e)

def verify_password(password, hashed):
    global inf
    return pbkdf2_sha512.verify(password, inf + hashed)