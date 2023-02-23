from main_package import chapter_6_functions


def test_my_sum_normal():
    assert chapter_6_functions.my_sum([1, 2, 3, 4, 5], [1, 2, 3]) == 28
    assert chapter_6_functions.my_sum([1, 2, 3], [1, 2, 3, 4, 5]) == 28
    assert chapter_6_functions.my_sum([], [1, 2, 3, 4, 5]) == 0


def test_show_odds():
    assert chapter_6_functions.show_odds([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert chapter_6_functions.show_odds([3, 7, 13, 6, 8]) == [3, 7, 13]
    assert chapter_6_functions.show_odds([]) == []


def test_show_nums_normal():
    assert chapter_6_functions.show_nums(1, 2, 3, 4, 5) == (1, 5, 3.0)


def test_show_text_normal():
    assert chapter_6_functions.show_text("Marat", 1, 2, 4) == "art"


def test_show_text_no_index():
    assert chapter_6_functions.show_text("Marat", 1, 2, 9) == "No needed index in the text"


def test_show_nested_func_res():
    def get_max(nums):
        res = max(nums)
        return res

    assert chapter_6_functions.show_nested_func_res(get_max, 1, 7) == 7


def test_show_func_multiplied_normal():
    def func():
        return "M"

    assert chapter_6_functions.snow_func_multiplied(func(), 5) == "MMMMM"


def test_show_recursive_sum():
    assert chapter_6_functions.show_recursion_sum(2, 5) == 1 + 1 * 2 + 2 * 2 + 3 * 2 + 4 * 2 + 5 * 2
