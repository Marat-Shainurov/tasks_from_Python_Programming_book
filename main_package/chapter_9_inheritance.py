
# Create an inheritance chain, that creates 3 classes, the base class has a field, each next class creates another
# field. Declare overriding methods in the derived classes which allow to assign values to the fields and display them.

class Alpha:

    def __init__(self, val):
        self.value = val

    def set(self, new_val):
        self.value = new_val

    def show(self):
        print(self.value)

class Bravo(Alpha):

    def __init__(self, val, name):
        super().__init__(val)
        self.name = name

    def set(self, new_val, new_name):
        self.value = new_val
        self.name = new_name

    def show(self):
        super().show(), print(self.name)

class Charlie(Bravo):

    def __init__(self, val, name, birth_date):
        Bravo.__init__(self, val, name)
        self.birth_date = birth_date

    def show(self):
        super().show(), print(self.birth_date)

# A = Alpha(32)
# A.show()
# A.set(33)
# A.show()
# B = Bravo(32, "Marat")
# B.show()
# B.set(33, "M")
# B.show()
# C = Charlie(32, "M.S.", [12, 6, 1990])
# C.show()


# Create a class with overriding methods for casting. The class object has to have the integer/strings/float fields.
# Casting methods return the corresponding field's value.
class MyClass:

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return str(self.txt)

    def __float__(self):
        return float(self.fract)

# A = MyClass()
# A.value = "12.06.1990"
# A.txt = "Marat"
# A.fract = 32.7
# print(int(A.value))
# print(str(A.txt))
# print(float(A.fract))

# Create a class with the __add__ method. Each object has to have a list fild, the adding method returns a new object,
# with a list of compiled two list (from these two objects).
class SumObjects:

    def __init__(self, lst):
        self.data = lst

    def __add__(self, obj_2):
        res = self.data + obj_2.data
        return SumObjects(res)

    def show(self):
        return self.data


# Create a class with casting methods (sum, subtraction from the number, subtraction the number).
class FourthClass:

    def __init__(self, num):
        self.number = num

    def __add__(self, other):
        return self.number + other

    def __sub__(self, other):
        return self.number - other

    def __rsub__(self, other):
        return other - self.number


# Create a class with the comparison methods. Each object has a field with a list of number. The __eq__() methods check
# their first elements, the __ne__() method checks their second elements, the __lt__() one check their third elements.
# If any of these two lists is shorter than 3 elements 0 is used.
class FifthClass:

    def __init__(self, lst):
        self.data = lst

    def __eq__(self, other):
        return bool(self.data and other.data and self.data[0] == other.data[0])

    def __ne__(self, other):
        if len(self.data) > 1 and len(other.data) > 1:
            return self.data[1] != other.data[1]
        else:
            return self.data[1] != 0 if len(self.data) > len(other.data) else other.data[1] != 0

    def __lt__(self, other):
        if len(self.data) > 2 and len(other.data) > 2:
            return self.data[2] < other.data[2]
        else:
            return self.data[2] < 0 if len(other.data) < 2 else other.data[2] < 0


# Create a class, with a special mode of accessing to its objects. Each object has to have a list field the value of
# which could be assigned the list type only. From the list being assigned only literals are appended to the field.
# When the field's value is read the first letters of each element should be returned.

class SixthClass:

    def __setattr__(self, attr_name, value):
        if isinstance(value, list):
            L = []
            for el in value:
                if isinstance(el, str):
                    L.append(el)
            self.__dict__[attr_name] = L

    def __getattribute__(self, item):
        if item.startswith("__"):
            return object.__getattribute__(self, item)
        else:
            print("the field is called -", item)
            res = object.__getattribute__(self, item)
            return "First letters - " + ".".join(res[x][0] for x in range(len(res))) + "."

    def __getattr__(self, item):
        print("No such attribute - ", end="")
        return item


# A = SixthClass()
# A.data = ["Shainurov", "Marat", 12, 6, 1990, ["june"], "Olegovich"]
# print(A.data)
# print(A.num)
# A.integer = 123
# print(A.integer)

# Create a program with a class which attributes can be iterated.
# Each object has to have 2 fields with lists of numbers.
# While indexing the sum of corresponding elements of these 2 lists is returned.
# If any of these element doesn't have such element – 0 is used.

class SeventhClass:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2
        self.position = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.position += 1
        if self.position >= max(len(self.list_1), len(self.list_2)):
            raise StopIteration
        res = (self.list_1[self.position] if self.position < len(self.list_1) else 0) + (
            self.list_2[self.position] if self.position < len(self.list_2) else 0)
        return res

# A = SeventhClass([1, 2, 3, 0, 9], [4, 5, 6, 7])
# try:
#     while True:
#         print(next(A))
# except StopIteration:
#     print()
# except IndexError:
#     print()

# Create a program with a class with callable objects. Each object has to have a field with list of numbers.
# As the result the object returns polynomial sum, which means that if the list is an object of type
# a0, a1, a2, a3 ... an, after passing "x" as the argument the program returns a0, a1*x, a2*x^2, a3*x^3 ... an*x^n.

class EightClass:

    def __init__(self, nums):
        self.nums = nums

    def __call__(self, n):
        res = sum([self.nums[x]*n**x for x in range(len(self.nums))])
        return res


# A = EightClass([1, 2, 3, 4, 5])
# print(A(2))
# Create a program with a class that has in iterator generating odd numbers. The number of its elements
# is regulated by the passed argument.

class NinthClass:

    def __init__(self, n):
        self.nums = n
        self.position = -1
        self.lst = [x*2+1 for x in range(n)]

    def __iter__(self):
        return self

    def __next__(self):
        self.position += 1
        if self.position < self.nums:
            return self.lst[self.position]
        else:
            raise StopIteration


# A = NinthClass(5)
# try:
#     while True:
#         print(next(A))
# except StopIteration:
#     print()

# Create a program with a class, that generates the Fibonacci numbers list. The number of elements is passed as the
# argument to the class constructor.

class TenthClass:

    def __init__(self, n):
        self.nums = n
        self.fibs = [1, 1]
        a = 1
        b = 1
        for k in range(self.nums-2):
            a, b = b, a+b
            self.fibs.append(b)
        self.position = -1

    def __getitem__(self, index):
        return self.fibs[index]

    def __iter__(self):
        return self

    def __next__(self):
        self.position += 1
        if self.position < self.nums:
            return self.fibs[self.position]
        else:
            raise StopIteration

# A = TenthClass(5)
# try:
#     while True:
#         print(next(A))
# except StopIteration:
#     print()
# except IndexError:
#     print()