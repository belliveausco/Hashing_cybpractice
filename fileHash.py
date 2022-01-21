import hashlib
list = ["f0.docx", "f1.docx", "f2.docx", "f3.docx", "f4.docx", "f5.docx", "f6.docx", "f7.docx", "f8.docx", "f9.docx", "f10.docx", "f11.docx", "f12.docx", "f13.docx", "f14.docx", "f15.docx", "f16.docx", "f17.docx", "f18.docx", "f19.docx", "f20.docx"]
# list is an array comprised of the files we are hashing, which makes it easier
# so that the user does not need to re enter multiple file paths
hash_list = []
# initializes array for hash values
for i in range(21):
# for loop designed to run through 21 times to equal 21 files we are hashing
    file_path = list[i]
# filepath will run through each element i times which is 21, 21 = files being hashed
    BLOCK_SIZE = 128
# designates size of block storage for each file being hashed
    hash_handler = hashlib.sha3_512()
#creates hash object
    with open(file_path, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while fb:
            hash_handler.update(fb)
# update using hash function
            fb = f.read(BLOCK_SIZE)
    file_hexhash = hash_handler.hexdigest()
#sets hash value to variable
    hash_list.append(f"{file_hexhash}""\n")
#adds hash value to array hash_list
    a = open("hash.txt", "a+")
#creates hash.txt file if one does not exist it will create one
    a.write(f"{file_hexhash}""\n")
#adds hashvalue to hash.txt file
    print(f"{file_path} file hash value: \n{file_hexhash}")
#displays hash value to user
    x = hash_list[0]
# x is equal to the hash value of f0.docx, which is the first item in the array at index 0
    def counttimes(hash_list, x):
        count = 0
#intializes count to 0
        for hashvalue in hash_list:
#for any element found in hash_list
            if (hashvalue == x):
#compares element to x which is hash value of f0.docx
                count = count + 1
#if statement is true will increment count by 1
        a.write("Identical copies of f0 among f1-f20 are ")
#writes print statement to hash.txt
        a.write(str(count))
#writes value of count after end of loop
        return count
counttimes(hash_list, x)
