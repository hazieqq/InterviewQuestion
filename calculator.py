import sys
import math

sys.argv.pop(0)
arr = sys.argv

stack = []
digit = []
total = 0
check = True
counter = 0
for i in range(len(arr)):
    try:
        if not arr[i].isdigit():
            stack.append(arr[i])
            counter += 1
        else:
            stack.append(arr[i])
            if counter == 1:
                while(stack):
                    print(stack)
                    first = stack.pop(0)
                    if first == '+':
                        digit.append(stack.pop(0))
                        while(digit):
                            total+=int(digit.pop())
                    elif first == '-':
                        digit.append(stack.pop(0))
                        while(digit):
                            if check:
                                total = int(digit.pop(0))
                                check = False
                            else:
                                total = total - int(digit.pop(0))
                    elif first == '*':
                        digit.append(stack.pop(0))
                        while(digit):
                            if check:
                                total = int(digit.pop(0))
                                check = False
                            else:
                                total = total * int(digit.pop(0))
                    elif first == '/':
                        digit.append(stack.pop(0))
                        while(digit):
                            if check:
                                total = int(digit.pop(0))
                                check = False
                            else:
                                total = total / int(digit.pop(0))
                    else:
                        digit.append(first)
                counter = 0
    except Exception as e:
        print("MATH ERROR")
        quit()
    
print(total)