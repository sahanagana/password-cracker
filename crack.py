import argparse
#run with 'python3 crack.py' + extension
#arguments
parser = argparse.ArgumentParser(description='python password cracker')
parser.add_argument('-m', 'mode', help = 'b for bruteforce or d for dictionary attack', required= False)
parser.add_argument('-i', '--input', help = 'Input password hash', required= False)
parser.add_argument('-h', '--hash', help = 'hash type, md5, sha256, or pt (for plaintext)', required= False)
args = parser.parse_args()
#dictionary attack--------------------------------
if (args.mode=='d'):
    print('starting dictionary attack...')

#brute force attack-------------------------------
elif (args.mode=='b'):
    print('starting brute force attack...')

#default------------------------------------------
print('bruh')
quit()