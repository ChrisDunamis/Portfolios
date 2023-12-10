MY_COURSE = "Project - Simple Calculator"
MY_SUBJECT = "SIMPLE CALCULATOR"

print("\n" + "Course:  ", MY_COURSE)
print("Subject: ", MY_SUBJECT + "\n")


def num1(num1_value):
    return num1_value


def num2(num2_value):
    return num2_value


arithmetic_options = input("""Please select an arithmetic option below:
    - ['1' | '+']: Addition
    - ['2' | '-']: Subtraction
    - ['3' | '*']: Multiplication
    - ['4' | '/']: Division
    
Select option::     """).lower()

if arithmetic_options in ['1', '+']:
    print("\n" + " ADDITION ".center(100, '•'))

    try:
        number_one = float(input("Enter a number: \t"))
        number_two = float(input("Enter a number: \t"))

        if number_one.is_integer() & number_two.is_integer():
            print(('-' * 100) + "\n" +
                  "The sum of {value1} + {value2} is: {result}".format(
                      value1=int(number_one), value2=int(number_two),
                      result=(num1(int(number_one)) + num2(int(number_two)))
                  ))
        else:
            print(('-' * 100) + "\n" +
                  "The sum of {value1} + {value2} is: {result}".format(
                      value1=float(number_one), value2=float(number_two),
                      result=(num1(float(number_one)) + num2(float(number_two)))
                  ))
    except ValueError as VE:
        print(('-' * 100) + "\n" +
              "Error: String value - {error}".format(error=str(VE)[35:]), "is an invalid number..." + "\n" +
              "Please enter a valid Number and try again!")
    except KeyboardInterrupt:
        print("\n" + ('-' * 100) + "\n" +
              "System Interrupted: End of program." + "\n" +
              "If you wish to try again, please restart the program...")
    finally:
        print('-' * 100)

elif arithmetic_options in ['2', '-']:
    print("\n" + " SUBTRACTION ".center(100, '•'))

    try:
        number_one = float(input("Enter a number: \t"))
        number_two = float(input("Enter a number: \t"))

        if number_one.is_integer() & number_two.is_integer():
            print(('-' * 100) + "\n" +
                  "The sum of {value1} - {value2} is: {result}".format(
                      value1=int(number_one), value2=int(number_two),
                      result=(num1(int(number_one)) - num2(int(number_two)))
                  ))
        else:
            print(('-' * 100) + "\n" +
                  "The sum of {value1} - {value2} is: {result}".format(
                      value1=float(number_one), value2=float(number_two),
                      result=(num1(float(number_one)) - num2(float(number_two)))
                  ))
    except ValueError as VE:
        print("\n" + ('-' * 100) + "\n" +
              "Error: String value - {error}".format(error=str(VE)[35:]), "is an invalid number..." + "\n" +
              "Please enter a valid Number and try again!")
    except KeyboardInterrupt:
        print("\n" + ('-' * 100) + "\n" +
              "System Interrupted: End of program." + "\n" +
              "If you wish to try again, please restart the program...")
    finally:
        print('-' * 100)

elif arithmetic_options in ['3', '*']:
    print("\n" + " MULTIPLICATION ".center(100, '•'))

    try:
        number_one = float(input("Enter a number: \t"))
        number_two = float(input("Enter a number: \t"))

        if number_one.is_integer() & number_two.is_integer():
            print(('-' * 100) + "\n" +
                  "The sum of {value1} * {value2} is: {result}".format(
                      value1=int(number_one), value2=int(number_two),
                      result=(num1(int(number_one)) * num2(int(number_two)))
                  ))
        else:
            print(('-' * 100) + "\n" +
                  "The sum of {value1} * {value2} is: {result}".format(
                      value1=float(number_one), value2=float(number_two),
                      result=(num1(float(number_one)) * num2(float(number_two)))
                  ))
    except ValueError as VE:
        print("\n" + ('-' * 100) + "\n" +
              "Error: String value - {error}".format(error=str(VE)[35:]), "is an invalid number..." + "\n" +
              "Please enter a valid Number and try again!")
    except KeyboardInterrupt:
        print("\n" + ('-' * 100) + "\n" +
              "System Interrupted: End of program." + "\n" +
              "If you wish to try again, please restart the program...")
    finally:
        print('-' * 100)

elif arithmetic_options in ['4', '/']:
    print("\n" + " DIVISION ".center(100, '•'))

    try:
        number_one = float(input("Enter a number: \t"))
        number_two = float(input("Enter a number: \t"))

        if number_one.is_integer() & number_two.is_integer():
            print(('-' * 100) + "\n" +
                  "The sum of {value1} ÷ {value2} is: {result}".format(
                      value1=int(number_one), value2=int(number_two),
                      result=(num1(int(number_one)) // num2(int(number_two)))
                  ))
        else:
            print(('-' * 100) + "\n" +
                  "The sum of {value1} ÷ {value2} is: {result}".format(
                      value1=float(number_one), value2=float(number_two),
                      result=(num1(float(number_one)) / num2(float(number_two)))
                  ))
    except ZeroDivisionError as ZDE:
        number_one = None
        number_two = 0

        print(('-' * 100) + "\n" +
              "Error: The operation {error!r} passed onto Value 2, is mathematically wrong.".format(
                  error=str(ZDE).title()
              ) + "\n" +
              "Please enter a valid Number and try again!")
    except ValueError as VE:
        print("\n" + ('-' * 100) + "\n" +
              "Error: String value - {error}".format(error=str(VE)[35:]), "is an invalid number..." + "\n" +
              "Please enter a valid Number and try again!")
    except KeyboardInterrupt:
        print("\n" + ('-' * 100) + "\n" +
              "System Interrupted: End of program." + "\n" +
              "If you wish to try again, please restart the program...")
    finally:
        print('-' * 100)
else:
    print(('-' * 100) + "\n" +
          "Please choose a valid option!" + "\n" +
          "Restart the program and try again..." + "\n" +
          ('-' * 100))
