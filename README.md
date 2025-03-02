<header>
## Examples in Python to Test Copilot

I have created two examples in Python to test the capabilities of GitHub Copilot. These examples demonstrate how Copilot can assist in writing Python code by providing autocomplete-style suggestions.

### Example 1: Prime Number Check

In this example, we will create a Python function to check if a number is prime.

1. Create a new file named `numbers_1.py`.
2. Define a function named `is_prime` that takes a number as an argument.
3. Use Copilot to generate the function body.

```python
def is_prime(n):
   if n <= 1:
      return False
   for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
         return False
   return True
```

### Example 2: Sum of Digits

In this example, we will create a Python function to calculate the sum of digits of a number.

1. Create a new file named `numbers_2.py`.
2. Define a function named `sum_of_digits` that takes a number as an argument.
3. Use Copilot to generate the function body.

```python
def sum_of_digits(n):
   total = 0
   while n > 0:
      total += n % 10
      n //= 10
   return total
```

These examples showcase how GitHub Copilot can help streamline the coding process by providing intelligent suggestions and completing code snippets.
