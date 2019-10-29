expression = input().split()
operators = ['plus', 'minus', 'multiply', 'divide']
if expression[1] == operators[0]:
    print(int(expression[0]) + int(expression[2]))
elif expression[1] == operators[1]:
    print(int(expression[0]) - int(expression[2]))
elif expression[1] == operators[2]:
    print(int(expression[0]) * int(expression[2]))
elif expression[1] == operators[3]:
    print(int(expression[0]) // int(expression[2]))
