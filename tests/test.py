import bcrypt

password = b"132"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.checkpw(password, hashed):
    print("It matches")
else:
    print("Does not match.")