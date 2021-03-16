# Python program to print all permutations of a given string. Hyper-exponential time complexity.

def toString(List):
    return ''.join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String  in the form of a list of characters
# 2. Starting index of the string. Initially 0, but updated at recursive call.
# 3. Ending index of the string. Initially len(string) - 1, but updated at recursive call.
def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]  # swap
            permute(a, l + 1, r)     # rec call
            a[l], a[i] = a[i], a[l]  # unswap to backtrack to the other choices.


if __name__ == '__main__':
    # Driver program to test the above function
    string = "ABC"
    n = len(string)
    a = list(string)
    permute(a, 0, n - 1)

    string = "JASON"            #5! = 120 permutations
    n = len(string)
    a = list(string)
    permute(a, 0, n - 1)

    # This code was originally contributed by Bhavya Jain here: https://www.geeksforgeeks.org/python-program-to-print-all-permutations-of-a-given-string/
    # and was adapted to Python 3 by Jason Filippou (https://github.com/jasonfilippou).