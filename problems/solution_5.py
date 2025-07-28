# 🔐 Codeword with a Digit
# You are participating in a secret mission, and your task is to find a codeword that contains at least one digit. You are given a list of messages and must check them in order to find the required word.

# As soon as you find such a word (i.e., containing at least one digit), you must immediately print it so the mission commander can see it.

# If none of the messages contain a codeword with a digit, you must output:
# -Codeword not found

def func(messages):
    for word in messages:
        lst = list(word.split(' '))

        for i in lst:
            for j in i:
                if j.isdigit():
                    return i
    return 'Кодовое слово не найдено'
print(func(messages))
       
