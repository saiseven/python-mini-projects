from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''





def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

# def write_key2():
#     with open('key2.key', 'a') as f:
#         f.write("\n")
#         f.write( fer.encrypt("1234".encode()).decode())
        
# write_key2()

def read_key(pwd):
        allow=False
        with open("key2.key", "r") as f:
            p=f.read()

            if fer.decrypt(p.encode()).decode()==pwd:
                allow=True
            else:
                allow=False
        return allow




def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

password = input("Please enter master password: ")
if read_key(password):
    pass
else:
    print("Incorrect password")
    quit()
        
while True:
    
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue 