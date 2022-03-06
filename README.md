# password-cracker
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


 - [x] Top 10,000 most common passwords can be cracked 
    - [x] Plain-text passwords can be checked 
    - [x] MD5 hashed passwords can be checked 
    - [x] SHA-256 hashed passwords can be checked 
 - [x]Dictionary Attack option 
 - [x]Command line arguments can be taken in


## usage

### arguments
-m : mode, b for bruteforce or d for dictionary attack
-i : input password, if hashed, you must use -h to indicate the type of hash
-t : hash type, md5, sha256, pt(plaintext)


### example
python3 crack.py -m d -i 5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8 -t sha256
returns 'password'
