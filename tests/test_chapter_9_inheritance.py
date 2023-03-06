from main_package import chapter_9_inheritance


def test_objects_sum():
    testing_instance_1 = chapter_9_inheritance.SumObjects([1, 2, 3])
    testing_instance_2 = chapter_9_inheritance.SumObjects([4, 5, 6, 7])
    testing_instance_res = testing_instance_1 + testing_instance_2
    assert testing_instance_res.show() == [1, 2, 3, 4, 5, 6, 7]


def test_fourth_class():
    testing_instance = chapter_9_inheritance.FourthClass(10)
    assert testing_instance.__add__(15) == 25
    assert testing_instance.__sub__(6) == 4
    assert testing_instance.__rsub__(25) == 15


def test_fifth_class():
    testing_instance_1 = chapter_9_inheritance.FifthClass([1, 2, 10])
    testing_instance_2 = chapter_9_inheritance.FifthClass([9, 7, 15])
    eq_res = testing_instance_1 == testing_instance_2
    ne_res = testing_instance_1 != testing_instance_2
    lt_res = testing_instance_1 < testing_instance_2
    assert eq_res == False
    assert ne_res == True
    assert lt_res == True


# def test_sixth_class():
#     testing_instance = chapter_9_inheritance.SixthClass()
#
