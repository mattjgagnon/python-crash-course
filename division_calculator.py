while True:
    first_number = input("\nFirst number: ")

    if first_number == 'q':
        break

    second_number = input("\nSecond number: ")

    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
