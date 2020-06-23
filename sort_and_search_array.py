from array import array as arr
from filecmp import cmp

# Start Program
"""
Program: sort_and_Search_array.py
Author: Paul Thairu
Last date modified: 06/23/2020

You can make a new files test_sort_and_search_array.py and sort_and_search_array.py. 
In the appropriate directories. For this assignment, 
you can hard-code a list you pass to the sort_array() and search_array(). 

Eventually write 2 functions sort_array() and search_array().
search_array() will return the index of the object in the list or a -1 if the item is not found
sort_array() will sort the list


"""
# declaring getList function and with array list parameter
def get_array(arr):
    print(arr)  # print the list of items


# Declaring searchList function with array list and subject to search parameters
def search_array(arr, subject):
    print("****************************************************")
    print(subject)  # element to search on th list
    for i in arr:  # looping through the list to find an element
        if (i == subject):  # if car is not in the list break
            break
    if subject in arr:
        pass
    else:
        return -1  # returning a value that does not exit in the array


def sort_array(arr):
    arr.sort()  # in build sort function to sort subject in alphabetical order
    print("Subjects in alphabetical order")
    print(arr)  # Print list of subjects in order


if __name__ == '__main__':
    arr = ['Maths', 'English', 'Biology', 'Chemistry', 'Physics']  # my hard coded array list
    subject = "French"  # car to search subject in the array list
    get_array(arr)  # function call and assigning to array of subjects
    if (search_array(arr, subject) == -1):  # If subject not found
        print(subject + " 'Does not exit in the ARRAY !!!!!!!'")
    else:  # if subject is found
        print(subject + " FOUND in the subject array..")
    print("****************************************************")
    sort_array(arr)  # sorting list in alphabetical order
