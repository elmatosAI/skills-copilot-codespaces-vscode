<header>
## Examples in Python to Test Copilot

I have created two examples in Python to test the capabilities of GitHub Copilot. These examples demonstrate how Copilot can assist in writing Python code by providing autocomplete-style suggestions.

### Example 1: Basic Arithmetic Operations

In this example, we will create a Python function to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

1. Create a new file named `arithmetic.py`.
2. Define a function named `calculate` that takes two numbers and an operator as arguments.
3. Use Copilot to generate the function body.

```python
def calculate(num1, num2, operator):
   if operator == '+':
      return num1 + num2
   elif operator == '-':
      return num1 - num2
   elif operator == '*':
      return num1 * num2
   elif operator == '/':
      return num1 / num2
   else:
      return "Invalid operator"
```

### Example 2: Fibonacci Sequence

In this example, we will create a Python function to generate the Fibonacci sequence up to a specified number of terms.

1. Create a new file named `fibonacci.py`.
2. Define a function named `fibonacci` that takes the number of terms as an argument.
3. Use Copilot to generate the function body.

```python
def fibonacci(n):
   sequence = []
   a, b = 0, 1
   while len(sequence) < n:
      sequence.append(a)
      a, b = b, a + b
   return sequence
```

These examples showcase how GitHub Copilot can help streamline the coding process by providing intelligent suggestions and completing code snippets.
