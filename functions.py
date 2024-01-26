import sqlite3
import uuid
import bcrypt
def connect_to_database():
    return sqlite3.connect('profile.db')

def create_table():
    with connect_to_database() as conn:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS login (
                     userid TEXT,
                     useremail TEXT,
                     userhashed TEXT
                 )""")
def create_account():
    print('Create User Profile:')
    useremail = input('Email: ')
    password = input('Password: ').encode("utf-8")

    userhashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=17))
    userid = uuid.uuid4().hex[:4]
    profile = [userid, useremail, userhashed]
    print(profile)

    with connect_to_database() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM login WHERE useremail=?", (useremail,))

        if c.fetchone() is not None:
            print("Email already exists...")
        else:
            print("Creating account...")
            c.execute("INSERT INTO login (userid, useremail, userhashed) VALUES (?, ?, ?)", profile)
            conn.commit()
def login():
    print('Login to User Profile:')
    useremail = input('Email: ')
    password = input('Password: ').encode("utf-8")

    with connect_to_database() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM login WHERE useremail=?", (useremail,))

        result = c.fetchone()
        if result is not None:
            print("Email match")
            if bcrypt.checkpw(password, result[2]):
                print("Successful Login!")
            else:
                print("Password incorrect.")
        else:
            print("Email does not exist")

if __name__ == "__main__":
    create_table()
    create_account()
    login()