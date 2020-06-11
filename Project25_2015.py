# Enter the code at row 3010, column 3019.
# paused until I complete the rest of the challenges! ~stink face~
multiplier = 252533
divisor = 33554393
end_row = 3010
end_column = 3019
start_code = 20151125
row = 1
max_row = 1
column = 1

next_code = 0
previous_code = start_code
match_found = False
while not match_found:
    if row == 1:
        max_row += 1
        row = max_row
        column = 1
    else:
        row -= 1
        column += 1
    next_code = previous_code*multiplier % divisor

    if row == end_row and column == end_column:
        print(next_code)
        match_found = True
    previous_code = next_code

