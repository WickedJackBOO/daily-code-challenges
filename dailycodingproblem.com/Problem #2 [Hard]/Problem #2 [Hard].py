# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?


arrayIn = [1, 2, 3, 4, 5]
arrayOut = []
indexNum = 0
print(len(arrayIn))
while indexNum <= (len(arrayIn)-1):
    print(f"index of: {indexNum}")
    firstNumber = True
    poped = arrayIn.pop(indexNum)
    print(f"poped: {poped}")
    for j in arrayIn:
        if firstNumber == True:
            product = j
            print(f"start product: {j}")
            firstNumber = False
        else:
            product *= j
            print(f"product sofar: {product/j} * {j} = {product}")
    arrayIn.insert(indexNum, poped)
    arrayOut.append(product)
    print(f"array out sofar: {arrayOut}")
    indexNum += 1
    print()
print(arrayOut)
