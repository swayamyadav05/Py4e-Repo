#Experiment-7: Create a list of numbers and perform various operations such as adding elements, removing elements, and accessing elements by index.

numbers = [3, 8, 1, 9, 6]
print(numbers)
numbers.append(7)
numbers.insert(2, 4)
print("After adding elements:", numbers)
addition = sum(numbers)
print("The sum of the numbers is:", addition)
addition = sum(numbers)
numbers.remove(3)
del numbers[0]
print("After removing elements:", numbers)
print("The sum of the numbers is:", sum(numbers))
print("Elemet at index 2:", numbers[2])
print("Last element:", numbers[-1])
