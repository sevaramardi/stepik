# 🎟️ Cinema Seating Chart
# You are working on a seat reservation management system for a cinema. You are given a list of booked seats, and your task is to display the seating layout, where:

# The English letter "X" indicates a booked seat;

# The English letter "O" indicates a free seat.

# ✅ The program must:
# Process a list named booked, which contains strings in the format "Р.<row>, М.<seat>" (note: Р and М are Cyrillic letters, representing "row" and "seat", respectively);

# Display the seating layout on the screen as follows:

# The cinema has 5 rows;

# Each row has 10 seats;

# If a seat is booked, its position in the layout should show "X"; otherwise, it should show "O";

# Seats should be separated by spaces in the output;

# You do not need to read input — the variable booked is already defined in the program.

#booked
lst = []

for i in range(1,6):
    new = []
    for j in range(1,11):
        new.append('O')
    new1 = new.copy()
    lst.append(new1)
    
if len(booked) > 0:
    for i in range(0,5):
        lst1 = list(booked[i].split(','))
        lst[int(lst1[0][2])-1][int(lst1[1][3:])-1] = 'X'

for i in range(0, 5):
    print(' '.join(lst[i]))
        




