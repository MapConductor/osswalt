Of course! Here is a high-quality SDK document for the given code snippet, formatted in Markdown.

---

## `calculate_sum()`

The `calculate_sum` function computes the sum of two integer values. It provides a simple and direct way to perform addition.

```python
def calculate_sum(a: int, b: int) -> int:
```

### Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `a` | `int` | The first integer to be added. |
| `b` | `int` | The second integer to be added. |

### Returns

- `int`: The integer result of the addition `a + b`.

### Example

Here is a basic example of how to use the `calculate_sum` function.

```python
# Import the function (assuming it's in a module named 'math_utils')
# from math_utils import calculate_sum

# Define the function for a standalone example
def calculate_sum(a: int, b: int) -> int:
    """
    Calculates the sum of two integers.
    """
    return a + b

# --- Usage ---

# Define two numbers
num1 = 15
num2 = 27

# Call the function to calculate their sum
total = calculate_sum(num1, num2)

# Print the result
print(f"The sum of {num1} and {num2} is: {total}")

# Expected output:
# The sum of 15 and 27 is: 42
```