import hashlib
import sys
import sha3

#define the buffer size - how much of a file is read into memory at a time, allows for larger file sizes
BUF_SIZE = 65536

#declaring our hashing algorithms
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()
sha512 = hashlib.sha512()
sha3 = hashlib.sha3_512()

#opens the command line argument as a file
with open(sys.argv[1], 'rb') as file:
    while True:
        #reads the contents of the file to the size of the buffer at a time
        data = file.read(BUF_SIZE)
        #breaks out of the loop if there's no data
        if not data:
            break
        #gets hash of the file
        sha1.update(data)
        sha256.update(data)
        sha512.update(data)
        sha3.update(data)

#prints out the has of the file
print("SHA1: {0}".format(sha1.hexdigest()))
print("SHA-256: {0}".format(sha256.hexdigest()))
print("SHA-512: {0}".format(sha512.hexdigest()))
print("SHA3: {0}".format(sha3.hexdigest()))