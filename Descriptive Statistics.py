while True:
    # Getting a list of numbers as string
    input_string = input(
        "Enter numbers to make some calculations, separated by a space or a comma: "
    )
    print("\n")
    input_string = input_string.replace(",", " ")
    user_list = input_string.split()

    # convert each item to float type
    for i in range(len(user_list)):
        user_list[i] = float(user_list[i])

    def number_format(num):
        if num % 1 == 0:
            return int(num)
        else:
            return float(num)

    # apply the number_format function for all items in the list
    for i in range(len(user_list)):
        user_list[i] = number_format(user_list[i])

    user_list.sort()

    # Useful Calculations
    mean = sum(user_list) / len(user_list)

    lst = [(user_list[i] - mean)**2 for i in range(len(user_list))]

    variance = (sum(lst) / len(user_list))

    def sqrt(x):
        return x**0.5

    standard_deviation = sqrt(variance)

    print("This is your list after sorting it " + str(user_list))
    print("The mean = " + str(number_format(mean)))
    print("The variance = " + str(number_format(variance)))
    print("The standard_deviation = " + str(number_format(standard_deviation)))

    print("\nwould you like to continue?")
    cont = input("press y for yes, any other key for no: ")

    if cont.lower() not in "y" or cont in "":
        break
    print("\n")

# ^_^
