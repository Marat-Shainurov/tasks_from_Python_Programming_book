# Create a class with 2 arguments as attributes, one method returning their values.
class FirstClass:

    def __init__(self, val_1, val_2):
        self.val_1 = val_1
        self.val_2 = val_2

    def show(self):
        return self.val_1, self.val_2


# Create a class, with a constructor method, that takes 2 arguments and then creates an attribute
# depending on the arguments types. If they are both integers it creates one attribute as their sum.
# If they are both strings it creates one attribute as their concatenated literal. Otherwise, it doesn't
# create any attributes.
class SecondClass:

    def __init__(self, user_literal=None, user_int=None):
        if isinstance(user_literal, str) and isinstance(user_int, str):
            self.user_attribute = user_literal + " " + user_int
        elif isinstance(user_literal, int) and isinstance(user_int, int):
            self.user_attribute = user_literal + user_int
        else:
            self.user_attribute = None

    def show_2(self):
        if self.user_attribute is not None:
            return self.user_attribute
        else:
            return "This class doesn't contain any attributes!"


# Create a class that takes a list as the argument, then creates an attribute compiled of the odd numbers
# from the user's argument. It should have 2 methods - the first should return the attribute's value,
# the second - calculate the average.
class ThirdClass:

    def __init__(self, user_list):
        self.user_data = []
        for element in user_list:
            if element % 2 != 0:
                self.user_data.append(element)

    def show_3(self):
        return self.user_data

    def average(self):
        return sum(self.user_data) / len(self.user_data)


# Create a function that takes 2 arguments - a list and a string. Then it creates a class named as the string.
# The literal elements of the list define the class attributes (non-literal elements are ignored).
# The values of the attributes are integers (elements indexes).
def create_objects(user_list, user_string):

    class MyClass:

        def __init__(self):
            for element in range(len(user_list)):
                if isinstance(user_list[element], str):
                    name = user_list[element]
                    self.__dict__[name] = element

        def show_4(self):
            return self.__dict__

        def show_4_class_name(self):
            return MyClass.__name__

    MyClass.__name__ = user_string
    return MyClass()


# Create a function that takes a class object, then returns another object, but with fields with integer values only.
def create_new_obj(user_object):

    new_object = user_object
    for k, v in new_object.__dict__.copy().items():
        if type(v) != int:
            new_object.__dict__.pop(k)

    return new_object


# Create a function that takes a number and a class name as the arguments, then creates a list of
# number-times class objects, with one attribute (a list of odd numbers).
def obj_generator(user_number, class_name):

    res = []
    for n in range(user_number):
        obj_per_cycle = class_name()
        obj_per_cycle.__dict__["value"] = [x*2+1 for x in range(3)]

        res.append(obj_per_cycle)

    return res


# Create a function that takes 2 objects of the same class, with one fields, a list of numbers. Then it returns another
# class object, with a list as its attribute, made up as the sum of pairs the argument objects' lists elements.
def create_obj_sum(obj_1, obj_2):

    obj_3 = obj_1
    a = obj_1.__dict__["value"]
    b = obj_2.__dict__["value"]
    obj_3.__dict__["value"] = []

    for x, y in zip(a + [0]*(len(b)-len(a) if len(a)<len(b) else 0), b + [0]*(len(a)-len(b) if len(b)<len(a) else 0)):
        obj_3.__dict__["value"].append(x+y)
    return obj_3


# Create a function, that generates a chain of the class objects, which takes a number as the argument, defining
# the number of objects. The function returns the first object in the chain (the last numerated).
def create_objects_chain(num):

    class ForEighth:

        def __init__(self, val=num):
            if val == 1:
                self.next = None
            else:
                self.next = ForEighth(val-1)
            self.numerate_objects()

        def numerate_objects(self, n=1):
            self.code = n
            if self.next is not None:
                self.next.numerate_objects(n+1)

        def show_chain(self):
            print(self.code)
            if self.next is not None:
                self.next.show_chain()

    objects = ForEighth()

    return objects.next.next.next.next


# Create a class, with a method that allows to insert an object inside existing chain of the objects, and another
# method that allows to delete an object in a way that remained objects formed a chain.
class ForNinth:

    def __init__(self, num=1):
        self.num = num
        if self.num == 1:
            self.next = None
        else:
            self.next = ForNinth(self.num-1)

    def insert_object(self, new_object):
        prev_obj = self
        while prev_obj.next and prev_obj.next.num < new_object.num:
            prev_obj = prev_obj.next
        new_object.next = prev_obj.next
        prev_obj.next = new_object
        return self

    def del_object(self, num):
        if self.num == num:
            return self.next
        prev_obj = self
        while prev_obj.next and prev_obj.next.num != num:
            prev_obj = prev_obj.next
        if prev_obj.next and prev_obj.next.num == num:
            prev_obj.next = prev_obj.next.next
        return self

    def show_chain_9(self):
        print(self.__dict__)
        if self.next is not None:
            self.next.show_chain_9()


# a = ForNinth(5)
# print(a.show_chain_9())
# b = ForNinth(5)
# a.insert_object(b)
# print(a.show_chain_9())
# a.del_object(2)
# print(a.show_chain_9())


# Create a program that is a binary tree of a class objects, that contains two other links to this class objects,
# they contain links to another pair if objects, and so forth. The number of the repetition is defined by the attribute
# "num", given to the function.

class Node:

    def __init__(self, num):
        self.left = None
        self.right = None
        self.num = num


def create_binary_tree(num):
    if num == 0:
        return None
    node = Node(num)
    node.left = create_binary_tree(num-1)
    node.right - create_binary_tree(num-1)
    return node


# root = create_binary_tree(3)
