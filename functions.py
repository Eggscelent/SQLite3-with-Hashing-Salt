import sqlite3, uuid, bcrypt
from validate_email import validate_email
from termcolor import colored
from colorama import *
from getpass import getpass

init()

def validemail(useremail):
    is_valid = validate_email(email_address=useremail, \
        check_regex=True, check_mx=True, \
        from_address='my@from.addr.ess', helo_host='my.host.name', \
        smtp_timeout=10, dns_timeout=10, use_blacklist=True)

def createaccount():

    print(colored('Create User Profile:', 'yellow'))
    useremail = input('Email: ')
    #password = input('password: ').encode("utf-8")
    password = getpass("Password: ").encode("utf-8")
    print(password)

    validemail(useremail)

    userhashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=17))
    userid = uuid.uuid4().hex[:4]
    profile = [userid, useremail, userhashed]
    print(profile)

    conn = sqlite3.connect('profile.db')
    c = conn.cursor()

    #create a table
    #c.execute("""CREATE TABLE login (
       # userid integer,
      #  useremail text,
     #   userhashed text
    #)""")

    c.execute("insert into login (userid, useremail, userhashed) values (?, ?, ?)", (userid, useremail, userhashed))
    conn.commit()

    c.execute("SELECT * FROM login WHERE useremail='jackryder1@live.com.au'")

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
            login()
    else:
        print(colored("Email does not exist", "red"))
        login()
