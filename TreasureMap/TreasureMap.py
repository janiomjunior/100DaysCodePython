row_column = input("Enter with row and column, ex: 23, 12: ")
vertical = int(row_column[0])
horizontal = int(row_column[1])
row1 = ['a', 'b', 'c']
row2 = ['d', 'e', 'f']
row3 = ['g', 'h', 'i']
map = [row1, row2, row3]

print(map[vertical-1][horizontal-1])


