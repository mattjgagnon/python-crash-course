filename = 'pi_digits.txt'

# read entire file and output
# with open(filename) as file_object:
#     contents = file_object.read()

# print(contents)

# read line by line

with open(filename) as file_object:
    for line in file_object:
        # invisible newlines printed with this
        # print(line)

        # rstrip removes them
        print(line.rstrip())

    # store the lines in a list for later use
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
