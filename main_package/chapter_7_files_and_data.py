import fractions
import datetime


# Get a program, which gets the base for a notation and a decimal number from the user's input and returns the number
# in that notation.
def converter_notations(decimal_number, notation_base):
    res = 0
    exp = len(decimal_number)
    for num in decimal_number:
        res_per_cycle = int(num) * notation_base ** (exp - 1)
        exp -= 1
        res += res_per_cycle
    return res
    # return int(str(decimal_number), notation_base)  # the shorter version via int(method)


# Get a finction which gets a decimal number and the number of its byte to return
def get_a_byte(decimal_number, byte_number):
    return str(bin(decimal_number))[byte_number+1]


# Get a function which get a decimal number and returns the sum of its bytes defined as binary.
def get_bytes_sum(decimal_number):
    decimal_number_bin = bin(decimal_number)
    res = [int(decimal_number_bin[num]) for num in range(len(decimal_number_bin)) if num != 0 and num != 1]
    return sum(res)


# get a function which gets a decimal number as the argument and returns reversed octal number.
def get_and_change_into_octal(decimal_number):
    decimal_number_octal = oct(decimal_number)
    return decimal_number_octal[:1:-1]


# Get a function which get 2 rational fractions, calculates their multiplication, subtraction, division and returns
# the max and the min of these three numbers.
def get_mix_and_max_rat_fractions(fraction_1, fraction_2):
    converted_num_1 = fractions.Fraction(fraction_1)
    converted_num_2 = fractions.Fraction(fraction_2)
    multiplied_nums = converted_num_1 * converted_num_2
    divided_nums = converted_num_1 / converted_num_2
    subtracted_nums = converted_num_1 - converted_num_2

    return min(multiplied_nums, divided_nums, subtracted_nums), max(multiplied_nums, divided_nums, subtracted_nums)


# Get a function which gets 2 complex numbers as the arguments, calculates their sum, subtraction,
# multiplication and division, and returns the one with the biggest modulus (absolute value).
def get_biggest_modulus_complex_nums(num_1, num_2):

    elements_tuple = (num_1 + num_2, num_1 - num_2, num_1 * num_2, num_1 / num_2)
    return max(abs(el) for el in elements_tuple)


# get a function which gets two dates as the arguments, and returns the numbers of the days between them.
def get_data_delta(data_1, data_2):
    the_date_1 = datetime.date.fromisoformat(data_1)
    the_date_2 = datetime.date.fromisoformat(data_2)
    delta = datetime.date(the_date_1.year, the_date_1.month, the_date_1.day) - \
            datetime.date(the_date_2.year, the_date_2.month, the_date_2.day)
    return delta.days


# get a function which gets the name of the file, output the file's content and creates the file's copy,
# with the numerated lines.
def get_copy_with_numerated_lines():

    file_name = input("file name: ")
    with open(file_name) as file:
        content = file.read()
        print(content)
        file.seek(0)
        with open("file_name_copy", "w") as f:
            n = 1
            for line in file:
                f.write(f"{n} - {line}")
                n += 1


# Get a program, which creates a file, with the file's name inputted from the user.
# Text to the file is inputted by the user, where all the lowercase letters are changed to uppercase.

file_name = input("Input the file's name: ")
user_text_line_1 = input("Input the text: ")
user_text_line_2 = input("Input the text: ")

with open(file_name, "w") as file:
    file.write(user_text_line_1.lower() + "\n")
    file.write(user_text_line_2.lower() + "\n")
    file.write("bye")


