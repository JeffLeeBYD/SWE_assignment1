from pickle import TRUE
from xmlrpc.client import boolean


def calculate(s: str) -> int:
    marks = {"+", "-", "*"}
    stack = []                      # stack
    now_num = ""                    # current
    last_mark = "+"                 # set default 
    for ch in s + "+":              # append a meaning-less mark in the end to calculate the last number with last_mark
        if ch.isdigit():
            now_num += ch
        elif ch in marks:
            num = int(now_num)      # calculate the current number read in with last operation mark
            if last_mark == "+":
                stack.append(num)   # if the last operation mark is +, we add the number into stack
            elif last_mark == "-":
                stack.append(-num)  # if the last operation mark is -, we add the negated number into stack
            elif last_mark == "*":  # only push number into stack when meeting + or - for final addition
                stack[-1] *= num    # if * is the last operand, multiply the last element in stack with the current number immediately
            now_num = ""
            last_mark = ch
    return sum(stack)               # do final addition

def valid(s: str) -> boolean:
    is_operator = True
    contain_operator = False
    for ch in s:
        if ch.isdigit():
            is_operator = False
        elif ch == '+' or ch == '-' or ch == '*':
            contain_operator = True
            if is_operator:
                return False
            is_operator = True
        else:
            return False
    if not contain_operator:
        return False
    if is_operator:
        return False
    return True

        

if __name__ == '__main__':
    user_in = input("Enter the expression: ")
    
    print (calculate("2+8*2"))