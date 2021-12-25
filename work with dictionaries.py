# The next our task is to consolidate two dictionaries
# in one. Lets try ;)


dictionary_example_1 = {1: 12, 2: 33, 3: 14}
dictionary_example_2 = {4: 13, 5: 35, 6: 16}


# # # # # # # # # # # # # # # # Here we are consolidate two dicts # # # #
def consolidationOfDictionaries():
    dictionary_example_3 = {}

    for elements in (dictionary_example_1, dictionary_example_2):
        dictionary_example_3.update(elements)
    print("using Update function: ", dictionary_example_3)
    # >> {1: 12, 2: 33, 3: 14, 4: 13, 5: 35, 6: 16}
# # # # # # # # # # # or another, more 'python' way # # # # # # # # #
    dictionary_example_4 = {**dictionary_example_1, **dictionary_example_2}
    print("Using ** :", dictionary_example_4)
    # >> {1: 12, 2: 33, 3: 14, 4: 13, 5: 35, 6: 16}

consolidationOfDictionaries()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
