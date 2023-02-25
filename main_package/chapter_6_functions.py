# Get a function with 2 arguments,
# which returns a sum of multiplications of each list’s element in pairs, one by one.
# If the lengths of these lists are different, the program should use cycle repetition of these element’s usage.

def my_sum(a: list, b: list):
    res = 0
    index_1 = 0
    index_2 = len(b)
    index_3 = len(a)

    if len(a) and len(b) != 0:
        if len(a) >= len(b):
            for element in range(len(a)):
                while index_1 < len(b):
                    res_el = a[index_1] * b[index_1]
                    res += res_el
                    index_1 += 1
                else:
                    while index_2 < len(a):
                        res_el = a[index_2] * b[index_2 - len(b)]
                        res += res_el
                        index_2 += 1
        else:
            for element in range(len(b)):
                while index_1 < len(a):
                    res_el = b[index_1] * a[index_1]
                    res += res_el
                    index_1 += 1
                else:
                    while index_3 < len(b):
                        res_el = b[index_3] * a[index_3 - len(a)]
                        res += res_el
                        index_3 += 1
        return res
    else:
        return 0


# or a shorter version via zip() method


def my_sum_2(a: list, b: list):
    if not a or not b:
        return 0
    res = 0
    for x, y in zip(a * ((len(b) + len(a) - 1) // len(a)), b * ((len(a) + len(b) - 1) // len(b))):
        res += x * y
    return res


# Get a function which gets a list of numbers as the argument and returns a list if odd ones.


def show_odds(l: list):
    res = []
    for element in l:
        if element % 2 != 0:
            res.append(element)
    return res


# Get a function which gets arbitrary number of arguments (numbers) and returns the min one,
# the max one, the average number.


def show_nums(*x):
    return min(x), max(x), sum(x) / len(x)


# Get a function which gets 2 arguments (a string and *args)
# and returns a new string of args indexes of the first argument.


def show_text(text, *nums):
    res = []
    for num in nums:
        try:
            res.append(text[num])
        except IndexError:
            return "No needed index in the text"
    return "".join(res)


# or a shorter version via list comprehensions

def show_text_2(text, *nums):
    res = (text[num] for num in nums if num < len(text))
    return "".join(res) if res else "No needed index in the text"


# Get a function, which get a function and two numbers as its args.
# It returns the result of the argument function (a max element of the list)..


def show_nested_func_res(func, num_1, num_2):
    list_nums = [i for i in range(num_1, num_2 + 1)]
    res = func(list_nums)
    return res


# Get a functions, which gets a function as the firs arg, and the second arg,
# which defines how many times the function (1st arg) should be called.


def snow_func_multiplied(function, n):
    return function * n


# Get a function, which calls itself recursively and returns the odd indexes of a string,
# given as the function’s argument


def get_recursive_text(text):
    if len(text) <= 0:
        print("")
    else:
        print(text[-len(text)], end="")
        get_recursive_text(text[-len(text) + 2:])


# Get a function with 2 arguments, which calls itself recursively and returns the sum of the geometrical progression,
# where the first element == 1, each term is calculated as the first argument multiplied by the previous number.
# The number of terms is defined by the second argument.

def show_recursion_sum(n, amount):
    if amount == 0:
        return 1
    else:
        return n * amount + show_recursion_sum(n, amount - 1)


# Get a function-generator, which creates an iterable object with months names.

def show_months():
    months = ["jan", "feb", "march", "april", "may", "june"]
    for m in months:
        yield m


mon = show_months()

for month in show_months():
    print(month, end=" ")


# Get a function-generator, which creates an iterable object of 2**n,
# where n-s and amounts of the yielded elements is defined by the argument.

def get_2_squares(amount):
    res = [2 ** i for i in range(amount)]
    for el in res:
        yield el


a = get_2_squares(5)

for e in a:
    print(e, end=" ")
