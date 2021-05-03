# def - key word for function in python

# here we will have functions with examples that will explain the built-in data types and everything we need to know
# about them in order to successfully solve the given tasks

def list_examples():
    # mutable (you can change the elements of the list as you wish) built in data type that can store all kinds of
    # data types provide access through index to them and also provides iteration over them

    list_a = [] # one way to initialize a list
    list_b = list() # another way to initialize a list

    # list can store all kinds of data types for example:

    # lists of predefined elements
    list_1 = [1, 2 ,3 ,4 ,5]  # list of integers
    list_2 = ["petar", "martin", "igor"]  # list of strings
    list_3 = [list_1, list_2] # list of lists

    list_4 = list(list_1) # cast any other "iterable" data type to list via the list constructor
    # lists can also store tuples, dicts, sets - data types that we will see later, also the hierarchy can go as deep as we like
    # list in list in list etc...

    # different things we can do with lists
    c_list = list_1 + list_2  # concatenate two lists in one ---> [1, 2, 3] + [4, 5, 6] = [1, 2, 3, 4, 5, 6]
    element_1 = c_list[1]  # access through index   ---> python indexing begins from 0
    element_2 = c_list[-1] # also we have negative indexing in python ---> element at the position -1 is the last element in the list

    example_list = ['a', 'b', 'c', 'd']
    element_3 = example_list[-1] # element_3 = d
    element_4 = example_list[-2] # element_4 = c

    #because the lists are mutable we can change any element by index
    example_list[2] = 3  #example_list = ['a', 'b', 3, 'd']
