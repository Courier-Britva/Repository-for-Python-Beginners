# The classic "palindromes" problem. I propose to make it more complicated

# Palindrome* is a word that reads the same both ways (like "aboba")

# # # # # # # Here we are checking is word palindrome or not # # # # # # # #
def palindromeChecker():
    while True:  # here we are making loop of function
        def is_palindrome(string):
            return string == string[::-1]  # This function checks if the letter with the
                                           # step forward first and the step backward from
                                           # the end will be the same

        word = input("\nHere we are checking is word Palindrome or not. \nWrite your word here: ")
        if is_palindrome(word):
            print("Yes! Its palindrome! Awesome ;0 \nLets try again")
        else:
            print("no,", word, "is not palindrome :(\nLets try again")


palindromeChecker()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
