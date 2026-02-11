#Question -> https://neetcode.io/problems/evaluate-reverse-polish-notation/question
#Time Complexity: O(n)
#Space Complexity: O(n)
def evalRPN(tokens: list[str]) -> int:

    operators = {'+', '-', '*', '/'}
    new_value = 0
    stack = []

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            if stack:
                if token == '+':
                    first_value = stack.pop()
                    second_value = stack.pop()
                    new_value = second_value + first_value
                    stack.append(new_value)
                elif token == '*':
                    first_value = stack.pop()
                    second_value = stack.pop()
                    new_value = second_value * first_value
                    stack.append(new_value)
                elif token == '-':
                    first_value = stack.pop()
                    second_value = stack.pop()
                    new_value = second_value - first_value
                    stack.append(new_value)
                elif token == '/':
                    first_value = stack.pop()
                    second_value = stack.pop()
                    new_value = int(second_value / first_value)
                    stack.append(new_value)
                
    return stack.pop()
                
print(evalRPN(tokens=["1","2","+","3","*","4","-"]))