# --------------------------------------------------- QUESTION 13 ---------------------------------------------------- #
print("\n" + "Question 13".center(110, '_'))

"""
(13): Write a Python function that prints out the first n rows of Pascal's triangle.
      Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

      Sample Pascal's triangle :
              
                      [1]
                    [1] [1]
                  [1] [2] [1]
                [1] [3] [3] [1]
              [1] [4] [6] [4] [1]
              
      Each number is the two numbers above it added together
"""


def get_pascals_triangle(n_rows):
    """The sum of Pascals Triangle for the given number of rows.

:param n_rows: The number of integer rows for the Pascals Triangle, where ``n`` and any integer ``0 ≤ k ≤ n``.
:type n_rows: int

:return: ``(n / k) = ((n - 1) / (k - 1)) + ((n - 1) / k)``
:rtype: list[list[int]]
    """

    pascals_result = []

    for rows in range(n_rows):
        temp_list = []

        for columns in range(rows + 1):
            if (columns == 0) or (columns == rows):
                temp_list.append(1)
            else:
                temp_list.append(pascals_result[rows - 1][columns - 1] + pascals_result[rows - 1][columns])

        pascals_result.append(temp_list)

    return pascals_result


def display_pascals_triangle():
    """Takes the number of rows and displays the type of Pascals Triangle from the user input.

:returns: None
    """

    print("Please choose a style of view, from the options below.")

    while formatter := input("""(1): Left-Angle Triangle
(2): Right-Angle Triangle
(3): Pyramid Triangle

Choose an option::      """).strip():
        if formatter in ('1', '2', '3'):
            break
        else:
            print("\n" + "Please choose a valid integer option, below.")

    print()
    print("Please choose a number value for the Pascals Triangle.")

    while pascals_triangle_rows := input("Enter Number of Rows::       ").strip():
        if pascals_triangle_rows.isdigit():
            pascals_triangle_rows = int(pascals_triangle_rows)

            if pascals_triangle_rows < 1:
                print("\n" + "A valid integer must be 1 < n.")
            else:
                break
        else:
            print("\n" + "Please enter a valid integer.")

    print()

    pascals_triangle = get_pascals_triangle(pascals_triangle_rows)

    # print("Pascal Results:", pascals_triangle, end="\n\n")

    # The "Variable: max_width", takes the format from the last/longest row to get the max width for each line we have
    max_width = len(" ".join([f"[{num}]" for num in pascals_triangle[-1]]))  # to print

    # This For Loop, loops over each row in the Pascal's Triangle getting each row's value 1 by 1 from the For Loop
    for row in pascals_triangle:  # Variable: row. Then for each number in the current row, format it into a string
        row_str = " ".join([f"[{num}]" for num in row])  # with square brackets around each number and join them with a
        # space in between.

        if formatter == '1':
            print(row_str)
        elif formatter == '2':
            print(row_str.rjust(max_width))
        elif formatter == '3':
            print(row_str.center(max_width))


display_pascals_triangle()

print('-' * 110)
# -------------------------------------------------------------------------------------------------------------------- #
