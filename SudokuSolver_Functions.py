#!/usr/bin/env python3
# -*- coding: utf-8 -*-


basic_numbers_for_compare = (1, 2, 3, 4, 5, 6, 7, 8, 9)

def find_square(row_number, column_number):
    if (row_number < 3):
        if (column_number < 3):
            square_number = 0
        if (column_number >= 3 and column_number <= 5):
            square_number = 1
        if (column_number > 5):
            square_number = 2
    if (row_number >= 3 and row_number <= 5):
        if (column_number < 3):
            square_number = 3
        if (column_number >= 3 and column_number <= 5):
            square_number = 4
        if (column_number > 5):
            square_number = 5
    if (row_number > 5):
        if (column_number < 3):
            square_number = 6
        if (column_number >= 3 and column_number <= 5):
            square_number = 7
        if (column_number > 5):
            square_number = 8        
    return(square_number)


def find_square_position(row_number, column_number):
    if (row_number == 0 or row_number == 3 or row_number == 6):
        if (column_number == 0 or column_number == 3 or column_number == 6):
            square_position = 0
        if (column_number == 1 or column_number == 4 or column_number == 7):
            square_position = 1
        if (column_number == 2 or column_number == 5 or column_number == 8):
            square_position = 2
    if (row_number == 1 or row_number == 4 or row_number == 7):
        if (column_number == 0 or column_number == 3 or column_number == 6):
            square_position = 3
        if (column_number == 1 or column_number == 4 or column_number == 7):
            square_position = 4
        if (column_number == 2 or column_number == 5 or column_number == 8):
            square_position = 5
    if (row_number == 2 or row_number == 5 or row_number == 8):
        if (column_number == 0 or column_number == 3 or column_number == 6):
            square_position = 6
        if (column_number == 1 or column_number == 4 or column_number == 7):
            square_position = 7
        if (column_number == 2 or column_number == 5 or column_number == 8):
            square_position = 8
    return(square_position)


def missing_number_list(row):
    missing_in_list = set()
    for i in basic_numbers_for_compare:
        s = i in row
        if (s == False):
            missing_in_list.add(i)
    return(missing_in_list)


def update_lists(list_of_rows, list_of_columns, list_of_squares, row_number, column_number, square_number, set_number):
    square_position = -1
    found_one = True
    number = list(set_number)
    list_of_rows[row_number][column_number] = number[0]
    list_of_columns[column_number][row_number] = number[0]
    square_position = find_square_position(row_number, column_number)
    list_of_squares[square_number][square_position] = number[0]
    return(found_one)


def print_by_row(list_of_rows):
    s = "=====================\n"
    m = 1
    for i in list_of_rows:
        n = 0
        while (n < 9):
            if (i[n] == 0):
                s += "|" + " "
            else:
                s += "|" + str(i[n])
            n += 1
            if (n == 3 or n == 6 or n == 9):
                s += "|"
        s += "\n"
        if (m == 3 or m == 6):
            s += "=====================\n"#"---------------------\n"
        m += 1
    s += "=====================\n"
    print(s)