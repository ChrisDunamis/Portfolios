# ---------------------------------------------------- QUESTION 1 ---------------------------------------------------- #
"""
(1): Write a Python function to find the maximum of three numbers.
"""


def maximum_of_three_numbers1(num1, num2, num3):  # METHOD 1:
    nums_list = num1, num2, num3

    print("\n" + "Question 1".center(80, '_') + "\n" +
          "Numbers Given:")

    for idx, value in enumerate(nums_list):
        print("|Value {idx}|: {num_value}".format(idx=(idx + 1), num_value=value))

    if (num1 > num2) and (num1 > num3):
        return "\n" + "The maximum number from the above values is Value 1: {}".format(num1)
    elif (num2 > num1) and (num2 > num3):
        return "\n" + "The maximum number from the above values is Value 2: {}".format(num2)
    elif (num3 > num1) and (num3 > num2):
        return "\n" + "The maximum number from the above values is Value 3: {}".format(num3)
    elif (num1 == num2) and (num1 and num2) > num3:
        return "\n" + "The maximum numbers from the above values is Values 1 and 2:" + "\n" + \
            "Value 1 = {}".format(num1) + "\n" + \
            "Value 2 = {}".format(num2) + "\n"
    elif (num2 == num3) and (num2 and num3) > num1:
        return "\n" + "The maximum numbers from the above values is Values 2 and 3:" + "\n" + \
            "Value 2 = {}".format(num2) + "\n" + \
            "Value 3 = {}".format(num3) + "\n"
    elif (num3 == num1) and (num3 and num1) > num2:
        return "\n" + "The maximum numbers from the above values is Values 1 and 3:" + "\n" + \
            "Value 1 = {}".format(num1) + "\n" + \
            "Value 3 = {}".format(num3) + "\n"

    return "\n" + "The maximum numbers from the above values are the Numbers Given:" + "\n" + \
        "Value 1 = {}".format(num1) + "\n" + \
        "Value 2 = {}".format(num2) + "\n" + \
        "Value 3 = {}".format(num3) + "\n"


def maximum_of_three_numbers2(num1, num2, num3):  # METHOD 1:
    nums_list = (num1, num2, num3)

    return max(nums_list)


maximum_number = (1, 2, 3)  # Pass the values on here...
maximum_numbers1_result = maximum_of_three_numbers1(*maximum_number)
maximum_numbers2_result = maximum_of_three_numbers2(*maximum_number)

# Method 1 Output: This gives an output for each value.
print(maximum_numbers1_result)  # If multiple values have the same max numbers, it will be returned.

# Method 2 Output: A simple output, that returns the max number.
print("The maximum number from the List {} is: {:>7}".format(maximum_number, maximum_numbers2_result))
print('-' * 80)
# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------- QUESTION 2 ---------------------------------------------------- #
"""
(2): Write a Python function to sum all the numbers in a list.
     Sample List     : (8, 2, 3, 0, 7)
     Expected Output : 20
"""


def sum_of_numbers(args):
    total = 0
    sum_values = args

    for value in sum_values:
        total = total + value

    return total


sum_of_these_values = (8, 2, 3, 0, 7)  # Pass the values on here...
sum_of_these_values_result = sum_of_numbers(sum_of_these_values)

print("Question 2".center(80, '_') + "\n" +
      "The sum of", end=' ')
print(*sum_of_these_values, sep=" + ", end=" = ")
print(sum_of_these_values_result)  # Method 1
# print(sum(sum_of_these_values))    # Method 2
print('-' * 80)
# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------- QUESTION 3 ---------------------------------------------------- #
"""
(3): Write a Python function to multiply all the numbers in a list.
     Sample List     : (8, 2, 3, -1, 7)
     Expected Output : -336 
"""


def multiply_all_numbers(args):
    multiply_by = 1
    multiply_each_value = args

    for each_value in multiply_each_value:
        multiply_by = multiply_by * each_value

    return multiply_by


multiplier = 1
multiply_these_values = (8, 2, 3, -1, 7)  # Pass the values on here...
multiply_these_values_result = multiply_all_numbers(multiply_these_values)

print("Question 3".center(80, '_') + "\n" +
      "The sum of", end=' ')
print(*multiply_these_values, sep=" * ", end=" = ")
print(multiply_these_values_result)  # Method 1

for each_number in multiply_these_values:
    multiplier = multiplier * each_number

# print(multiplier)  # Method 2
print('-' * 80)
# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------- QUESTION 4 ---------------------------------------------------- #
"""
(4): Write a Python program to reverse a string.
     Sample String   : "1234abcd"
     Expected Output : "dcba4321"
"""


def reverse_string(string):
    return string[::-1]


string_input = "1234abcd"  # Pass the values on here...
reversed_string = reverse_string(string_input)

print("Question 4".center(80, '_') + "\n" +
      "String Input:    {str_input}".format(str_input=string_input) + "\n" +
      "String Reversed: {str_reversed}".format(str_reversed=reversed_string) + "\n" +
      ('-' * 80))
# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------- QUESTION 5 ---------------------------------------------------- #
"""
(5): Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the 
     number as an argument.
"""


def calculate_the_factorial_of_a_number(non_negative_int):
    factorial = 1                 # A Non-Negative Integer, which also is a counter, starts/set at the value 1.
    factorial_values = []         # The given values for the factorial is appended onto this empty list.
    num_value = non_negative_int  # The given value for the factorial.

    # This For Loop, allows the values of the given factorial, to be in reversed order. Which will be used for the
    for idx in range(1, (num_value + 1)).__reversed__():  # output. Since the formula for the factorial is "n - 1".
        factorial_values.append(idx)  # Adds the index of the given value(s) onto the "Variable: factorial_values".
        factorial = factorial * idx   # Multiplies the values of the index to the value of the "Variable: factorial".

    # Output:
    print("The Factorial of {factorial_value}! is:".format(factorial_value=factorial_values[0]))
    print(*factorial_values, sep=" * ", end=" = ")

    return factorial  # Returns the sum of the factorial.


factorial_value = 5  # Pass the value on here...
factorial_results = calculate_the_factorial_of_a_number(factorial_value)

print(factorial_results)
# -------------------------------------------------------------------------------------------------------------------- #
