# PRINT ------------------------------------------------------
import pickle
print('hello world')
print('''hello
world''')

# INPUT ------------------------------------------------------
name = input()
word = raw_input("Enter the word ")

# FS ---------------------------------------------------------
'''
modes
r - read(by def)
w - write
a - append
r+ - read & write, pointer on beginning
w+ - read & write, new file created if not exists
a+ - append & read, pointer on the end
'''

# READ
f = open('poem.txt')  # reading mode by def
# whole as string
all_read = f.read()  # read(5) reads the first 5 chars of all
# whole as list of strings
all_read = f.readlines()
# by line
while True:
    line = f.readline()  # readline(5) reads the first 5 chars of line
    if len(line) == 0:  # 0 is a end of file (EOF)
        break
    print(line, end='')
f.close()

# WRITE
poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
используй Python!
'''
f = open('poem.txt', 'w')  # use 'a' for append
f.write(poem)  # write all as string to file
f.writelines(poem)  # write list of strings
f.close()

# PICKLING/UNPICKLING
'''
The pickle module is used to store complex data such as list
and dictionary. There is cPickle - faster c version of pickle
'''


name = ["mohit", "bhaskar", "manish"]
skill = ["Python", "Python", "Java"]
pickle_file = open("emp1.dat", "w")
pickle.dump(name, pickle_file)
pickle.dump(skill, pickle_file)
pickle_file.close()

pickle_file = open("emp1.dat", 'r')
name_list = pickle.load(pickle_file)
skill_list = pickle.load(pickle_file)
