# file basics

# """
# "r" - open file for reading
# "w" - open a file for weiting
# "x" - creation file if not exists
# "a" - Add more content to a file
# "b" - binary mode 
# "+" - read and write


f = open("23_read.txt","r")
content = f.read()
print(content)

f.close()



