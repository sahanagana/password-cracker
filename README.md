# password-cracker
Python Password Cracker
 - [x] Dictionary Attack option 
 - [x] Bruteforce Attack option
 - [x] Command line arguments can be taken in
 - [x] Top 10,000 most common passwords can be cracked 
    - [x] Plain-text passwords can be checked 
    - [x] MD5 hashed passwords can be checked 
    - [x] SHA-256 hashed passwords can be checked 



## usage

### arguments
-m : mode, b for bruteforce or d for dictionary attack
-i : input password, if hashed, you must use -h to indicate the type of hash
-t : hash type, md5, sha256, pt(plaintext)


### examples
python3 crack.py -m d -i 5f4dcc3b5aa765d61d8327deb882cf99 -t md5
returns 'password'

python3 crack.py -m b -i abc -t pt
returns '['a','b','c']'

## notes
- Bruteforce only works with plaintext
- SHA256 doesn't work
