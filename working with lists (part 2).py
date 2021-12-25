# In this task we are asked to put two lists into one

example_list_1 = [1, 4, 7, 5, 4, 2, 12]
example_list_2 = [2, 3, 4, 7, 8, 9, 13]


# # # # Here we are adding one list to another in easiest way # # #
def listAgglomeration():
    example_list_3 = example_list_1 + example_list_2
    print("Adding one list to another is: ", example_list_3)


# >>[1, 4, 7, 5, 4, 2, 12, 2, 3, 4, 7, 8, 9, 13]
# That how result looks like


listAgglomeration()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# or another version of this problem, where we are
# asked to find common to a list of elements

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def CommonElements():
    example_list_4 = [element for element in example_list_1 if element in example_list_2]
    print("Common elements in lists is: ", example_list_4)
    # >> [4, 7, 4, 2]


CommonElements()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
