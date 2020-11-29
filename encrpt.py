#!/usr/bin/python3
from cryptography.fernet import Fernet
import hashlib
import main



class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key
    
    def getKey(self, password):
        
        hasher = hashlib.sha512(password.encode('utf-8'))
        return hasher.digest()

    def file_encrypt(self, key, original_file, new_file, password):
            
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open (new_file, 'wb') as file:
            file.write(encrypted)

        


    def file_decrypt(self, key, encrypted_file, decrypted_file, password): 

                
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)




