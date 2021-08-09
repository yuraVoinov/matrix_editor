import random
from math import nan


class MatrixClass:
    matrix: list

    def __init__(self):
        self.matrix = []

    def to_string(self):
        matrix_string = ""
        for x in self.matrix:
            matrix_string += str(x) + "\n"
        return matrix_string

    def random_fill(self, rows, columns):
        self.matrix.clear()
        for x in range(1, rows + 1):
            row = []
            for j in range(1, columns + 1):
                row.append(random.randint(10, 99))
            self.matrix.append(row)

    def read_file(self):
        self.matrix.clear()
        matrix_file = input("Select file you would like to open: ")
        f = open(f"{matrix_file}", "r")
        for line in f:
            row = line.rstrip()
            row = row.split(' ')
            i = 0
            while i < len(row):
                row[i] = int(row[i])
                i += 1
            self.matrix.append(row)
        return self.matrix

    def matrix_print(self):
        for x in self.matrix:
            print(x)

    def find_max_element(self):
        if not self.matrix:
            return nan
        max_element = 0
        max_row_index = 0
        for x in self.matrix:
            max_row_element = max(x)
            row_index = self.matrix.index(x)
            if max_row_element > max_element:
                max_element = max_row_element
                max_row_index = row_index
        max_column_index = self.matrix[max_row_index].index(max_element)
        return max_element, max_row_index, max_column_index

    def max_row(self):
        if not self.matrix:
            return nan
        max_row_sum = 0
        max_row_index = 0
        for x in self.matrix:
            row_sum = sum(x)
            row_index = self.matrix.index(x)
            if row_sum > max_row_sum:
                max_row_sum = row_sum
                max_row_index = row_index
        return max_row_index, max_row_sum

    def max_column(self):
        if not self.matrix:
            return nan
        column_sum_list = []
        i = 0
        while i < len(self.matrix[0]):
            column_sum = 0
            for x in self.matrix:
                column_sum += x[i]
            i += 1
            column_sum_list.append(column_sum)
        return column_sum_list.index(max(column_sum_list)), max(column_sum_list)

    def swap_rows(self, first_row, second_row):
        if not self.matrix:
            return nan
        if first_row > len(self.matrix) or second_row > len(self.matrix):
            return None
        self.matrix[first_row - 1], self.matrix[second_row - 1] = self.matrix[second_row - 1], self.matrix[
            first_row - 1]
        return self.matrix

    def swap_columns(self, first_column, second_column):
        if not self.matrix:
            return nan
        if first_column > len(self.matrix[0]) or second_column > len(self.matrix[0]):
            return None
        for x in self.matrix:
            x[first_column - 1], x[second_column - 1] = x[second_column - 1], x[first_column - 1]
        return self.matrix

    def row_print(self, row_index):
        if not self.matrix:
            return nan
        if row_index > len(self.matrix):
            return None
        return self.matrix[row_index - 1]

    def column_print(self, column_index):
        if not self.matrix:
            return nan
        if column_index > len(self.matrix[0]):
            return None
        column = []
        for x in self.matrix:
            column.append(x[column_index - 1])
        return column
