


def moveBracks(string):
    stack = []
    for i in string:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
        
    answer =  len(stack)//2
    print(answer)
    return answer

moveBracks(")(()")
moveBracks("()()")
moveBracks(")(")
moveBracks(")))(((")
            
