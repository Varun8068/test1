numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2,numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]


numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 5, 8]
