table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
    ["dogs", "cats", "moose", "goose"],
]


def print_table(table):

    col_widths = []
    for list in table:  # longest element
        col_widths.append(len(max(list, key=len)))

    for i in range(len(table[0])):
        for j in range(len(table)):
            line = table[j][i]
            print(line.rjust(max(col_widths)), end=" ")
        print()


print_table(table_data)
