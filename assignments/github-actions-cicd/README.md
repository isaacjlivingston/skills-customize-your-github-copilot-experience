# 📘 Assignment: Automating CI/CD with GitHub Actions

## 🎯 Objective

Set up a Continuous Integration (CI) pipeline using GitHub Actions that automatically runs your test suite with `pytest` and checks your code style with `ruff` every time you push to GitHub.

## 📝 Tasks

### 🛠️ Create Your First GitHub Actions Workflow

#### Description
Create a workflow file that triggers on every push and pull request, sets up a Python environment, and installs your project's dependencies.

#### Requirements
Completed program should:

- Create the file `.github/workflows/ci.yml` in your repository.
- Set the workflow to trigger on `push` and `pull_request` events.
- Define a job called `ci` that runs on `ubuntu-latest`.
- Include steps to check out the code and set up Python 3.12 using `actions/setup-python`.
- Install `pytest` and `ruff` using `pip` in a run step.

```yaml
# Starter structure — fill in the missing steps
name: CI

on: [push, pull_request]

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v4
      # TODO: Add Python setup and dependency install steps
```

### 🛠️ Run Tests and Lint in the Pipeline

#### Description
Add steps to your workflow that run `pytest` and `ruff` automatically so every push is validated.

#### Requirements
Completed program should:

- Add a step that runs `pytest -v` against your test file.
- Add a step that runs `ruff check .` to lint the codebase.
- Give each step a descriptive `name` field so the Actions log is easy to read.
- Confirm the workflow passes end-to-end by pushing to GitHub and viewing the Actions tab.

### 🛠️ Observe and Interpret Workflow Results

#### Description
Read and understand the feedback that GitHub Actions provides after a run, including how to identify failures and read logs.

#### Requirements
Completed program should:

- Navigate to the **Actions** tab in the GitHub repository and open a completed run.
- Identify the steps that passed (green check) and any that failed (red X).
- Intentionally introduce a failing test or lint error, push it, and observe the workflow fail.
- Fix the error, push again, and confirm the workflow returns to a passing state.
