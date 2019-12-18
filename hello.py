# line comment
""" multiline
comment
"""

# Print
print('hello world')
print('''hello
world''')
print("Hey there it's a cow")
print('a')

# Division with Integers
a = 5 / 2
b = 5.0 / 2.0
c = 5 // 2
print(a) #2.5
print(b) #2.5
print(c) #2

# Loop
sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']
for shark in sharks:
    print(shark)

# Func
def calculate():
    print('done')
def again():
    # Take input from user
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')
    if calc_again == 'Y':
        calculate()
    elif calc_again == 'N':
        print('See you later.')
    # If user types another key, run the function again
    else:
        again()