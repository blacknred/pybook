# VARIABLES ------------------------------------------------------
# can be reassign, global and local(function scope)
x = y = z = 0  # multiple assignment
j, k, l = "shark", 2.05, 15
type(x)  # type
None  # emptiness
id(x)  # memoty location(check identity etc)


# CONDITIONS ------------------------------------------------------
if grade >= 90:
    print("A grade")
elif grade >= 80:
    print("B grade")
else:
    print("Failing grade")


# LOOPS -----------------------------------------------------------
while True:
    pass

for i in range(0, 5):
    print(i)

range(start, stop, step)  # generate a list on-the-fly.
xrange(start, stop, step)  # the same, but frees the memory after
continue
break
'''
The pass statement tells the program to disregard that
condition and continue to run the program as usual.
The pass statement can create minimal classes, or act as a placeholder
when working on new code and thinking on an algorithmic level before
hammering out details.
'''
pass


# FUNCTIONS --------------------------------------------------------
'''
Pass by reference, except reassignment in the body case
TypeError, if dont pass any argument to the function with param
allow default params, *variable length params
'''


def profile_info(username, followers=2, *rest):
    print("Username: " + username)
    print("Followers: " + str(followers))
    for var in rest:
        print(var)


# **kwargs(pass a keyworded, variable-length args dictionary)
def print_values(**kwargs):
    for key, val in kwargs.items():
        print("The value of {} is {}".format(key, val))


# lambda
def defaultdict(arg):
    return arg


def func():
    return "Cricket"


game = defaultdict(func)
game = defaultdict(lambda: "Cricket")


# common call
profile_info("sammyshark", 945, 'klk', 89)
# keyword arguments(any order we pass args) call
profile_info(followers=820, username="cameron-catfish")  # keyword arguments
# *args and **kwargs calls


def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)


def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1:", kwarg_1)


args = ("Sammy", "Casey", "Alex")
kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
some_args(*args)
some_kwargs(**kwargs)


# EXCEPTIONS -----------------------------------------------------
def divide1():
    try:
        num = int(raw_input("Enter the number "))
        c = 45/num
        print(c)
    except Exception as e:
        print(e), type(e)
    else:
        print("result is ", c)
    finally:
        print("finally program ends")


divide1()


# User-defined exceptions
class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (self.value)


try:
    num = raw_input("Enter the number : ")
    if num == '2':
        raise MyException("ohh")
    else:
        print("number is not 2")
except MyException as e:
    print("My exception occurred")
