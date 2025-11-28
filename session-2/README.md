# 🐍 Session 2: Logic, Conditionals & Control Flow

## 1\. Comparison Operators (The Basis of Logic)

- **Concept:** Boolean Data Type (`True` / `False`)
- **Operators:**
  - `==` (Equal to)
  - `!=` (Not equal to)
  - `>` , `<` (Greater/Less than)
  - `>=`, `<=` (Greater/Less than or equal)

<!-- end list -->

```python
x = 10
y = 20

print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
```

---

## 2\. Logical Operators (Combining Conditions)

- **`and`**: Returns True if **both** statements are true.
- **`or`**: Returns True if **at least one** statement is true.
- **`not`**: Reverse the result.

<p align="center">
  <img src="logic-gate.jpeg" width="300">
</p>
<!-- end list -->

```python
is_sunny = True
have_money = False

# AND Example
print(is_sunny and have_money) # False

# OR Example
print(is_sunny or have_money)  # True

# NOT Example
print(not is_sunny)            # False
```

---

## 3\. Conditional Statements (If, Elif, Else)

- **Syntax:** Importance of the **Colon (`:`)** and **Indentation (Whitespace)**.
- **Flow:** Python checks from top to bottom. Stops at the first `True`.

### A. Basic `if`

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

### B. `if` ... `else`

```python
temperature = 5

if temperature > 20:
    print("It's a warm day.")
else:
    print("It's cold outside.")
```

### C. The `elif` Ladder (Multiple Conditions)

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F (Failed)")
```

---

## 4\. Nested Conditions (If inside If)

- **Concept:** Filtering data in layers.
- **Warning:** Avoid deep nesting (readability issues).

<!-- end list -->

```python
username = "admin"
password = "123"

if username == "admin":
    # User is found, now check password
    if password == "123":
        print("Login Successful!")
    else:
        print("Wrong Password.")
else:
    print("User not found.")
```

---

## 5\. Switch Cases (Match Case)

- **Version:** Python 3.10+ feature.
- **Use case:** Cleaner alternative to many `elif`s when checking a single variable.
- **`case _`**: Acts as the `default` or `else`.
- **`|` Operator:** Combine multiple cases.

<!-- end list -->

```python
status_code = 404

match status_code:
    case 200:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500 | 503:
        print("Server Error")
    case _:
        print("Unknown Status")
```

---

## 6\. Practical Task (Class Exercise)

**Scenario:** A simple Ticket Pricing System based on age.

- **Input:** User enters age.
- **Logic:**
  - `< 5`: Free
  - `5 - 18`: $10
  - `18 - 60`: $20
  - `> 60`: $15 (Senior Discount)
