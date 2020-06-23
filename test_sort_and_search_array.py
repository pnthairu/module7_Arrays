# Start Program
"""
Program: test_sort_and_Search.py
Author: Paul Thairu
Last date modified: 06/019/2020

Purpose of this program is to unit test. Trying to find an element in a list of elements
In my example i have a list of car type and I will try to search and sort list of these cars
"""
import unittest
from sort_search_function import sort_and_search_array

class MyTestCase(unittest.TestCase):
    def test_sort(arry): # sorting the elements in alphabetical order
        new_lst = sorted(arry)
        sort_and_search_array.sort_array(arry)  # using sort function to sort in alphabetical order
        if arry == new_lst:
            print("Pass, car found in the Array")
        else:
            print("Failed, var NOT FOUND IN THE ARRAY")

    def test_search(arry, value):  # searching for an element (car) in the list
        index = sort_and_search_array.search_array(arry, value)
        if index == -1:
            print(value, "Not found")
        else:
            print(value, "Present: ", index)

    my_list_cars = ["Mercedes", "Ford", "Chevrolet", "Jeep"]
    test_search(my_list_cars, "Toyota")  # searching for FORD in the array
    test_search(my_list_cars, "Jeep")   # searching for BMW in the array
    test_sort(my_list_cars)  # sorting the cars in order

# ENd program
