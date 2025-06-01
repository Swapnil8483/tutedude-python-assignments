#Read file and handle error
#methode 1
from certifi import contents

try:
    smpl_file = open(r"C:\Users\swapn\OneDrive\Desktop\python_Programs\sample.txt", "r")
    file_rd = smpl_file.read()
    print(file_rd)
    smpl_file.close()
except FileNotFoundError:
    print("File not found, check your file name or path")

#method 2

try:
    with open (r"C:\Users\swapn\OneDrive\Desktop\python_Programs\sample.txt", "r") as smpl_file:
        file_rd = smpl_file.read()
        if file_rd:
            print(file_rd)
        else:
            print("File is empty")
except FileNotFoundError:
    print("File not found, check your file name or path")