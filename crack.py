import argparse
import hashlib
#run with 'python3 crack.py' + extension
#arguments
parser = argparse.ArgumentParser(description='python password cracker')
parser.add_argument('-m', '--mode', help = 'b for bruteforce or d for dictionary attack', required= False)
parser.add_argument('-i', '--input', help = 'Input password hash', required= False)
parser.add_argument('-h', '--hash', help = 'hash type, md5, sha256, or pt (for plaintext)', required= False)
args = parser.parse_args()
#dictionary attack--------------------------------
if args.mode=='d':
    print('starting dictionary attack...')
    #take in file from user and open
    filename = input('Enter dictionary file name:')
    with open(filename, 'r') as dictfile:
        #loop through it line by line
        for line in dictfile:
            #run da function to compare
            if dictionary_attack(line, args.input)==True:
                print('Matched!')
                break
            else:
                continue
        #otherwise
        print('Couldn\'t find match rip lol')

#brute force attack-------------------------------
elif args.mode=='b':
    print('starting brute force attack...')
    with open('passwords.txt','r') as passwords:
        print(passwords)

#default------------------------------------------
else:
    print('bruh')
    quit()

#functions----------------------------------------
def dictionary_attack(word, target):
    wordbytes= word.encode('utf-8')
    if(args.hash!= 'p'):
        wordhash = args.hash(wordbytes)
        digest = wordhash.hexdigest()
    if digest == target:
        return True