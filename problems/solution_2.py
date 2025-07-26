# 🌟 Task: Horizontal Bar Chart with Asterisks
# 📥 Input Format:
# A single line containing several natural numbers (positive integers).

# 📤 Output Format:
# Each number is represented on a separate line by that many asterisks *.
lst = list(map(int,input().split()))
for i in lst:
    print(i*'*')
