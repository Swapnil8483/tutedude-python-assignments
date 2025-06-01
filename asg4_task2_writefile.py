#Write and append in file Output.txt
#1sr write in file
wrt = input("Type here, what you want to write to the file:")
try:
    with open(r"C:\Users\swapn\OneDrive\Desktop\python_Programs\output.txt", "w") as wrt_file:
        wrt = wrt_file.write(f"{wrt}")
        print("Data successfully written to output.txt")
except FileNotFoundError:
    print("File not found, check your file name or path")

#2nd append to the same file
wrt = input("Type here, what you want to add to the file:")
try:
    with open(r"C:\Users\swapn\OneDrive\Desktop\python_Programs\output.txt", "a") as apnd_file:
        apnd = apnd_file.write(f"\n{wrt}")
        print("Data successfully appended to output.txt")
except FileNotFoundError:
    print("File not found, check your file name or path")

#Finally read all data.
print("Final content of output.txt:")
try:
    with open(r"C:\Users\swapn\OneDrive\Desktop\python_Programs\output.txt", "r") as rd_file:
        rd = rd_file.read()
        if rd:
            print(rd)
        else:
            print("File is empty")
except FileNotFoundError:
    print("File not found, check your file name or path")