# VARIABLES -----------------------------------------------------------
# can be reassign
# global and local(function scope)
# multiple assignment
x = y = z = 0
j, k, l = "shark", 2.05, 15


# CONDITIONS --------------------------------------------
if grade >= 90:
    print("A grade")
elif grade >= 80:
    print("B grade")
else:
    print("Failing grade")


# LOOPS ------------------------------------------------
while

for i in range(0, 5):
    print(i)

continue
break
pass
```The pass statement tells the program to disregard that
condition and continue to run the program as usual.
The pass statement can create minimal classes, or act as a placeholder
when working on new code and thinking on an algorithmic level before
hammering out details.
```


# FUNCTIONS --------------------------------------------
# bodies
# allow default args
def profile_info(username, followers=2):
    print("Username: " + username)
    print("Followers: " + str(followers))

# *args(pass a variable-length args)
def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

# **kwargs(pass a keyworded, variable-length args dictionary)
def print_values(**kwargs):
    for key, val in kwargs.items():
        print("The value of {} is {}".format(key, val))

# explicit positional params along with *args and **kwargs
def example(arg_1, arg_2, *args, **kwargs):

# calls
# keyword arguments allow dont bother in which order we pass args
profile_info("sammyshark", 945)  # common
profile_info(followers=820, username="cameron-catfish")  # keyword arguments
print_values(my_name="Sammy", your_name="Casey")  # **kwards call

# *args and **kwargs calls
def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)

def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1:", kwarg_1)

args = ("Sammy", "Casey", "Alex")
kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
some_args(*args)
some_kwargs(**kwargs)
