#!/usr/bin/python3 
import string as st
import random as rd 
import argparse as arg
import encrpt


#generate alphanumeric charactor
alphanum = st.ascii_letters + st.digits + st.punctuation

passwd = []


def gen(passwrdLength):
    global passwordHolder
    for _ in alphanum:
        if len(passwd) < int(passwrdLength):
            passwd.append(rd.choice(alphanum))
        # gen_p = passwd[-1]
    passwordHolder = ''.join(passwd)
    return passwordHolder
#store the pass in a file
def store_pass(password):
    with open('passfile', 'a+') as pass_file:
        
        pass_file.write(args.application +':' + gen(15) + '\n') 
        pass_file.close

    #check if gen-pass has been created

def pass_checker(application):
    with open('passfile','r') as file:
        x = file.read()
    #iterate through list check if website/application name exist in the list
        if application not in x:      
            print('[+] Succesfully created ')  
            store_pass(gen(args.passwrdLength))

        else:
            print('[+] Password already exists for this application {}'.format(args.application))         


#encrypt file after password are stored
#create command line args
def commandline():
    parser = arg.ArgumentParser(description='choose which app is the pass generated and length')
    parser.add_argument('-a', '--app', dest='application', help='choose the application you want the password to be generated for', required=True)
    parser.add_argument('-l', '--length', dest='passwrdLength', help='specify password length', required=True)
    # parser.add_argument('-ef', )
    parser.add_argument('-e', '--encrypt', dest='encrypted_file', help='specify password length')
    parser.add_argument('-d', '--decrypt', dest='decrypted_file', help='specify password length')
    parser.add_argument('-p', '--password', dest='password', help='specify password length' )


    args = parser.parse_args()
    if not args.application :
        print('[+] Please choose an application that the password will be used for. ' )
    elif not  args.passwrdLength:
        print('[+] Please specify a password length  ' )
    # elif not args.encrypted_file:
    #     print('[+] please choose a file location ')
    # elif not args.decrypted_file:
    #     print('[+] please choose a password to encrypt file with')
    # elif not args.password:
    #     print('[+] please choose a password to encrypt file with')
    else:
        return args

if __name__ == "__main__":
    args = commandline()
    global encryptor
    global secret_pass
    global loaded_key

    encryptor=encrpt.Encryptor()

    mykey=encryptor.key_create()
    secret_pass = encryptor.getKey(args.password )
    encryptor.key_write(mykey, 'mykey.key')
    loaded_key=encryptor.key_load('mykey.key')


    

    if args.encrypted_file:
        encryptor.file_encrypt(loaded_key,  args.encrypted_file, 'new',args.password)

    elif args.decrypted_file:

        if encryptor.getKey(args.password ) == secret_pass:

            encryptor.file_decrypt(loaded_key, 'new', args.decrypted_file, args.password)
            
        else:

            print('[-] Wrong pasword.Please try again to Decrypt file')
    else:

        gen(args.passwrdLength)
    
        pass_checker(args.application)


   
    
            
