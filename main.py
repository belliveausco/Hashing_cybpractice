import hashlib
print(hashlib.algorithms_guaranteed)
#if pycharm available, homework working on hash component
#h = hashlib.sha3_256() #function to call to create hash object
#h.update(b‘ABCED’) #provide input and convert to b(byte) object one sequence of byte data (in this doing this to a string) h.update takes input and converts it to the hash object
#h_digest = h.digest() #provide the hash value based on update function
#h_hexDigest = h.hexdigest() #returns everything in hex convert from byte to hex
#h_digestSize = h.digest_size #to get size of hash value
#print(f’h hash value: {h_digest}’) #prints out hash value
#print(f’h hash hex value: {h_hexDigest}’)
#print(f’h hash value size: {h_digestSize}’) #prints hash value size
#h.update(b’abcde’)
#h_hexDigest = h.hexdigest()
#print(f’h hash hex value: {h_hexDigest}’)
h = hashlib.sha3_256() #creates hash object
#update using hash function
h.update(b'ABCDE')
h_hexDigest = h.hexdigest()
print(f'h hash value is: {h_hexDigest}')
#m1='ABCDE'
#d1=H(m1)
#m2='abcde'
#d2=H(m1+m2) to add both use update
h.update(b'abcde')
h_hexDigest = h.hexdigest()
print(f'h hash value is: {h_hexDigest}')
h2 = hashlib.sha3_256() #creates hash object
#update using hash function
h2.update(b'ABCDEabcde')
h2_hexDigest = h2.hexdigest() #if you provide 3 different data it will accumulate data, 2 is both lowercase and so is 3
print(f'h2 hash value is: {h2_hexDigest}')
h2.update(b" ") #can verify if changed values will be different it will repeat same if no changes made
h2_hexDigest = h2.hexdigest()
print(f'h2 hash value is: {h2_hexDigest}')
#think of output how would we know if data was manipulated
#we would check to see is hash values are equal to each other
#if not data was changed