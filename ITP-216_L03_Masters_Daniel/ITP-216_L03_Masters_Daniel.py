#ITP 216 Lab 3
# Name: Daniel Masters
# Email: damaster@usc.edu


# 1. file_read_header()
    # a. Description: Retrieves the first line from a text file.
    # b. Parameters: 1
        # i. File name (string)
    # c. Returns: 1
        # i. The first line of the file (String)
def file_read_header(file_name):
    f_in = open(file_name, 'r')
    header = f_in.readline()
    f_in.close()
    return header

# 2. file_read_data()
    # a. Description: Retrieves all data from a text file except the first line.
    # b. Parameters: 1
        # i. File name (String)
    # c. Returns: 1
        # i. All the data from the file except for the first line (list)
def file_read_data(file_name):
    with open(file_name, 'r') as f_in:
        line_list = f_in.readlines()
    return line_list[1:]


# 3. main()
    # a. Description: Primary entrypoint to your codebase.
    # b. Parameters: 0
    # c. Returns: 0
def main():
    # d. Loads the contents of the file into two variables by calling their respective functions.
    my_file_name = "oscar_age_female.csv"
    first_line = file_read_header(file_name=my_file_name)
    # Then prints the header
    print("Header:", "\n\t", first_line)
    # print(rest_of_data)
    rest_of_data = file_read_data(my_file_name)
    print("Data:")
    # iterates through (item by item) and prints the rest of the data.
    for line in rest_of_data:
        print("\t", line, end="")

if __name__ == '__main__':
    main()