#!/usr/bin/python3 
import string as st
import random as rd 
import argparse as arg
import encrpt
import subprocess as sb


#generate alphanumeric charactor
alphanum = st.ascii_letters + st.digits + st.punctuation

passwd = []
global application
global length
global file_to_encrypt
file_to_encrypt = ''
application = ''
length = 0


def gen(passwrdLength):
    global passwordHolder
    for _ in alphanum:
        if len(passwd) < int(passwrdLength):
            passwd.append(rd.choice(alphanum))
        # gen_p = passwd[-1]
    passwordHolder = ''.join(passwd)
    return passwordHolder
#store the pass in a file
def store_pass(password, app):
    with open('passfile', 'a+') as pass_file:
        
        pass_file.write(app +':' + gen(15) + '\n') 
        pass_file.close

    #check if gen-pass has been created

def pass_checker(application):
    with open('passfile','r') as file:
        x = file.read()
    #iterate through list check if website/application name exist in the list
        if application not in x:      
            print('[+] Succesfully created ')  
            store_pass(gen(length), application)

        else:
            print('[x] Password already exists for this application {}'.format(application))         

def main():
    try:
        while True:

            options = input("please choose:\n 1)To generate password and save it\n 2)encrypt file\n 3)decrypt file \nChoice: ")
        
            if int(options) == 1 :

                file_name = input('what would you like your password file to be called: ')
                
                sb.run(['touch' , file_name])

                #user input for appplication  
                application = input('please choose an application you would like a password to be generated for: ')
                #user input for password length
                length = input('please choose the length of the password to be generated: ')
                #store password
                if length != 0 and application != '' :
                    gen(length)
                    pass_checker(application)
                else:
                    print('please enter an application and password')
                    continue
                #ask user if they want to encrypt file or decrypt
                # options2 = input("Do you want to encrypt file or Decrypt\n if you want to encrypt press '1' if you would like to decrypt press '2':")
                    #if encrypt 
            elif int(options) == 2:
                encryptor=encrpt.Encryptor()
                enc_pas = input('please enter the password you want to encrypt file: ')

                
                file_to_encrypt = input('Name of file to be encrypted? ')
                global ecrypt_pass
                ecrypt_pass = encryptor.getKey(enc_pas )
                mykey=encryptor.key_create()
                # encryptor.key_write(bytes(enc_pas, 'utf-8'), 'mykey.key' )
                encryptor.key_write(mykey, 'mykey.key')
                loaded_key=encryptor.key_load('mykey.key')
                encryptor.file_encrypt(loaded_key, file_to_encrypt , 'new')
                with open('mykey.key', 'a') as pass_file:
                    pass_file.write('\n' + str(ecrypt_pass))
                    pass_file.close()


                # provide password that will be used during decryption
            #if decrypt 
            elif int(options) == 3:
                encryptor=encrpt.Encryptor()
                with open('mykey.key', 'r') as pass_file:
                    # pass_file.write('\n' + str(ecrypt_pass))
                    passwd1 = pass_file.readlines()[1]
                    pass_file.close()

                dec_pas = input('please enter the password you used to encrypt file: ')
                loaded_key=encryptor.key_load('mykey.key')
                
                new = encryptor.getKey(dec_pas)
            #check if password provided during encryption is the same as the one being provided during decryption of file
                if str(new) == str(passwd1):
                    encryptor.file_decrypt(loaded_key, 'new', 'dec')
                    print('thank you')
                else:
                    print(new)
                    print(passwd1)
                    print('[-] Wrong password.Please try again to Decrypt file')
            #ask for password before decrypting
            else:
                print('Thank you!')
    except KeyboardInterrupt :
        print('[+] Script exited!!!')
    # encryptor=encrpt.Encryptor()
    
            

# b'u\x0b\xe7\xccR\xba\x8dPf8\x1c_5\xc9\x15,A\xd9X\xa2\x06\xcf\x0c^\xf4&\x026*G\xd9\x8a\xedn\r\x97\x8b\xd7\x02C\x04\x89U>\xe6g\xdf\xa6\xeaL\x7ffA\xbb\xa8qC\xc9\x08\x93~\xd8\xe1\xaa'
# b'u\x0b\xe7\xccR\xba\x8dPf8\x1c_5\xc9\x15,A\xd9X\xa2\x06\xcf\x0c^\xf4&\x026*G\xd9\x8a\xedn\r\x97\x8b\xd7\x02C\x04\x89U>\xe6g\xdf\xa6\xeaL\x7ffA\xbb\xa8qC\xc9\x08\x93~\xd8\xe1\xaa'





if __name__ == "__main__":
    main()