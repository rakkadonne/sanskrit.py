# Sanskrit-to-Python Mappings

This project provides a dictionary that maps Sanskrit keywords to their equivalent Python syntax. The goal is to allow writing Python code using Sanskrit constructs.

---

## Features

- **Sanskrit Syntax**: Write Python logic with Sanskrit keywords.

---

## Keyword Mappings

### 🔹 Boolean & None
| Sanskrit | Python |
|----------|--------|
| सत्     | `True` |
| असत्    | `False` |
| नास्ति   | `None` |

### 🔹 Logical Operators
| Sanskrit | Python |
|----------|--------|
| च        | `and` |
| वा       | `or` |
| न        | `not` |

### 🔹 Conditional Statements
| Sanskrit   | Python |
|------------|--------|
| यदि        | `if` |
| अथयदि     | `elif` |
| अथ         | `else` |

### 🔹 Looping Constructs
| Sanskrit   | Python   |
|------------|----------|
| परिहरन     | `for`     |
| यावत्      | `while`   |
| अग्रिम     | `break`   |
| विराम      | `continue`|
| गच्छतु     | `pass`    |

### 🔹 Functions and Lambdas
| Sanskrit     | Python   |
|--------------|----------|
| नियोग        | `def`     |
| निर्वतनम्     | `return`  |
| अनाम         | `lambda`  |

### 🔹 Exception Handling
| Sanskrit      | Python     |
|---------------|------------|
| प्रयततु       | `try`       |
| विहाय         | `except`    |
| अन्ततः        | `finally`   |
| विगर्हते       | `raise`     |
| निश्चितयति     | `assert`    |

### 🔹 Importing Modules
| Sanskrit | Python   |
|----------|----------|
| आयात     | `import` |
| यतः      | `from`   |
| नाम्ना    | `as`     |

### 🔹 Scope and Memory
| Sanskrit     | Python     |
|--------------|------------|
| सर्वत्रगम्    | `global`    |
| असामीपिक     | `nonlocal`  |
| अपनयति      | `del`       |

### 🔹 Classes & Async
| Sanskrit    | Python     |
|-------------|------------|
| विधि        | `class`     |
| सह          | `with`      |
| यत्नतः       | `async`     |
| प्रतीक्षेत्   | `await`     |

### 🔹 Other Keywords
| Sanskrit | Python |
|----------|--------|
| इति      | `in`   |
| अस्ति     | `is`   |
| दत्ते     | `yield`|

### 🔹 Built-in Functions
| Sanskrit       | Python     |
|----------------|------------|
| पङ्क्तिः       | `range`     |
| मुद्रण         | `print`     |
| प्रवेशयति      | `input`     |
---

### How to Write Python in Sanskrit:

1. Download `sanskrit.py` or clone the repo at [sanskrit.py](https://github.com/rakkadonne/sanskrit.py)  .
2. Write Sanskrit Python code using the Sanskrit Python dictionary as a manual.
3. Save the file with a `.esspy` extension.
4. Run the command:

   ```bash
   python <path_to_sanskrit.py> <path_to_.esspy_file>

---

### Some Important Details 

1. Can **create modules in Sanskrit Python** and import them in other `.esspy` or `.py` files.

2. Can **import from standard or Custom Python modules** as usual — the tool does not block or interfere with native imports.

3. This **only replaces Python keywords and native functions**, and does **not touch the namespace** of other classes, methods, or modules, ensuring compatibility with external libraries (from pip) or custom codebases. So , you can use latin characters for variables, built in modules or if you wish the original keyword also (it would still be valid).
