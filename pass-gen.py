#!/usr/bin/python3 
import string as st
import random as rd 
import argparse as arg


#generate alphanumeric charactor
alphanum = st.ascii_letters + st.digits + st.punctuation

passwd = []





def gen(passwordLength):
    global passwordHolder
    for _ in alphanum:
        if len(passwd) < int(passwordLength):
            passwd.append(rd.choice(alphanum))
        # gen_p = passwd[-1]
    passwordHolder = ''.join(passwd)
    return passwordHolder
    
            

#store the pass in a file
def store_pass(password):
    with open('passfile', 'a+') as pass_file:
        
        pass_file.write(args.application +': ' + gen(15) + '\n')
        pass_file.close
#check if gen-pass has been created
#encrypt file after password are stored
#create command line args
def commandline():
    parser = arg.ArgumentParser(description='choose which app is the pass generated and length')
    parser.add_argument('-p', '--app', dest='application', help='choose the application you want the password to be generated for')
    parser.add_argument('-l', '--length', dest='passwordLength', help='specify password length')



    args = parser.parse_args()
    

    if not args.application :
        print('[+] Please ' + args.application.help)
    elif not  args.passwordLength:
        print('[+] Please ' + args.passlen.help)
    else:
        return args








args = commandline()
gen(args.passwordLength)
store_pass(gen(args.passwordLength))
            
    # print(gen(args.passwordLength))

