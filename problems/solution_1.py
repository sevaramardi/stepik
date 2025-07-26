# ♟️ Chessboard
# You need to create a chessboard of size n × n, using the character X to represent black squares and O to represent white squares.
# Even-indexed cells should be marked as X, and odd-indexed cells as O;
# The color pattern should alternate, just like on a real chessboard;
# The first cell of the first row must always be X.

# ✅ Write a program that:
# Accepts an integer n (the size of the chessboard);
# Uses nested loops to generate the board;
# Outputs the board as a square template, alternating X and O.

n = int(input())
for i in range(0,n):
    for j in range(0, n):
        if i%2 == 0 or i == 0:
            if j%2 == 0 or j == 0:
                print('X', end=' ')
            else:
                print('O', end= ' ')
        else:
            if j%2 == 0 or j == 0:
                print('O', end=' ')
            else:
                print('X', end= ' ')
            
    print()

#output for n=5
# X O X O X 
# O X O X O 
# X O X O X 
# O X O X O 
# X O X O X 
