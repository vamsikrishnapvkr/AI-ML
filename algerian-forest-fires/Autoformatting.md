## Python Auto Formatting + Import Sorting + Git Pre-Commit Setup
- Using:
    - Visual Studio Code
    - Ruff
    - Black
    - pre-commit
- This setup gives:
    - automatic indentation
    - automatic import sorting
    - no extra spaces
    - same formatting for all developers
    - automatic checks before Git commit

## STEP 1 — Project Structure
### Create this structure:
```text
my-python-project/
│
├── .vscode/
│   └── settings.json
│
├── .pre-commit-config.yaml
├── pyproject.toml
├── requirements-dev.txt
│
├── src/
│   └── main.py
│
└── .gitignore
```

## STEP 2 — Install Required Packages
- pip install ruff black pre-commit

## STEP 3 — Configure VS Code Auto Formatting
```json
{
  // =========================
  // AUTO SAVE SETTINGS
  // =========================

  // Save automatically after delay
  "files.autoSave": "afterDelay",

  // Delay in milliseconds
  // 1000 = 1 second
  "files.autoSaveDelay": 1000,



  // =========================
  // EDITOR FORMATTING
  // =========================

  // Auto format entire file on save
  "editor.formatOnSave": true,

  // Auto format pasted code
  "editor.formatOnPaste": true,



  // =========================
  // PYTHON SETTINGS
  // =========================

  "[python]": {

    // Use Ruff as formatter
    "editor.defaultFormatter": "charliermarsh.ruff",

    // Run actions automatically on save
    "editor.codeActionsOnSave": {

      // Fix lint problems automatically
      "source.fixAll": "explicit",

      // Organize imports automatically
      "source.organizeImports": "explicit"
    }
  },



  // =========================
  // INDENTATION SETTINGS
  // =========================

  // Use spaces instead of tabs
  "editor.insertSpaces": true,

  // 4-space indentation
  "editor.tabSize": 4,

  // Detect existing indentation automatically
  "editor.detectIndentation": true
}
```

## STEP 4 — Install VS Code Extensions
- Install these extensions:
    - Ruff VS Code Extension
    - Python Extension for VS Code

## STEP 5 — Configure Ruff + Black Rules
### pyproject.toml
```toml
# ======================================
# BLACK CONFIGURATION
# ======================================

[tool.black]

# Maximum line length
line-length = 88

# Python version
target-version = ["py311"]



# ======================================
# RUFF CONFIGURATION
# ======================================

[tool.ruff]

# Same line length as black
line-length = 88

# Python version
target-version = "py311"



# ======================================
# LINT RULES
# ======================================

[tool.ruff.lint]

select = [

    # pycodestyle errors
    "E",

    # pyflakes
    "F",

    # Import sorting
    "I"
]



# ======================================
# FORMAT RULES
# ======================================

[tool.ruff.format]

# Use double quotes
quote-style = "double"

# Use spaces for indentation
indent-style = "space"

# Auto detect line endings
line-ending = "auto"

# Format code inside docstrings
docstring-code-format = true
```

## STEP 6 — Configure Git Pre-Commit Hooks
### .pre-commit-config.yaml
```yaml
repos:

  # ====================================
  # RUFF
  # ====================================

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.11.10

    hooks:

      # Fix lint issues automatically
      - id: ruff
        args: [--fix]

      # Format code automatically
      - id: ruff-format



  # ====================================
  # BLACK
  # ====================================

  - repo: https://github.com/psf/black
    rev: 25.1.0

    hooks:
      - id: black
```

## STEP 7 — Enable Git Hooks (RUN ONLY ONCE)
- run: pre-commit install
- This installs Git hooks. Only once per project.

## STEP 8 — Manual Formatting Commands
### If you want to manually clean the whole project:
- Fix lint issues + imports
    - ruff check . --fix
    - removes unused imports
    - sorts imports
    - removes extra spaces
    - fixes many code issues
- Format all files
    - ruff format .
    - fixes indentation
    - fixes spacing
    - fixes line wrapping
    - applies consistent formatting

## STEP 9 — Daily workflow (IMPORTANT)
### After setup, you NEVER manually format every time.
- You just do:
    - git add .
    - git commit -m "update code"

### Automatically happens:
- fixes indentation
- removes extra spaces
- sorts imports
- formats code
- checks errors