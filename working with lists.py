# In this task, you are asked to assemble a sheet
# that will be filtered according to a certain attribute
example_list = [1, 4, 7, 5, 4, 2, 12]


# # # # # # # # # # # # This part of code print all elements less then 5 # # #
def ElementsLessThenFive():
    for element in example_list:
        if element < 5:
            print("elements less then 5 is: ", element)
# In this task we can choose any number to compare the items in the list to,
# or we can choose another comparison operator (for example, ">")

ElementsLessThenFive()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # Also we can complete this task using function of Python # # # # # # # #
print("Also elements less then 5 ;) : ", list(filter(lambda elem: elem < 5, example_list)))
# Here as a result we have a list (in my example its [1, 4, 4, 2])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
