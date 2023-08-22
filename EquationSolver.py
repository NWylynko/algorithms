
# You are going to write a program that can take a string representing a mathematical
# equation in infix form and solve it by converting it into postfix and then evaluating the
# postfix.

from Stack import DSAStack
from ShufflingQueue import DSAShufflingQueue


class EquationSolver:
    def __init__(self):
        pass

    def solve(self, equation):
        # solve the equation
        # return the answer

        postfix = self._parseInfixToPostfix(equation)
        answer = self._evaluatePostfix(postfix)
        return answer

    def _parseInfixToPostfix(self, equation: str):
        # convert the equation to postfix
        # return the postfix equation

        stack = DSAStack(20)
        queue = DSAShufflingQueue(20)

        for token in equation.split(" "):
            if token.isdigit():
                queue.enqueue(token)
            elif token == "(":
                stack.push(token)
            elif token == ")":
                while stack.peek() != "(":
                    queue.enqueue(stack.pop())
                stack.pop()
            elif token in "+-*/^":
                while not stack.isEmpty() and self._precedenceOf(token) <= self._precedenceOf(stack.peek()):
                    queue.enqueue(stack.pop())
                stack.push(token)
            else:
                raise ValueError("Invalid token: " + token)

        while not stack.isEmpty():
            queue.enqueue(stack.pop())

        return queue

    def _evaluatePostfix(self, postfix):
        # evaluate the postfix equation
        # return the answer

        stack = DSAStack(20)

        while not postfix.isEmpty():
            token = postfix.dequeue()
            if token.isdigit():
                stack.push(token)
            elif token in "+-*/^":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self._executeOperation(token, operand1, operand2)
                stack.push(result)
            else:
                raise ValueError("Invalid token: " + token)

        return stack.pop()

    def _precedenceOf(self, operator):
        # return the precedence of the operator

        if operator == "^":
            return 4
        elif operator in "*/":
            return 3
        elif operator in "+-":
            return 2
        elif operator == "(":
            return 1
        else:
            raise ValueError("Invalid operator: " + operator)

    def _executeOperation(self, operator, operand1, operand2):
        # evaluate the operator with the operands
        # return the result

        if operator == "^":
            return int(operand1) ** int(operand2)
        elif operator == "*":
            return int(operand1) * int(operand2)
        elif operator == "/":
            return int(operand1) / int(operand2)
        elif operator == "+":
            return int(operand1) + int(operand2)
        elif operator == "-":
            return int(operand1) - int(operand2)
        else:
            raise ValueError("Invalid operator: " + operator)


# test the equation solver
if __name__ == "__main__":
    solver = EquationSolver()
    assert solver.solve("1 + 2") == 3
    assert solver.solve("1 + 2 * 3") == 7
    assert solver.solve("1 + 2 * 3 + 4") == 11
    assert solver.solve("1 + ( 2 * 3 ) + ( 4 * 5 )") == 27
    print(solver._parseInfixToPostfix("1 + ( 2 * 3 ) + ( 4 * 5 )")._queue)
    assert solver.solve("1 + 2 * 3 + 4 * 5 ^ 6") == 62507
    assert solver.solve("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3") == 3
    assert solver.solve("3 + 5 * 2 / ( 1 - 2 ) ^ 6 ^ 3") == 13
    print("All tests passed")
