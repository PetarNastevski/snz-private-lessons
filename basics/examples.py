# def - key word for function in python

def simple_variables_examples():
    # in python we do not need to specify the variable type, we can just do the following
    a = 5    # integer variable
    b = 2.2  # float

    # python does not have character data type ---> a single char is simple string with a length of 1

    c = "a"    # there is no difference between '' and ""
    d = 'a'

    # also string is interpreted as "list of chars" so everything we can do with lists like: iterations, slice, concatenation, etc...also applies to strings

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
    element_1 = c_list[1]     # access through index   ---> python indexing begins from 0
    element_2 = c_list[-1]    # also we have negative indexing in python ---> element at the position -1 is the last element in the list

    example_list = ['a', 'b', 'c', 'd']
    element_3 = example_list[-1] # element_3 = d
    element_4 = example_list[-2] # element_4 = c

    #because the lists are mutable we can change any element by index
    example_list[2] = 3  #example_list = ['a', 'b', 3, 'd']

    # slicing lists    [index1:index2]  index1 is inclusive, index2 is exclusive
    slice_list1 = [1, 2, 3 ,4, 5]
    sub_slice1 = slice_list1[:3]    # sub_slice = [1, 2, 3]
    sub_slice2 = slice_list1[2:4]   # sub_slice [3, 4]

    # iteration over lists
    for item in list_1:
        print(item)

    for i in range(5):         # range(index1, index2) index1 --> inclusive, index2 ---> exclusive if not specified index1 = 0
        print(list_1[i])

    for i in range(2, 5):      # access elements by index from 2 to 5 without index 5
        print(list_1[i])

    # some of the most important list methods
    methods_examples = ['a', 'b', 'c']
    methods_examples.append('d')    # adds el at the end of the list
    el = methods_examples.pop(1)    # removes and returns the value of the element at given position index
    methods_examples.remove('d')    # remove the first occurrence of the "element" from the list
    methods_examples.reverse()      # reverse the list ['c', 'b', 'a']
    methods_examples.insert(1, 'g') # insert element at given position "index"
    index = methods_examples.index('a') # return the index of the first occurrence of the "element"
    count = methods_examples.count('a') # count and return number of occurrences of "element"
    length = len(methods_examples)      # get the len of the list ---> len = 3

    #list comprehension ---> create a list from another list, for example filter some elements that satisfy some condition
    list1 = [1, 2 ,3, 4, 5, 6]
    list2 = [item for item in list1]  #copy the list1 ---> no condition
    list2 = [item for item in list1 if item > 2]  #[3, 4, 5, 6]


def tuple_examples():
    # imutable(initialized values can't be changed) similar to lists --->both keep the order

    tup_1 = (2, 3) # create predefined tuple
    list_ex = [1, 2]
    tup_2 = tuple(list_ex)  # cast list_ex to tuple using tuple constructor

    for el in tup_2:   #iterate tuple
        print(el)

    list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    for tup in list_of_tuples:   # in each iteration "tuple" is the whole (.....)
        print(tuple)

    # we can access tuple elements by index but not change them
    # tup_1[0] = 2 # we cannot do this

    # but we can do this
    for tup in list_of_tuples:   # in each iteration "tuple" is the whole (.....)
        print(tup[0], tup[1], tup[2])


def set_examples():
    set_1 = set()  # the difference between set and list is that set does not keep the order of the elements which means you cant access them with index


def dict_examples():
    # built in data types that look like this {key: value, key: value}
    # key must be some simple data type while value can be whole list, tuple or even another dictionary

    dict_1 = {}  # initialize dict
    for i in range(3):
        dict_1[i] = i + 1   # construct an dict that look like this {0: 1, 1: 2, 2: 3}

    for key, val in dict_1.items():  # .items ---> interprets pairs of key, val as tuples
        print(key, val)

    for el in dict_1.keys():   # returns list that contains all keys
        print(el)

    for el in dict_1.values():  # returns list that contains all values
        print(el)

    # we can do stuff like this
    suma = sum(dict_1.keys())  # return the sum of the elements that are keys in the dictionary ---> (we will see more examples like this while solving the tasks)


if __name__ == '__main__':
    print("HELLO")
    list_examples()