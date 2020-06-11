from string import ascii_letters, digits
Total_mem_chars = 0
Total_chars = 0
string_line = ''
with open('Project8_2015', 'r') as file:
    for line in file:
        if '\n' in line:
            new_line_found = -1
        else:
            new_line_found = None
        new_line = line[:new_line_found]
        Total_chars += len(new_line)
        string_line = new_line.replace("\\", "\\\\")
        string_line = string_line.replace("\"", "\\\"")
        string_line = '"' + string_line + '"'
        # new_line = 'string_line = ' + line
        # exec(new_line)
        if string_line != '':
            Total_mem_chars += len(string_line)

print(Total_mem_chars)
print(Total_chars)
print(Total_mem_chars-Total_chars)
