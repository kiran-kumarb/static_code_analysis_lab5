### **Objective**

To improve the code quality, maintainability, and security of the `inventory_system.py` program by using static analysis tools:

-   **Pylint** (code quality and logical issues)
-   **Flake8** (PEP8 style and formatting)
-   **Bandit** (security vulnerabilities)

### **Tools Used & Commands**

"pip install pylint flake8 bandit

python -m pylint inventory_system.py > pylint_report.txt

python -m flake8 inventory_system.py > flake8_report.txt

python -m bandit -r inventory_system.py > bandit_report.txt"

  

**Issue Type**

**Tool**

**Line(s)**

**Description**

**Fix Approach**

**Mutable default argument**

Pylint

8

Function `addItem` used `logs=[]` as a default argument, causing the same list to be shared across calls.

Changed default to `None` and initialized inside function.

**Bare except**

Pylint / Bandit / Flake8

19

`except:` block catches all exceptions, hiding real errors.

Replaced with specific exception type `except KeyError:` and added logging message.

**Use of `eval()`**

Bandit / Pylint

59

`eval()` executes arbitrary code and poses a major security risk.

Removed `eval()` completely.

**File handling without context manager**

Pylint

26, 32

Files were opened using `open()` and not closed properly.

Replaced with `with open(..., encoding='utf-8')` for automatic closing.

**Naming convention (camelCase)**

Flake8 / Pylint

8–48

Functions used `camelCase` names (e.g., `addItem`, `removeItem`), violating PEP8.

Renamed to `snake_case` (`add_item`, `remove_item`, etc.).

**Missing docstrings**

Pylint

Multiple (8–48)

Functions lacked docstrings explaining purpose and parameters.

Added short descriptive docstrings for every function.

**Unused import**

Pylint / Flake8

2

`import logging` was unused in the original code.

Integrated `logging` module properly for logs.

**No newline at EOF**

Flake8 / Pylint

61

File did not end with a newline, violating PEP8 formatting.

Added final newline at the end of the file.

**Logging f-string interpolation**

Pylint

38, 58, 64, 66

Used f-strings inside logging calls.

Switched to lazy formatting using `%s` and `%d` placeholders.

**Inconsistent return statements**

Pylint

33

Function `add_item()` returned `logs` in one path but nothing in others.

Ensured all branches consistently return `logs`.

**Global statement warning**

Pylint

89

Use of `global stock_data` flagged for maintainability.

Suppressed locally with `# pylint: disable=global-statement`.

  

1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were **style-related errors** reported by *Flake8* and *Pylint*, such as missing newlines, unused imports, and incorrect naming (camelCase → snake_case). These fixes were straightforward since they only required formatting adjustments.  
The hardest issues were **removing the `eval()` function** and **replacing bare `except:` blocks**, as they required understanding how the code executed and ensuring the program’s behavior stayed consistent after making safer replacements.

---

### 2. Did the static analysis tools report any false positives?

Yes. *Bandit* flagged the use of `eval()` as a severe security issue, even though it was only used for demonstration purposes. While technically correct, it acted as a false positive in this specific educational context. However, removing it was still the right decision to follow secure coding standards.

---

### 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate static analysis tools into both **local and CI/CD workflows**:

-   Use **pre-commit hooks** to automatically run `pylint`, `flake8`, and `bandit` before every commit.
    
-   Add them to a **GitHub Actions** or **GitLab CI pipeline** to ensure every push and pull request is checked for code quality and security.
    
-   Enable **real-time linting in IDEs** like VS Code so developers can fix issues instantly while coding.
    

---

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

After applying the fixes, the code became:

-   **More readable:** with proper naming conventions, spacing, and docstrings.
    
-   **More secure:** by removing unsafe functions like `eval()` and handling exceptions explicitly.
    
-   **More maintainable:** due to structured logging and consistent returns.
    
-   **More robust:** since file operations now use context managers (`with open()`), preventing resource leaks and improving reliability.