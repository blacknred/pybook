# VARIABLES -----------------------------------------------------------
# can be reassign
# multiple assignment
x = y = z = 0
j, k, l = "shark", 2.05, 15
# global and local(function scope)


# NUMBERS -------------------------------------------------------------
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
x ** y  # or
round(17.34989436516001, 4)  # round 17.3499
# count sum for lists, tuples, and dictionaries
sum({-10: 'x', -20: 'y', -30: 'z'})  # -60


# BOOLEANS -------------------------------------------------------------
my_bool = 5 > 8


# STRINGS --------------------------------------------------------------
# immutable
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
str(12)
str.upper()
str.lower()
str.isalnum()
str.isalpha()
str.islower()
str.isupper()
str.isnumeric()
str.isspace()  # only whitespaces
str.istitle()  # String Is in Title Case
" ".join(str)  # H e l l o ,  W o r l d !
",".join(["sharks", "crustaceans", "plankton"])
str.split()  # ['Hello', 'world']
str.replace('world', 'kitty')
len(str)  # 13
str.count('l')  # 3
str.find('o')  # 4 (first index)
str.find('o', 5)  # 8 (first after)
print("Sammy the {} has a pet {}!".format("shark", "pilot fish"))
print("Sammy ate {0:f} percent of a {1}!".format(75, "pizza"))
print("Sammy ate {0:.3f} percent of a pizza!".format(75.765367))


# COMPOUND DATA TYPES --------------------------------------------

# LISTS (mutable)
my_list = ['shark', 'cuttlefish', 'squid', 'mantis shrimp']
my_list[2] = 'anemone'
# slicing
my_list[1:4]
my_list[:4]
# concat
my_list + oceans
my_list + 'ocean'
my_list * 2  # multiple replication
del my_list[1]
del my_list[1:4]
my_list[1][0]  # nested lists
# methods
fish.append('flounder')
fish.insert(3, 'anchovy')
fish.extend(my_list)
fish.remove('kissing gourami')  # only remove the first instance
fish.pop(3)  # return the item
fish.index('herring')  # find index
fish.copy()
fish.reverse()
fish.count()
fish.count('goby')
fish.sort()
fish.clear()
# list comprehensions
# List comprehensions allow us to transform one list or other sequence
# into a new list. They provide a concise syntax for completing this
# task, limiting our lines of code
number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)  # [0, 4, 16, 36, 64]
number_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
print(number_list)  # [0, 15, 30, 45, 60, 75, 90]
number_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
print(number_list)  # [40, 80, 120, 80, 160, 240, 120, 240, 360]


# TUPLES (immutable)
my_tuple = ('blue coral', 'staghorn coral', 'pillar coral')


# DICTIONARIES (hold related data(key - value))
my_dictionary = {'name': 'Sammy', 'animal': 'shark', 'color': 'blue'}
# methods
tuple(my_list)  # from lists or strings because of iteration
list(my_tuple)  # from lists or strings because of iteration
