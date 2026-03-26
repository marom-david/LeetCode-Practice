class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operator = {'+', '-', '*', '/'}
        result = 0

        for t in range(len(tokens)):
            if tokens[t] not in operator:
                stack.append(int(tokens[t]))
            else:
                first_item = stack.pop()
                second_item = stack.pop()
                if tokens[t] == '+':
                    result = second_item + first_item
                elif tokens[t] == '-':
                    result = second_item - first_item
                elif tokens[t] == '*':
                    result = second_item * first_item
                elif tokens[t] == '/' and first_item != 0:
                    result = int(float(second_item) / first_item)
                stack.append(result)

        return stack.pop()