import argparse
import hashlib
#from itertools import combinations_with_replacement or permutations
import random
import itertools
import string

#run with 'python3 crack.py' + extension ez dub im cracked at pyhton
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
        #WHY IT NOT WORKR ITS LITERLAYL THE SMA EHTING kms
        wordbytes= word.encode('utf-8')#remove utf-8? #print hash
        wordhash = hashlib.sha256(wordbytes)
        word = wordhash.hexdigest()
        #idek atp
    elif(hashtype=='md5'): #she works i lov her mwah <33333
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
        filename = 'passwords.txt' #yum
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
        #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

#brute force attack-------------------------------
elif args.mode=='b':
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '@' + '#' + '$' + '.' 
    #LIST :)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    #irdlfjkks
    length = len(args.input)
    attempt = ""
    # if its not the ANSWER
    while(attempt!= args.input):
        #iterate through chars
        for guess in itertools.product(chars,repeat=length): 
            #make ur guess
            attempt = ''.join(guess)
            #CHECK eet
            #HASH BROWN.maybe
            print("checking: %s" %(attempt))
            if(attempt==args.input):
                #PRINT AND LEAVE!!!!!!!!!!!!!!!
                print("Matched! %s" %(attempt))
                break
#default------------------------------------------
else:
    #mission aboot
    print('bruh')
    quit()
