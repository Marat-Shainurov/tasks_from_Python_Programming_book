import main_package.chapter_8_classes
from main_package.chapter_8_classes import *


class TestClasses:

    def test_FirstClass_show(self):
        testing_object = FirstClass("first val", "second val")
        assert testing_object.show() == ("first val", "second val")

    def test_SecondClass(self):
        testing_object_2 = SecondClass("first", "second")
        testing_object_2_2 = SecondClass(1, 10)
        testing_object_2_3 = SecondClass([1], 20)
        assert testing_object_2.show_2() == "first second"
        assert testing_object_2_2.show_2() == 11
        assert testing_object_2_3.show_2() == "This class doesn't contain any attributes!"

    def test_ThirdClass(self):
        testing_object_3 = ThirdClass([x for x in range(10)])
        assert testing_object_3.show_3() == [1, 3, 5, 7, 9]
        assert testing_object_3.average() == sum([1, 3, 5, 7, 9]) / len([1, 3, 5, 7, 9])


def test_create_objects():
    testing_object_4 = main_package.chapter_8_classes.create_objects([1, "two", 3, "four", [6], "five"], "FourthClass")
    assert testing_object_4.show_4() == {"two": 1, "four": 3, "five": 5}
    assert testing_object_4.show_4_class_name() == "FourthClass"


class ForFifth:

    def __init__(self):
        self.name = "Marat"
        self.birth_year = 1990
        self.birt_month = 6
        self.birth_day = 12

    def display_for_fifth(self):
        return self.__dict__


def test_create_new_obj():
    testing_object_5 = ForFifth()
    testing_object_5_1 = main_package.chapter_8_classes.create_new_obj(testing_object_5)
    assert testing_object_5_1.display_for_fifth() == {"birth_year": 1990, "birt_month": 6, "birth_day": 12}


class SixthClass:

    def show_sixth(self):
        return self.__dict__


def test_obj_generator():
    testing_objects = main_package.chapter_8_classes.obj_generator(3, SixthClass)
    assert [x.show_sixth()["value"] for x in testing_objects] == [[1, 3, 5], [1, 3, 5], [1, 3, 5]]


class ForSeventh:
    def display_7(self):
        return self.__dict__["value"]


a = ForSeventh()
a.value = [1, 2, 3, 4, 5]
b = ForSeventh()
b.value = [6, 7, 8, 9, 10]
c = ForSeventh()
c.value = [1, 2, 3]
d = ForSeventh()
d.value = [6, 2, 3, 4, 5]


def test_create_obj_sum():
    testing_obj_7 = main_package.chapter_8_classes.create_obj_sum(a, b)
    testing_obj_7_2 = main_package.chapter_8_classes.create_obj_sum(d, c)
    assert testing_obj_7.display_7() == [7, 9, 11, 13, 15]
    assert testing_obj_7_2.display_7() == [7, 4, 6, 4, 5]
