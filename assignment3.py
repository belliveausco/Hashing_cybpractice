import hashlib
count = 0
def sortList():
    for i in range(21):
        file_path = input("Enter the file path: ")
        BLOCK_SIZE = 10276
        hash_handler = hashlib.sha3_512()
        with open(file_path, 'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while fb:
                hash_handler.update(fb)
                fb = f.read(BLOCK_SIZE)
        file_hexhash = hash_handler.hexdigest()
        print(f"{file_path} file hash value: \n{file_hexhash}")
        a = open("hash.txt", "a+")
        a.write(f"{file_hexhash}""\n")
    print(a.readline(21))
    a.close()
def writeList():
    for j in range(21):
        b = open("hash.txt")
        print(str(b.readline(1)))
        if str(b.readline(1)) == str(b.readline(j)):
            count = count+1
            b.write(str(count))
        else:
            print("No match!")
    b.close()
sortList()
writeList()
