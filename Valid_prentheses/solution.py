
def isValid(str):
        dict = {")":"(", "}":"{","]":"[" }
        stack = []
        for i in str:
            # if i is an closing bracket
            if i in dict:
                top_value = stack.pop() if stack else "#"
                if dict[i] != top_value:
                    return False
            else:
                stack.append(i)
                print(stack)
        if not stack:
            return True
        else:
            return False

print(isValid("]"))