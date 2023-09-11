def pascals_triangle(numRows):
    return_list = [[1]]
    previous_list = []
    for row_number in range(2, numRows+1):

        row = []
        row.append(1)
        for item in range(len(return_list[row_number-2])-1):
            row.append(return_list[row_number-2][item]+return_list[row_number-2][item+1])

        row.append(1)
        return_list.append(row)
    return return_list

if __name__ == "__main__":
    output_list = pascals_triangle(5)
    print(output_list)
    print()