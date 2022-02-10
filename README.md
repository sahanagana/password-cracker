# password-cracker
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


 - [x] Top 10,000 most common passwords can be cracked 
    - [x] Plain-text passwords can be checked 
    - [x] MD5 hashed passwords can be checked 
    - [x] BCrypt hashed passwords can be checked 
    - [x] SHA-256 hashed passwords can be checked 
    
 - [ ]Brute force approach option
 - [x]Dictionary Attack option 
 - [x]Command line arguments can be taken in


## usage

### arguments
-m : mode, b for bruteforce or d for dictionary attack
-i : input password, if hashed, you must use -h to indicate the type of hash
-h : hash type, md5, sha256, pt(plaintext) or bc(bcrypt)
