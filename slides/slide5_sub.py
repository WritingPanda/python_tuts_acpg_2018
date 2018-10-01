# This is a string
sample_string = "Hello python group!"
if isinstance(sample_string, str):
    print("Yep, this is a string!")
else:
    print("No, this is not a string.")

# This is a boolean
sample_bool = True
if isinstance(sample_bool, bool):
    print("That's a boolean!")
else:
    print("Nope.")

# This is an integer
sample_integer = 2018
if isinstance(sample_integer, int):
    print("Totally an integer.")
else:
    print("No, this is not an integer.")

# This is a float
sample_float = 20.18
if isinstance(sample_float, float):
    print("It's a float!")
else:
    print("Nope, not a float.")

# This is a complex number
sample_complex = 20+18j
if isinstance(sample_complex, complex):
    print("Oof, that's weird. Not something that is commonly used unless you're a scientist.")
else:
    print("It's simpler than I thought.")

# List
sample_list = [1, 2, 3]
sample_list.append(4)
print(sample_list)
if isinstance(sample_list, list):
    print("That's a list, all right.")
else:
    print("Sorry, breh. That's no list.")

# Dictionary
sample_dict = {
    "key": "value",
    "id": 1,
    "is_json": False,
}
print(sample_dict["key"])
if isinstance(sample_dict, dict):
    print("Nice dict.")
else:
    print("That ain't a dict I ever seen.")

# Tuples
# https://www.programiz.com/python-programming/methods/tuple
sample_tuple = ("red", "blue", "green",)

def update_tuple(the_tuple, appending_value):
    try:
        the_tuple.append(appending_value)
    except Exception as e:
        print(f"You can't do that. Here's why: {e}")
    return the_tuple

print(update_tuple(sample_tuple, "purple"))

if isinstance(sample_tuple, tuple):
    print("Tuples can't change.")
else:
    print("If this changed, then it's not a tuple.")

# while loop
x = 1
while x <= 15:
    print(x)
    x = x + 1
    if x == 7:
        print("Halfway there!")
        continue
    if x == 14:
        print("Let's stop here instead.")
        break

# for loop
for x in range(0, 15):
    print(x)
    x = x + 1
    if x == 7:
        print("You get the point.")
        break

# functions
def my_func(parameter: str, default="value"):
    # reversing strings
    # [begin:end:step]
    reverse = parameter[::-1]
    reverse_default = default[::-1]
    return reverse, reverse_default

print(my_func("hello, python group!"))

# classes
class Person():
    def __init__(self, firstname, lastname, height):
        self.firstname = firstname
        self.lastname = lastname
        self.height = height

    def is_taller_than_omar(self):
        omar_height_in_cm = 181
        if self.height > omar_height_in_cm:
            return True
        else:
            return False

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    def get_firstname(self):
        return self.firstname
    
    def get_lastname(self):
        return self.lastname

    def _private_function(self):
        return f"It's not really private, but the underscore helps us know that the developer wants it to be private."
    
new_person = Person("Doug", "Mendizzie", 179)
print(new_person.get_fullname())
print(new_person._private_function())
print(new_person.__dir__())
print("\n")
print(new_person.__dict__)
