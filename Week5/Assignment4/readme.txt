Tavish Peckham
Data Structures Spring 2018
Assignment 4 Readme

Question 1: Scale by
    Multiplies each index of matrix self by a scalar passed as an argument.

Question 2: Transpose
    Creates a new matrix with the given matrix's rows and columns reversed.
    Sets each value (i, j) of the new matrix to the corresponding inverse
    value (j, i) of the passed matrix.

Question 3: Add
    Creates a new matrix with the same dimensions of the matrices passed as
    arguments. Sets the value of each element of the new matrix (i, j) to the
    sum of the corresponding elements (i, j) of the two passed matrices.

Question 4: Subtract
    Creates a new matrix with the same dimensions of the matrices passed as
    arguments. Sets the value of each element of the new matrix (i, j) to the
    difference between the corresponding elements (i, j) of the two passed
    matrices.

Question 5: Multiply
    Creates a new matrix with the row dimension of the first matrix and the
    column dimension of the second matrix. Then iterates through three ranges
    M, N, O where M is the first matrix's row length, N is the second matrix's
    column length, and O is the same between the first matrix's column length
    and the second matrix's row length. We then assign to the element at
    coordinate (M, N) of the new matrix the sum of its current value (if any)
    and the product of the elements of the first matrix's coordinates (M, O)
    and the second matrix's coordinates (O, N). By the end of the sequence,
    each coordinate of the new matrix should come as the sum of two products,
    each produced from a single iteration.
