import sqlite3, uuid, bcrypt, sys
from validate_email import validate_email
from termcolor import colored
from colorama import *
from getpass import getpass

init()

def createaccount():

    print(colored('Create User Profile:', 'yellow'))
    useremail = input('Email: ')
    password = getpass("Password: ").encode("utf-8")

    is_valid = validate_email(useremail, verify=True)

    userhashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=17))
    userid = uuid.uuid4().hex[:4]
    profile = [userid, useremail, userhashed]
    print(profile)

    conn = sqlite3.connect('profile.db')
    c = conn.cursor()

    c.execute("SELECT * from login WHERE useremail= ?", (useremail,))
    if c.fetchone() is not None:
        print(colored("email already exists...", "yellow"))
    else:
        print(colored("creating account...", "green"))
        c.execute("insert into login (userid, useremail, userhashed) values (?, ?, ?)", (userid, useremail, userhashed))
        conn.commit()

        c.execute("SELECT * FROM login WHERE useremail=useremail")

        print(c.fetchall())

        conn.commit()
        conn.close()

def login():
    conn = sqlite3.connect('profile.db')
    c = conn.cursor()

    print(colored('Login to User Profile:', 'yellow'))
    useremail = input('email: ')
    password = input('password: ').encode("utf-8")

    c.execute("SELECT * from login WHERE useremail= ?", (useremail,))
    if c.fetchone() is not None:
        print(colored("email match", "green"))
        try:
            results = c.execute("SELECT * from login WHERE useremail= ?", (useremail,)).fetchone()
            print(colored(results, "yellow"))
        finally:
            c.close()

        if bcrypt.checkpw(password, results[2]):
            print(colored("Successful Login!", "green"))
        else:
            print(colored("Password incorrect.", "red"))
    else:
        print(colored("Email does not exist", "red"))

def createtable():
    conn = sqlite3.connect('profile.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE login (
            userid integer,
            useremail text,
            userhashed text
        )""")