#xx1-read-file.py

# no imports required

# use built-in Python function to open file for reading
f = open("test.txt", "r")

# read file contents
text1 = f.read()

# operating systems limit the number of open files
# it is necessary to close all open files
f.close()

# output the file contents
print(text1)

# to be sure file be closed after reading, 'try-finally' construction can be used
try:
    f = open("test.txt", "r")
    text2 = f.read()
finally:
    f.close()

# output the file contents
print(text2)

# language construction 'with' will close file automatically after usage
with open("test.txt", "r") as f:
    text3 = f.read()

print(text3)
