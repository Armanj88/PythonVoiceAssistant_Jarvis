import os
import pickle

if not os.path.exists("name.txt"):  
    name = input("What is your name? ")
    with open("name.txt", "w") as f:
        f.write(name)
    print("Hello, " + name + "! Welcome!")
if not os.path.exists("password.secret"):
    password = input("What is your password? Please enter a sentence because it will be used as a voice password: ").lower().strip()
    with open("password.secret", "wb") as f:
        pickle.dump(password, f)
    print("Your password has been saved!")
else:
    print("You are already do configurations!")
    print("Please start jarvis.py file to run jarvis!")
    
input("Press enter to exit...")