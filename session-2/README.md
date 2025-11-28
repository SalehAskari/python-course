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

---

# 🧠 چالش‌های برنامه‌نویسی: منطق و شرط‌ها

### ۱. تحلیل‌گر مثلث (Triangle Analyzer)

**هدف:** کار با عملگرهای مقایسه‌ای و شرط‌های تودرتو.
سه عدد به عنوان طول اضلاع مثلث از کاربر بگیرید ($a, b, c$). برنامه باید دو مرحله بررسی انجام دهد:

1.  **آیا اصلاً مثلث تشکیل می‌شود؟** (قانون: مجموع هر دو ضلع باید از ضلع سوم بزرگتر باشد: $a+b > c$ و...). اگر نشد، چاپ کند `Invalid Triangle`.
2.  اگر مثلث معتبر بود، نوع آن را مشخص کند:
    - **متساوی‌الاضلاع:** هر سه ضلع برابر (`Equilateral`)
    - **متساوی‌الساقین:** دو ضلع برابر (`Isosceles`)
    - **مختلف‌الاضلاع:** هیچ ضلعی برابر نیست (`Scalene`)

**مثال خروجی:**

```text
Enter side A: 5
Enter side B: 5
Enter side C: 8
Result: It is a valid Isosceles triangle.
```

---

### ۲. سیستم تخفیف فروشگاه زنجیره‌ای (Advanced Discount System)

**هدف:** اولویت‌بندی شرط‌ها (elif) و متغیرهای بولی.
برنامه‌ای بنویسید که مبلغ خرید (`amount`) و وضعیت عضویت (`is_member`) را بگیرد.
قوانین محاسبه قیمت نهایی:

1.  اگر مبلغ بالای ۲۰۰ دلار باشد **و** عضو باشد: ۲۰٪ تخفیف.
2.  اگر مبلغ بالای ۲۰۰ دلار باشد **و** عضو نباشد: ۱۰٪ تخفیف.
3.  اگر مبلغ بین ۱۰۰ تا ۲۰۰ دلار باشد (عضویت مهم نیست): ۵٪ تخفیف.
4.  اگر زیر ۱۰۰ دلار باشد: هیچ تخفیفی ندارد.
    **نکته انحرافی:** اگر مبلغ بالای ۵۰۰ دلار باشد، فارغ از عضویت، یک `Special Gift` هم باید در خط جداگانه چاپ شود.

**مثال خروجی:**

```text
Enter amount: 600
Are you a member (True/False)? True
Final Price: 480.0
Message: You get a Special Gift!
```

---

### ۳. سال کبیسه و قرن (Leap Year Logic)

**هدف:** درک عمیق عملگرهای `and`، `or` و باقی‌مانده تقسیم `%`.
یک سال میلادی را دریافت کنید و تشخیص دهید آیا کبیسه (Leap Year) است یا خیر.
**قانون پیچیده ریاضی:**

- سال باید بر ۴ بخش‌پذیر باشد.
- **اما** اگر بر ۱۰۰ بخش‌پذیر بود، کبیسه **نیست**.
- **مگر اینکه** بر ۴۰۰ هم بخش‌پذیر باشد (که در این صورت باز هم کبیسه **است**).
  _(مثلا ۱۹۰۰ کبیسه نیست، اما ۲۰۰۰ کبیسه است)._

**مثال خروجی:**

```text
Enter year: 1900
Result: Not a Leap Year.
```

---

### ۴. سیستم احراز هویت امنیتی (Nested Security Check)

**هدف:** تمرین `if` های تودرتو (Nested) و `not`.
برنامه‌ای برای ورود به یک سیستم محرمانه بنویسید. ورودی‌ها: `username`, `password`, `is_banned` (آیا کاربر مسدود است؟).
مراحل چک کردن (به ترتیب):

1.  اگر کاربر مسدود است (`is_banned` برابر True): بلافاصله چاپ کند `Account Locked` (حتی اگر رمز درست باشد).
2.  اگر نام کاربری "admin" نیست: چاپ کند `User Not Found`.
3.  اگر نام کاربری درست است، رمز را چک کند. اگر رمز "1234" بود: چاپ کند `Welcome Admin`.
4.  اگر رمز اشتباه بود: چاپ کند `Wrong Password`.

**مثال خروجی:**

```text
Username: admin
Password: 777
Is Banned (True/False): False
Result: Wrong Password
```

---

### ۵. مبدل واحد هوشمند (Smart Converter with Match Case)

**هدف:** استفاده از `match case` و ترکیب آن با شرط‌های داخلی.
برنامه‌ای بنویسید که یک عدد و یک "کد تبدیل" از کاربر بگیرد و عملیات را انجام دهد.
کدها:

- `1`: تبدیل کیلومتر به مایل (فرمول: $km \times 0.62$)
- `2`: تبدیل سلسیوس به فارنهایت (فرمول: $(C \times 1.8) + 32$)
- `3`: بررسی زوج یا فرد بودن عدد.
- `_`: برای هر کد دیگری چاپ کند `Invalid Code`.

**نکته:** در داخل `case 1` و `case 2`، اگر عدد ورودی منفی بود، عملیات انجام نشود و چاپ کند `Negative input not allowed`.

**مثال خروجی:**

```text
Enter number: 10
Enter mode (1-3): 1
Result: 6.2 miles
```
