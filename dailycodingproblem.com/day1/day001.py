# yah I know not a good start doing day one on day two :( sorry


# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


theList = [10, 15, 3, 7]
sum = 17

def twoNumberSum(list, k):
    for firstNumber in list:
        for secondNumber in list:
            if ((firstNumber + secondNumber) == k):
                print (f"{firstNumber} + {secondNumber} = {k}")


twoNumberSum(theList, sum)