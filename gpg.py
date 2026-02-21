from gnupg import GPG
from getpass import getpass
import json
from sys import exit


with open('config.json', 'r', encoding='utf-8') as f: conf = json.load(f)

gpg = GPG()
styles, ui = conf['styles'], conf['ui']


# Encryption
def encrypt():
    data = input(ui['input_data'])
    file_name = input(ui['input_file']) + conf['settings']['extension']
    password = getpass(ui['input_password'])
    symmetric = conf['settings']['cipher']
    
    encription = gpg.encrypt(data, 
                             recipients=None, 
                             symmetric=symmetric, 
                             passphrase=password,
                             output=file_name)

    if (encription.ok):
        print(f"{styles['info']}{ui['success_encryption']}{styles['reset']}")
    else:
        print(f"{styles['error']}{ui['error_input']}{styles['reset']}")
    exit()


# Decryption
def decrypt():
    file_name = input(ui['input_file']) + conf['settings']['extension']
    password = getpass(ui['input_password'])
    try:
        with open(file_name, 'rb') as f:
            decryption = gpg.decrypt_file(f, passphrase=password)
            if (decryption.ok):
                print(f"{styles['info']}{ui['success_decryption']}{styles['reset']}\n{decryption}")
            else:
                print(f"{styles['error']}{ui['error_input']}{styles['reset']}")
            exit()
    except FileNotFoundError:
        print(f"{styles['error']}{ui['error_file']}{styles['reset']}")
        exit()

actions = {'1': encrypt, '2': decrypt, '3': exit}

while True:
    choice = input(ui['menu'])
    actions.get(choice, lambda: print("?"))()
