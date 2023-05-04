# You are given a string 'S' of length 'N' representing an arithmetic expression. Your task is to compute the result of the expression.
# Note: remove all the imports else it will show error

def calculator(s, n):
    # write your code here
    stack = []
    sign = '+'
    num = 0
    for i in range(n):
        c = s[i]
        if c.isdigit():
            num = num*10+int(c)
        if i + 1 == len(s) or (c == '+' or c == '-' or c == '*' or c == '/'):
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] = stack[-1]*num
            elif sign == '/':
                stack[-1] = stack[-1]/float(num)
            sign = c
            num = 0
    return sum(stack)