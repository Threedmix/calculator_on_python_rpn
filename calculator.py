input = input() 
output = []
stack = []
op = {'+':1, '-':1, '*':2, '/':2}
i = 0
while i < len(input):
    c = input[i]
    if c in '0123456789':
        num = []
        while i < len(input) and input[i] in '0123456789':
            num.append(input[i])
            i += 1
        output.append(''.join(num))
        continue
    elif c in '+-*/':
        while len(stack) != 0 and op.get(stack[-1], 0) >= op[c] and stack[-1] != '(':
            output.append(stack.pop())
        stack.append(c)
    elif c == '(':
        stack.append(c)
    elif c == ')':
        while len(stack) != 0 and stack[-1] != '(': 
            output.append(stack.pop())
        if len(stack) != 0 and stack[-1] == '(':
            stack.pop()
    i += 1

while len(stack) != 0:
    output.append(stack.pop())

res = []
for c in output:
    if c in '+-*/':
        l1 = res.pop()
        l2 = res.pop()
        if c == '+':
            res.append(l2 + l1)
        elif c == '-':
            res.append(l2 - l1)
        elif c == '*':
            res.append(l2 * l1)
        elif c == '/':
            res.append(l2 / l1)    
    else:
        res.append(int(c))
print(res[0])
