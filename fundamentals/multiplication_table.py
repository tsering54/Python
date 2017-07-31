print ' x 1 2 3 4 5 6 7 8 9 10 11 12'

for row in range(1, 12+1):
    display_string = ''
    for column in range(0, 12+1):
        if column is 0:
            display_string += '' + str(row)
        else:
            display_string += '' + str(column * row)
    print display_string
