#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import SudokuSolver_Functions as Susolv


full_sudoku_list = [0, 3, 0, 4, 0, 0, 0, 6, 0, \
                    0, 0, 0, 9, 1, 0, 0, 0, 0, \
                    2, 0, 5, 0, 8, 0, 0, 9, 7, \
                    0, 9, 7, 0, 3, 2, 0, 0, 5, \
                    5, 0, 3, 0, 0, 4, 0, 0, 0, \
                    1, 0, 0, 5, 9, 8, 7, 3, 0, \
                    0, 6, 0, 3, 0, 0, 0, 0, 0, \
                    0, 0, 4, 0, 7, 1, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 4, 0, 0]	

    
class SuBoard():
    def __init__(self):
        self.row_1_list = [0] * 9
        self.row_2_list = [0] * 9
        self.row_3_list = [0] * 9
        self.row_4_list = [0] * 9
        self.row_5_list = [0] * 9
        self.row_6_list = [0] * 9
        self.row_7_list = [0] * 9
        self.row_8_list = [0] * 9
        self.row_9_list = [0] * 9
        self.list_of_rows = [self.row_1_list, self.row_2_list, self.row_3_list, self.row_4_list, self.row_5_list, self.row_6_list, self.row_7_list, \
                self.row_8_list, self.row_9_list]

        self.column_1_list = [0] * 9
        self.column_2_list = [0] * 9
        self.column_3_list = [0] * 9
        self.column_4_list = [0] * 9
        self.column_5_list = [0] * 9
        self.column_6_list = [0] * 9
        self.column_7_list = [0] * 9
        self.column_8_list = [0] * 9
        self.column_9_list = [0] * 9
        self.list_of_columns = [self.column_1_list, self.column_2_list, self.column_3_list, self.column_4_list, self.column_5_list, \
                           self.column_6_list, self.column_7_list, self.column_8_list, self.column_9_list]
        
        self.square_1_list = [0] * 9
        self.square_2_list = [0] * 9
        self.square_3_list = [0] * 9
        self.square_4_list = [0] * 9
        self.square_5_list = [0] * 9
        self.square_6_list = [0] * 9
        self.square_7_list = [0] * 9
        self.square_8_list = [0] * 9
        self.square_9_list = [0] * 9
        self.list_of_squares = [self.square_1_list, self.square_2_list, self.square_3_list, self.square_4_list, self.square_5_list, \
                           self.square_6_list, self.square_7_list, self.square_8_list, self.square_9_list]

        self.all_full = False


def pull_lists_from_full(field):
    #set rows
    n = 0
    m = 0
    for i in full_sudoku_list:
        field.list_of_rows[n][m] = i
        m += 1
        if(m > 8):
            m = 0
            n += 1
    #set columns
    n = 0
    m = 0
    for i in full_sudoku_list:
        field.list_of_columns[n][m] = i
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
        field.list_of_squares[n][m] = i
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


def begin(field, found_one):
    n = 0
    row_number = 0
    column_number = 0
    square_number = 0
    missing_in_row = set()
    missing_in_column = set()
    missing_in_square = set()
    missing_comparison = set()
    for row in field.list_of_rows:    
        column_number = 0
        while(column_number < 9):
            if (row[column_number] == 0):
                #global all_full
                field.all_full = False
                square_number = Susolv.find_square(row_number, column_number)
                missing_in_row = Susolv.missing_number_list(row)
                #1st check to update list for this position (row only)
                if (len(missing_in_row) == 1):
                    found_one = Susolv.update_lists(field.list_of_rows, field.list_of_columns, field.list_of_squares, \
                                                    row_number, column_number, square_number, missing_in_row)
                else:                   
                    #2nd check to update list for this position (row and column)
                    missing_in_column = Susolv.missing_number_list(field.list_of_columns[column_number])
                    missing_comparison = missing_in_row.intersection(missing_in_column)
                    if (len(missing_comparison) == 1):
                        found_one = Susolv.update_lists(field.list_of_rows, field.list_of_columns, field.list_of_squares, \
                                                        row_number, column_number, square_number, missing_comparison)
                    else:
                        #last check to update list for this position (row, column, and square)
                        missing_in_square = Susolv.missing_number_list(field.list_of_squares[square_number])
                        missing_comparison = missing_comparison.intersection(missing_in_square)
                        if (len(missing_comparison) == 1):
                            found_one = Susolv.update_lists(field.list_of_rows, field.list_of_columns, field.list_of_squares, \
                                                            row_number, column_number, square_number, missing_comparison)
            column_number += 1
            n += 1
        row_number += 1
    return(found_one)
                    
 
def main_running_loop():
    field = SuBoard()
    pull_lists_from_full(field)
    found_one = True
    field.all_full
    while (found_one):
        field.all_full = True
        found_one = False
        found_one = begin(field, found_one)
    Susolv.print_by_row(field.list_of_rows)
    if (field.all_full == True):
        print("Puzzle done.")
    elif (found_one == False):
        print("Puzzle could not be completed.")


main_running_loop()
