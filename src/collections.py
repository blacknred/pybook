'''
each collection has unique characteristic and
can be used to achieve the desired outcome.
All the collections are part of the collections module.
Container is a generic word, means anything that can hold anything.
'''
import collections

# COUNTER ----------------------------------------------------
'''
Counter is a container and it tracks the frequency of values
workds with iterable types: string, list, tuple
'''
counter = collections.Counter("La La Land")  # ({' ': 2, 'a': 3, ...})
counter.update("Locarno Caine")

# sort by most_common
co = collections.Counter()
file_txt = open("Counter_input.txt", "r")
for line in file_txt:
    co.update(line.lower())
print("Most common:n")
for letter, count in co.most_common(5):
    print('%s: %7d' % (letter, count))

# operations: addition, subtraction, union and intersection
co1 = collections.Counter(['C', 'L', 'E', 'O', 'P', 'A', 'T', 'R', 'A'])
co2 = collections.Counter('JULIUS CAESAR')
print("addition n", co1 + co2)  # Prints addition of sets
print("Subtractionn", co1 - co2)  # Prints substration of sets
print("Union n", co1 | co2)  # Prints union of sets
print("Intersection n", co1 & co2)  # Prints intersection of sets


# DEQUE ----------------------------------------------------------
'''
A Deque double-ended queue. It can be visualized similar to a pipe, which is
open at the both ends. Allows addition and removal of els from either ends.
'''
d1 = collections.deque("Google")
print(d1)  # ['G', 'o', 'o', 'g', 'l', 'e']
d1.extend('raj')  # ['G', 'o', 'o', 'g', 'l', 'e', 'r', 'a', 'j']
d1.append('hi')  # ['G', 'o', 'o', 'g', 'l', 'e', 'hi']
d1.extendleft("de")
d1.appendleft("le")
d1.pop()
d1.popleft()
d.rotate(2)  # ['l', 'e', 'G', 'o', 'o', 'g']
d1.rotate(-2)  # ['o', 'g', 'l', 'e', 'G', 'o']


# ORDERED DICTIONARY --------------------------------------------
'''
The OrderedDict is a subclass of the dictionary and it remembers the order
in which the els are added(iterates orderly against regular arbitrary dict)
'''
d1 = collections.OrderedDict()


# DEFAULT DICTIONARY --------------------------------------------
'''
Provides a default value for a nonexistent key with a callable function
'''
game = defaultdict(lambda: "Cricket")
game1 = defaultdict(int)  # default int value is 0
game["A"] = "Football"
game["B"] = "Badminton"
print(game["C"])  # Cricket
print(game["C"])  # 0

# NAMED TUPLE ---------------------------------------------------
'''
namedtuple gives you a special feature to create your own data type.
namedtuple(typename, field_names[, verbose=False][,rename=False])
immutable like tuple
'''
employee = collections.namedtuple('emp', 'name, age, empid')
record1 = employee("Hamilton", 28, 12365)
print("Record is ", record1)  # emp<name='Hamilton',age=28,empid=12365>
print("name of employee is ", record1.name)  # Hamilton
print("type is ", type(record1))  # <class `__main__.emp`>
#
list1 = ['BOB', 21, 34567]
record2 = employee._make(list1)  # create from list
record3 = record2._asdict()  # convert to dict
record1 = record1._replace(age=25)  # immutable, but can be replaced
