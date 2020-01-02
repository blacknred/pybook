# PRINT
import pickle
print('hello world')
print('''hello
world''')

# READ/WRITE
poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
используй Python!
'''
f = open('poem.txt', 'w')
f.write(poem)  # write buffer to file
f.close()

f = open('poem.txt')  # reading mode by def
while True:
    line = f.readline()
    if len(line) == 0:  # 0 is a end of file (EOF)
        break
    print(line, end='')
f.close()
