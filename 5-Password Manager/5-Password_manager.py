from cryptography.fernet import Fernet
# for encryption and decryption purposes


def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


# write_key()                                               # used this function only once to create a single key in key.key file bcoz it becomes very complicated further

master_pwd = input("What is the master password? ")

key = load_key() + master_pwd.encode()                      # .encode() - coverts given text into bytes
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()                    # .rstrip() - Return a copy of the string with trailing (end) whitespace removed.
            user, passw = data.split(" | ")         # .split(sep) - Return a LIST of the Substrings in the string, using sep (separator used to split the string) as the separator string.
            print( "User:", user, "| Password:", fer.decrypt(passw.encode()).decode() )


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    # file = open('passwords.txt', 'a')                                 # normal file opening and appending method (manually close as well)
    # file.close()
    
    with open('passwords.txt', 'a') as f:                                   # 'with' keyword allows you to automatically close the file after its use 
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")   # .encrypt() - takes data in bytes for encryption. So thats why pwd(password) is converted into bytes using encode() function


while True:
    mode = input("\nMENU\n1. View\n2. Add\n3. Quit\nEnter your choice: ")

    if mode == '1':
        recheck_mpwd = input("Enter Master Password: ")
        if recheck_mpwd == master_pwd:
            print()
            view()
        else:
            print("Error! Master Password does not match!")
    elif mode == '2':
        add()
    elif mode == '3':
        break
    else:
        print("Invalid mode!")
        continue