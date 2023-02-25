from main_package import chapter_7_files_and_data
import fractions
import datetime


def test_converter_notations():
    assert chapter_7_files_and_data.converter_notations("32", 20) == 62
    assert chapter_7_files_and_data.converter_notations("120", 12) == 168
    assert chapter_7_files_and_data.converter_notations("2650", 32) == 71840


def test_get_a_byte():
    assert chapter_7_files_and_data.get_a_byte(100, 3) == "0"
    assert chapter_7_files_and_data.get_a_byte(100, 2) == "1"
    assert chapter_7_files_and_data.get_a_byte(1234, 4) == "1"
    assert chapter_7_files_and_data.get_a_byte(1234, 5) == "1"
    assert chapter_7_files_and_data.get_a_byte(1234, 6) == "0"


def test_get_bytes_sum():
    assert chapter_7_files_and_data.get_bytes_sum(100) == 3
    assert chapter_7_files_and_data.get_bytes_sum(1234) == 5


def test_get_and_change_into_octal():
    assert chapter_7_files_and_data.get_and_change_into_octal(120) == "071"
    assert chapter_7_files_and_data.get_and_change_into_octal(2345) == "1544"
    assert chapter_7_files_and_data.get_and_change_into_octal(19) == "32"


def test_get_mix_and_max_rat_fractions():
    assert chapter_7_files_and_data.get_mix_and_max_rat_fractions("3/5", "6/7") == \
           (fractions.Fraction(-9, 35), fractions.Fraction(7, 10))
    assert chapter_7_files_and_data.get_mix_and_max_rat_fractions("12/19", "6/7") == \
           (fractions.Fraction(-30, 133), fractions.Fraction(14, 19))

def test_get_biggest_modulus_complex_nums():
    assert chapter_7_files_and_data.get_biggest_modulus_complex_nums(3+4j, 9+6j) == 54.08326913195984


def test_get_delta_date():
    assert chapter_7_files_and_data.get_data_delta("2023-02-25", "1990-06-12") == 11946
