import argparse
import hashlib
#from itertools import combinations_with_replacement or permutations
import random

#run with 'python3 crack.py' + extension
#arguments
parser = argparse.ArgumentParser(description='python password cracker')
parser.add_argument('-m', '--mode', help = 'b for bruteforce or d for dictionary attack', required= True)
parser.add_argument('-i', '--input', help = 'Input password hash', required= True)
parser.add_argument('-t', '--type', help = 'hash type, md5, sha256, or pt (for plaintext)', required= True)
args = parser.parse_args()

#functions----------------------------------------
def dictionary_attack(word, target):
    #if needed, hash it
    hashtype = args.type
    if(hashtype== 'sha256'):
        wordbytes= word.encode('utf-8')
        wordhash = hashlib.sha256(wordbytes)
        word = wordhash.hexdigest()
    elif(hashtype=='md5'):
        wordbytes= word.encode('utf-8')
        wordhash = hashlib.md5(wordbytes)
        word = wordhash.hexdigest()
    if word == target:
        return True
    return False

#dictionary attack--------------------------------
if args.mode=='d':
    print('starting dictionary attack...')
    #take in file from user and open
    filename = input('Enter dictionary file name (don\'t put anything if you want to use the top 10000 passwords):')
    #if the user put nothing, just use the passwords file
    if len(filename)== 0:
        filename = 'passwords.txt'
    with open(filename, 'r') as dictfile:
        #loop through it line by line
        found = False
        for line in dictfile:
            #run da function to compare
            if dictionary_attack(line.rstrip(), args.input)==True:
                print('Matched! %s' %(line))
                found = True
                break
            else:
                continue
        #otherwise
        if found == False:
            print('Couldn\'t find match rip lol')

#brute force attack-------------------------------
elif args.mode=='b':
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphlist = list(alphabet)
    attempt = ""
    while(attempt!= args.input):
        attempt = random.choices(alphlist, k= len(args.input))
        print('trying %s' %(attempt))
        if(attempt==list(args.input)):
            print('password found! %s' %(attempt))
            break
#default------------------------------------------
else:
    print('bruh')
    quit()
