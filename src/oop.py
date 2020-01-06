# BLUEPRINT -------------------------------------------------
'''
self
all public by def(make private by starting with __),
methods are virtual
The static method(via decorator @staticmethod) doesn't take an instance or
class as the first argument. They are just simple functions - but we include
them in class because they have some logical connection with the class.
'''


class Fish():
	__amount = 45  # private

	# constructor
    def __init__(self, name):
		self.name = name

	# print instance directly
    def __str__(self):
		return f"Fish {self.name} with id {self.id}"
	
	# delete
    def __del__(self):
        print('{0} is dead!'.format(self.name))

	# static
	@staticmethod
	def check_amt(amt):
		if amt < 50000:
			return True
		else:
    		return False

    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")
        print(self.check_amt(self.name))


'''
INHERITANCE
- Multiple inheritance is available.
- Overriding parent methods works explicitly.
- Built-in func super() call the rest of the parent method in case of
overriding. The func is most commonly used within the __init__() method
because that is where you will most likely need to add some uniqueness
to the child class and then complete initialization from the parent.
After overridden the constructor method, we no longer can to pass
first_name in as a parameter, so therefore initialize the first_name
by calling the variable in our object instance.
'''


class Shark(Fish):
	pass


class CoralReef(Coral, Anemone):
	pass


class Trout(Fish):
	def __init__(self, water="freshwater"):
		self.water = water
		super().__init__(self)
	pass


# INSTANCE --------------------------------------------------
def main():
	fish = Fish("Fishy")
    sammy = Shark("Sammy")
	print(fish)
    fish.swim()  # Fishy is swimming.
    sammy.be_awesome()  # Sammy is being awesome.


if __name__ == "__main__":
    main()

