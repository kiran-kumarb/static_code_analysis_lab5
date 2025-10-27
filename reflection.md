### 1. Which issues were the easiest to fix, and which were the hardest? Why?

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