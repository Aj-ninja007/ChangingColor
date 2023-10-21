
def evalpost(s):
    stack=[]
    for i in s:
        if i not in ['^','*','/','+','-','(',')']:
            stack.append(i)
        else:
            a=stack.pop()
            b=stack.pop()
            stack.append(f'({b}{i}{a})')
    return stack[-1]
t="ab+cd+*"
print(evalpost(t))




