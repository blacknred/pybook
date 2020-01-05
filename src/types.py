# INTs, FLOATs --------------------------------------------------------------
my_int = 89
my_float = 9.8
# methods
float(57)
int(390.8)
abs()  # absolute value of a number from null
x // y  # floor division, returns a quotient
x % y  # modulo division, returns a remainder
# finding the quotient and remainder in one function
# here we'll have 266 pages filled with 300 words and 200 words left
divmod(80000, 300)  # (266, 200)
# raise numbers to a certain power
pow(2, 24)  # 16777216
x ** y  # exponentiation
round(17.34989436516001, 4)  # round 17.3499
# count sum for lists, tuples, and dictionaries
sum({-10: 'x', -20: 'y', -30: 'z'})  # -60


# BOOLEANS ------------------------------------------------------------------
my_bool = 5 > 8
is  # Returns True if two variables point to the same object and False
is not  # Returns False if two variables point to the same object and True


# STRINGS -------------------------------------------------------------------
# immutable, iterable, utf-8 by def
str = "Hello, World!"
str = '''
Hello
World
'''
print(str[1])  # e
print(str[-1])  # d
# slicing
print(str[3:5])  # llo
print(str[:5])  # Hello
print(str[5:])  # World
# concatenation
print("Sammy" + "Shark")
print("Sammy" + 27)  # error, no implicit convertion
print("Sammy" + "27")  # explicit convertion
# replication
print("Sammy" * 9)
# raw string(ignore all formatting)
print(r"Sammy says,\"The balloon\'s color is red.\"")
# methods
str(12)  # conversion
str.upper()
str.lower()
str.isalnum()
str.isalpha()
str.isdigit()
str.islower()
str.isupper()
str.isnumeric()
str.isspace()  # only whitespaces
str.istitle()  # String Is in Title Case
str.startswith('Swa')
str.endswith("ng")
" ".join(str)  # H e l l o ,  W o r l d !
",".join(["sharks", "crustaceans", "plankton"])
str.split()  # ['Hello', 'world']
str.split("-", 1)
str.rsplit("-", 1)
str.replace('world', 'kitty')
str[::-1]  # reverse
len(str)  # 13
min(str)  # the min char from string according to the ASCII
max(str)  # the max char from string according to the ASCII
str.count('l')  # 3
str.find('o')  # 4 (first index)
str.find('o', 5)  # 8 (first after)
if "be" in str:  # also find
print("Sammy the {} has a pet {}!".format("shark", "pilot fish"))
print("Sammy ate {0:f} percent of a {1}!".format(75, "pizza"))
print("Sammy ate {0:.3f} percent of a pizza!".format(75.765367))



# COMPOUND DATA TYPES -----------------------------------------------------------

# TUPLES (immutable(items can`t be added to or removed), iterable, faster than lists)
my_tuple = ('blue coral',)
my_tuple = 'ji', '88', 7
my_tuple = ('blue coral', 'staghorn coral', 25, 'i')
my_tuple[1] = 'staghorn coral'
a, b, c, d = my_tuple  # unpack
# methods
my_tuple[1:3]  # slicing
coral_kelp = (my_tuple + kelp)
multiplied_coral = my_tuple * 2
len(my_tuple)
max(my_tuple)
min(my_tuple)
tuple(my_list)  # from lists or strings because of iteration



# DICTIONARIES (mutable, related data(key - value), unordered(arbitrary
# unlike lists & tuples), keys are string, int, float, or tuple that
# does not contain any list)
my_dictionary = {'name': 'Sammy', 'animal': 'shark', 'color': 'blue'}
my_dictionary['name']
my_dictionary['name'] = 'Jamie'
del my_dictionary['name']
# methods
dict(my_tuple or my_list)  # tuple or list that contain elements as pairs of two values
len(my_dictionary)
str(my_dictionary)
max(my_dictionary)  # by keys
min(my_dictionary)  # by keys
my_dictionary.copy()
my_dictionary.clear()
my_dictionary.update({'followers': 481})
# keys
sammy.keys()  # dict_keys(['followers', 'username', 'online'])
for common_key in sammy.keys() & jesse.keys():
    print(sammy[common_key], jesse[common_key])
# values
sammy.values()  # dict_values([True, 'sammy-shark', 987])
# all items
sammy.items()  # dict_items([('online', True), ...])
for key, val in sammy.items():
    print(key, 'is the key for the value', val)



# LISTS (mutable, iterable)
my_list = ['shark', 'cuttlefish', 'squid']
my_list[2] = 'anemone'
a, b = [1, 2]  # unpack
del my_list[1]
del my_list[1:4]
my_list * 2  # multiple replication
my_list[1][0]  # nested lists
# slicing
my_list[1:4]
my_list[:4]
# concat
my_list + oceans
my_list + 'ocean'
# methods
len(my_list)
max(my_list)
min(my_list)
list('uiu', 'po')
list(my_tuple)  # from lists or strings because of iteration
sorted(my_list)  # returns a new list, args: key=None, reverse=False
my_list.append(my_list)  # ['shark', 'cuttlefish', 'squid', ['shark' ..]]
my_list.extend('flounder')  # ['shark', 'cuttlefish', 'squid', 'flounder']
my_list.insert(3, 'anchovy')
my_list.remove('kissing gourami')  # only remove the first occurrence
my_list.pop()  # return the last item
my_list.pop(3)  # return the item
my_list.index('herring')  # find index
my_list.copy()
my_list.reverse()
my_list.count()
my_list.count('goby')
my_list.clear()
# sort (possible args: cmp=None, key=None, reverse=False)
my_list.sort()
# reverse
my_list.sort(reverse=True)
# key
list_tup = [("a", 4), ("b", 1), ("v", 5), ("f", 2)]
list_tup.sort(key=lambda x: x[1])  # [("b", 1), ("f", 2), ("a", 4), ("v", 5)]
# cmp(complex)
list1 = [10, 9, 3, 7, 2, 1, 23, 1, 561, 1, 1, 96, 1]
def cmp1(x, y):
    if x == 1 or y == 1:
        c = y-x
    else:
        c = x-y
    return c
list1.sort(cmp=cmp1)  # [2,3,7,9,10,23,96,561,1,1,1,1,1]
'''
list comprehensions
allow us to transform one list or other sequence into a new list.
Provide a concise syntax, limiting our lines of code
'''
number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)  # [0, 4, 16, 36, 64]
number_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
print(number_list)  # [0, 15, 30, 45, 60, 75, 90]
number_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
print(number_list)  # [40, 80, 120, 80, 160, 240, 120, 240, 360]
'''
build-in iteration functions
'''

def square(number):
    return number*number


def even(number):
    if (number % 2) == 0:
        return True
    return False


numbers = [1, 2, 3, 4, 5]
squared_numbers = []
even_numbers = []

# map
for number in numbers:
    squared = square(number)
    squared_numbers.append(squared)
squared_numbers = list(map(lambda number: number*number, numbers))
# filter
for number in numbers:
    if even(number):
        even_numbers.append(number)
even_numbers = filter(even, numbers)
# zip (combine values with matching indexes from multiple lists into tuple)
even_numbers = [2, 4]
even_numbers_squared = [4, 8]
combined = []
even_numbers_index = 0
for number in even_numbers:
    squared = even_numbers_squared[even_numbers_index]
    squared_tuple = (number, squared)
    combined.append(squared_tuple)

combined = tuple(zip(even_numbers, even_numbers_squared))