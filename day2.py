# day2.py

# Part A: List operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Part B: String operations
text = "Python is awesome!"

print("numbers:", numbers)

numbers.append(3)
print("After append:", numbers)

numbers.sort()
print("After sort:", numbers)

avg = sum(numbers) / len(numbers)
print("Average is", avg)

mid = numbers[3:6]
print("Middle three elements:", mid)

# Part B: String operations
text = "Python is awesome!"
print("Uppercase:", text.upper())

count_o = text.count("o")
print("Number of o’s:", count_o)

words = text.split()
print("Words list:", words)

reversed_words = " ".join(words[::-1])
print("Reversed words:", reversed_words)
