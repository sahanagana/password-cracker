import argparse
import hashlib
#from itertools import combinations_with_replacement or permutations
import itertools

#run with 'python3 crack.py' + extension
#arguments
parser = argparse.ArgumentParser(description='python password cracker')
parser.add_argument('-m', '--mode', help = 'b for bruteforce or d for dictionary attack', required= False)
parser.add_argument('-i', '--input', help = 'Input password hash', required= True)
parser.add_argument('-h', '--hash', help = 'hash type, md5, sha256, pt (for plaintext), or bc(for bcrypt)', required= False)
args = parser.parse_args()
#dictionary attack--------------------------------
if args.mode=='d':
    print('starting dictionary attack...')
    #take in file from user and open
    filename = input('Enter dictionary file name (don\'t put anything if you want to use the top 10000 passwords):')
    #if the user put nothing, just use the passwords file
    if len(filename)== 0:
        filename = passwords.txt
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
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0','1','2','3','4','5','6','7','8','9']
    print('starting brute force attack...')
    #use itertools to create combinations of letters and numbers?
    #print(list(combinations_with_replacement([1, 2], 2)))
    #print (list(permutations([1, 'geeks'], 2)))

#default------------------------------------------
else:
    print('bruh')
    quit()

#functions----------------------------------------
def dictionary_attack(word, target):
    #if needed, hash it
    hashtype = args.hash
    if(hashtype!= 'pt' or hashtype!='bc'):
        wordbytes= word.encode('utf-8')
        wordhash = hashlib.hashtype(wordbytes)
        word = wordhash.hexdigest()
    elif(hashtype=='bc'):
        wordbytes= word.encode('utf-8')
        wordhash = bcrypt.hash(wordbytes)
        word = wordhash.hexdigest()
    if word == target:
        return True
    return False
