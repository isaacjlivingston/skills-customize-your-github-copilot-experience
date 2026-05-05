# 📘 Assignment: Testing Python Code with pytest

## 🎯 Objective

Learn how to write and run automated tests for Python functions using `pytest`. By the end of this assignment, you will have a working test suite that validates the behavior of a small Python module.

## 📝 Tasks

### 🛠️ Write Your First Tests

#### Description
Install `pytest` and write basic test functions that verify the behavior of the provided helper functions in `starter-code.py`.

#### Requirements
Completed program should:

- Install `pytest` using `pip install pytest`.
- Create a file called `test_functions.py` in the same folder.
- Write at least one test function per helper function using the `test_` naming convention.
- Use plain `assert` statements to check expected outputs.
- Pass all tests by running `pytest` in the terminal.

```text
Example test function

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

### 🛠️ Cover Edge Cases

#### Description
Expand your test suite to handle edge cases and unexpected inputs, making your tests more robust.

#### Requirements
Completed program should:

- Add at least two edge-case tests per function (e.g., zero values, negative numbers, empty strings).
- Use `pytest.raises` to verify that invalid inputs raise the correct exceptions.
- Organize related tests into a test class using `class Test<FunctionName>`.

```text
Example edge case and exception test

import pytest

class TestDivide:
    def test_normal(self):
        assert divide(10, 2) == 5

    def test_zero_dividend(self):
        assert divide(0, 5) == 0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(10, 0)
```

### 🛠️ Read and Understand the pytest Report

#### Description
Run the full test suite and interpret the output that `pytest` produces.

#### Requirements
Completed program should:

- Run `pytest -v` to see verbose output for each test.
- Identify which tests passed (`.`) and which failed (`F`) in the summary.
- Fix any failing tests so the final run shows all green passes.
- Confirm the final output includes a line such as `N passed` with no failures.
