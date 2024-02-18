from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            site, user, passw = data.split("|")
            print("Site/App:", site, "User:", user + ", Password:", fer.decrypt(passw.encode()).decode())

def add():
    site = input("Site/App: ")
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as file: #gets the file and saves to variable "file"
        file.write(site + "|" + name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        
def search(ans):
    found = False
    ans = str(ans)
    with open("passwords.txt", "r") as file: #opens text file
        for line in file.readlines(): #loops through lines (different passwords for sites)
            if(str(line.lower()).find(ans.lower()) != -1): #if the site searched for is found in the line
                data = line.rstrip()
                site, user, passw = data.split("|")
                print("Site/App:", site, "User:", user + ", Password:", fer.decrypt(passw.encode()).decode())
                found = True
                break
        if not found:
            print("Site/app not found in the file")
            
def delete(ans):
    i = 0
    ans = str(ans)
    with open("passwords.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if(str(line.lower()).find(ans.lower()) != -1): #if the site searched for is found in the line
                del lines[i]
                break
            else:
                i += 1
        with open("passwords.txt", "w") as nfile:
            for line in lines:
                nfile.write(str(line))
        print("done")
    
        

while True:
    mode = input("Would you like to add a new password, view existing ones, search by site, or delete a site password? (view, add, search, delete), press q to quit: ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "search":
        ans = input("What site/app would you like to search for? ")
        search(ans)
    elif mode == "delete":
        ans = input("What site do you want to delete the password of? ")
        delete(ans)
    else:
        print("Invalid mode.")
        continue