file_name = 'files/test1.txt'
file_name = r'files\test1.txt'
file_name = 'files\\test1.txt' # three ways to describe a file

#open the file step by step
file_obj = open(file_name)
print(file_obj)
content = file_obj.read();
print(content)
file_obj.close()

file_name = 'files/test1.txt'

# open the file in a whole
try:
     with open(file_name, encoding='utf-8') as file_obj: # set encoding as utf-8 to read a chinese file
       print(file_obj.read())
    # auto close
except FileNotFoundError as fe:
    print(fe)

# read a file with a size
try:
     with open(file_name, encoding='utf-8') as file_obj:
       file_content = ''
       while True:
           content = file_obj.read(2)  # read 2 chars each time, each Chinese word is a char
           if not content:
             break
           print(content, end='') # remove \n
           file_content+= content
       print(file_content)
    # auto close
except FileNotFoundError as fe:
    print(fe)

# readline() can read one line each time
# readlines() will read all content and push each line into a list

file_name = 'files/test3.txt'

# write
with open(file_name, 'w') as file_obj:
    file_obj.write('test \n')
    file_obj.write('test \n')

# append
with open(file_name, 'a') as file_obj:
    file_obj.write('test \n')
    file_obj.write('test \n')

# r+ : read and write. If file does not exist, error
# w+ : read and write. If file does not exist, create
# a+ : read and append. If file does not exist, create


# read a bianry file and write into another. The file has two types: text and binary
file_name = 'files/1.jpg'
with open(file_name, 'rb') as file_obj:
    new_file_name = 'files/img/1.jpg'
    with open(new_file_name,'wb') as new_file_obj:
        size =  1024 * 100
        while True:
            content = file_obj.read(size)
            if not content:
                break
            new_file_obj.write(content)

# file_obj.tell()  get the current binary position of reading
# file_obj.seek(pos,from) from can be 0 (from start), 1 (from current), 2(from end)
# one Chinese word represents 3 byte



# OS file operation
import os
from pprint import pprint

dir_list = os.listdir('files') # get all files and dirs under a path in a list
pprint(dir_list)

pprint(os.getcwd()) # get the current path

# os.chdir()
os.mkdir('files/static')
os.rmdir('files/static')
open('files/test4.txt','w')
os.remove('files/test4.txt')
# os.rename(old_name, new_name) if name contains path, it can move files