from random import randint


# ---------------------------------------------------- QUESTION 6 ---------------------------------------------------- #
print("\n" + "Question 6".center(110, '_'))

"""
(6): Write a Python function to check whether a number falls within a given range.
"""


def number_given_range(num):
    num1, num2 = 1, 10  # Number range...
    num_range = randint(num1, num2)

    if num == 0:
        return "Incorrect!!" + "\n\n" + \
            \
            "Given Number: {value}".format(value=num) + "\n" + \
            "You have entered the Number: {value}. Please give a value between {value1} - {value2}.".format(
                value=num, value1=num1, value2=num_range)
    elif num1 <= num <= num_range:
        return "Correct!" + "\n\n" + \
            \
            "Given Number: {value}".format(value=num) + "\n" + \
            "This is within the range {value1} - {value2}.".format(value1=num1, value2=num_range)
    # elif num != num_range:
    #     return "\n" + "Incorrect!" + "\n\n" + \
    #         \
    #         "Given Number: {value}".format(value=num) + "\n" + \
    #         "This is not in the range {value1} and {value2}.".format(value1=num1, value2=num_range)

    return "Incorrect!!" + "\n\n" + \
        \
        "Given Number: {value}".format(value=num) + "\n" + \
        "This is a negative number, please give a value between {value1} - {value2}.".format(
            value1=num1, value2=num_range
        )


value1, value2 = -10, 10
user_num = randint(value1, value2)
user_result = number_given_range(user_num)

print(user_result)
print('-' * 110)
# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------- QUESTION 7 ---------------------------------------------------- #
print("Question 7".center(110, '_'))

"""
(7): Write a Python function that accepts a string and counts the number of upper and lower case letters.
     Sample String : 'The quick Brow Fox'
     Expected Output : No. of Upper case characters : 3
                       No. of Lower case Characters : 12
"""


def count_string_characters(input_string):
    """
    Takes the "Parameter: input_string", as String value(s) from the "Variable: string".
    """

    strings = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  # Alphabets defined in UPPER and lower cases.

    # Gets the sum as an integer of the lower cased string.
    lower_cased_str = sum(lower_case.islower() for lower_case in input_string)

    # Get the sum as an integer of the UPPER CASED string.
    upper_cased_str = sum(upper_case.isupper() for upper_case in input_string)

    # The "Function: lambda", returns the given Expression defined as "special_chars". This will check the Argument
    # passed into the "Parameter: (input_string)", and check for occurrences in the "Variable: strings". If the values
    # given into the "Parameter: (input_string)", are not listed in the "Variable: strings", then it will be "filtered"
    # out as a "special_chars_str". This is then wrapped in the "Functions: list() and len()", to get the sum of
    # elements/special characters used in the given string.
    special_chars_str = len(list(filter(lambda special_chars: special_chars not in strings, input_string)))
    false_strings = "String format must be in [A-Z] or [a-z], and can also include spaces, commas or special " + \
                    "characters." + "\n\t  " + \
                    "Please try again!"

    # A condition designed to catch if numeric values are on to the Parameter. If that is True, then it prints the
    if any(each_char.isdigit() for each_char in input_string):  # Variable: false_strings, as a message.
        lower_cased_str = 0  # Resets the values of the variables below.
        upper_cased_str = 0
        special_chars_str = 0

        print("NOTE:", false_strings + "\n")

        return lower_cased_str, upper_cased_str, special_chars_str

    return lower_cased_str, upper_cased_str, special_chars_str


string = "Th€ qu!ck Brow Fox"  # Pass the values on here...
sum_lower_str, sum_upper_str, sum_special_chars_str = count_string_characters(string)  # Collects the values returned
# from the "Function: count_string_characters()".

print("Function - count_string_characters():", count_string_characters.__doc__ + "\n" +

      "Input String: {!r} contains...".format(string) + "\n\n" +

      "[{}] lower-cased character(s).".format(sum_lower_str) + "\n" +
      "[{}] UPPER-CASED character(s).".format(sum_upper_str) + "\n" +
      "[{}] Special character(s).".format(sum_special_chars_str) + "\n" +
      ('-' * 110))
# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------- QUESTION 8 ---------------------------------------------------- #
print("Question 8".center(110, '_'))

"""
(8): Write a Python function that takes a list and returns a new list with distinct elements from the first list.
     Sample List : [1,2,3,3,3,3,4,5]
     Unique List : [1, 2, 3, 4, 5]
"""


def return_distinct_elements_from_list(user_list):
    unique_elements = []

    for element in user_list:
        if element not in unique_elements:
            unique_elements.append(element)

    return unique_elements


integer_list = [1, 2, 3, 3, 3, 3, 4, 5]  # Pass the values on here...
unique_list = return_distinct_elements_from_list(integer_list)


print("Input List:  {}".format(integer_list) + "\n" +
      "Unique List: {}".format(unique_list) + "\n" +
      ('-' * 110))
# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------- QUESTION 9 ---------------------------------------------------- #
print("Question 9".center(110, '_'))

"""
(9): Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
     Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 
            1 and itself.
"""


def prime_number(number):
    valid_prime_number = True

    if number <= 1:
        return "Must be greater than 1!", "NOTE: The number [{}] <= 1".format(number)
    else:
        for num in range(2, number):
            if (number % num) == 0:
                valid_prime_number = False
                break

    if valid_prime_number:
        return number, "This is a Prime Number."

    return number, "This is NOT a Prime Number."


input_num = 7  # Pass the values on here...
check_prime_number, is_prime = prime_number(input_num)

print("Input Number: [{value}]".format(value=check_prime_number) + "\n" +
      "{result}".format(result=is_prime) + "\n" +
      ('-' * 110))
# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------- QUESTION 10 ---------------------------------------------------- #
print("Question 10".center(110, '_'))

"""
(10): Write a Python program to print the even numbers from a given list.
      Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
      Expected Result : [2, 4, 6, 8]
"""


def return_even_numbers_in_list(given_list):
    even_numbers_in_list = [num for num in given_list if (num % 2) == 0]
    odd_numbers_in_list = [num for num in given_list if (num % 2) != 0]

    return even_numbers_in_list, odd_numbers_in_list


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Pass the values on here...
even_lists, odd_lists = return_even_numbers_in_list(input_list)

print("Given List: {}".format(input_list) + "\n\n" +

      "Even Numbers in List: {even}".format(even=even_lists) + "\n" +
      "Odd Numbers in List:  {odd}".format(odd=odd_lists) + "\n" +
      ('-' * 110))
# -------------------------------------------------------------------------------------------------------------------- #
