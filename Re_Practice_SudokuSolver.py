#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import SudokuSolver_Functions as Susolv


row_1_list = [0] * 9
row_2_list = [0] * 9
row_3_list = [0] * 9
row_4_list = [0] * 9
row_5_list = [0] * 9
row_6_list = [0] * 9
row_7_list = [0] * 9
row_8_list = [0] * 9
row_9_list = [0] * 9
list_of_rows = [row_1_list, row_2_list, row_3_list, row_4_list, row_5_list, row_6_list, row_7_list, \
                row_8_list, row_9_list]

column_1_list = [0] * 9
column_2_list = [0] * 9
column_3_list = [0] * 9
column_4_list = [0] * 9
column_5_list = [0] * 9
column_6_list = [0] * 9
column_7_list = [0] * 9
column_8_list = [0] * 9
column_9_list = [0] * 9
list_of_columns = [column_1_list, column_2_list, column_3_list, column_4_list, column_5_list, \
                   column_6_list, column_7_list, column_8_list, column_9_list]

square_1_list = [0] * 9
square_2_list = [0] * 9
square_3_list = [0] * 9
square_4_list = [0] * 9
square_5_list = [0] * 9
square_6_list = [0] * 9
square_7_list = [0] * 9
square_8_list = [0] * 9
square_9_list = [0] * 9
list_of_squares = [square_1_list, square_2_list, square_3_list, square_4_list, square_5_list, \
                   square_6_list, square_7_list, square_8_list, square_9_list]

all_full = False


full_sudoku_list = [0, 3, 0, 4, 0, 0, 0, 6, 0, \
                    0, 0, 0, 9, 1, 0, 0, 0, 0, \
                    2, 0, 5, 0, 8, 0, 0, 9, 7, \
                    0, 9, 7, 0, 3, 2, 0, 0, 5, \
                    5, 0, 3, 0, 0, 4, 0, 0, 0, \
                    1, 0, 0, 5, 9, 8, 7, 3, 0, \
                    0, 6, 0, 3, 0, 0, 0, 0, 0, \
                    0, 0, 4, 0, 7, 1, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 4, 0, 0]	
    

def pull_lists_from_full():
    #set rows
    n = 0
    m = 0
    for i in full_sudoku_list:
        list_of_rows[n][m] = i
        m += 1
        if(m > 8):
            m = 0
            n += 1
    #set columns
    n = 0
    m = 0
    for i in full_sudoku_list:
        list_of_columns[n][m] = i
        n += 1
        if(n > 8):
            n = 0
            m += 1
    #set squares
    n = 0
    m = 0
    hor_wrap = 3
    vert_wrap = 3
    for i in full_sudoku_list:
        list_of_squares[n][m] = i
        m += 1
        if(m >= hor_wrap):
            n += 1
            m = -3 + hor_wrap
        if(n >= vert_wrap):
            n = -3 + vert_wrap
            m = hor_wrap
            hor_wrap += 3
        if(hor_wrap > 9):
            m = 0
            n = vert_wrap
            hor_wrap = 3
            vert_wrap += 3


def begin(found_one):
    n = 0
    row_number = 0
    column_number = 0
    square_number = 0
    missing_in_row = set()
    missing_in_column = set()
    missing_in_square = set()
    missing_comparison = set()
    for row in list_of_rows:    
        column_number = 0
        while(column_number < 9):
            if (row[column_number] == 0):
                global all_full
                all_full = False
                square_number = Susolv.find_square(row_number, column_number)
                missing_in_row = Susolv.missing_number_list(row)
                #1st check to update list for this position (row only)
                if (len(missing_in_row) == 1):
                    found_one = Susolv.update_lists(list_of_rows, list_of_columns, list_of_squares, row_number, column_number, square_number, missing_in_row)
                else:                   
                    #2nd check to update list for this position (row and column)
                    missing_in_column = Susolv.missing_number_list(list_of_columns[column_number])
                    missing_comparison = missing_in_row.intersection(missing_in_column)
                    if (len(missing_comparison) == 1):
                        found_one = Susolv.update_lists(list_of_rows, list_of_columns, list_of_squares, row_number, column_number, square_number, \
                                                 missing_comparison)
                    else:
                        #last check to update list for this position (row, column, and square)
                        missing_in_square = Susolv.missing_number_list(list_of_squares[square_number])
                        missing_comparison = missing_comparison.intersection(missing_in_square)
                        if (len(missing_comparison) == 1):
                            found_one = Susolv.update_lists(list_of_rows, list_of_columns, list_of_squares, row_number, column_number, square_number, \
                                                     missing_comparison)
            column_number += 1
            n += 1
        row_number += 1
    return(found_one)
                    
 
def main_running_loop():
    pull_lists_from_full()
    found_one = True
    global all_full
    while (found_one):
        all_full = True
        found_one = False
        found_one = begin(found_one)
    Susolv.print_by_row(list_of_rows)
    if (all_full == True):
        print("Puzzle done.")
    elif (found_one == False):
        print("Puzzle could not be completed.")


main_running_loop()
