with open('test.csv', 'r') as input_file, open('test_formatted.csv', 'w') as output_file:
    # Iterate over each line in the input file
    for line in input_file:
        # Remove the last character from the line and write it to the output file
        output_file.write(line.rstrip('\n')[:-1] + '\n')