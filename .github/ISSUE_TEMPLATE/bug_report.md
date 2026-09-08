---
name: Bug report
about: Report something broken in the calculator, logger, or notifier modules
title: ''
labels: bug
assignees: ''
---

**Describe the bug**
A clear and concise description of what's broken.

**To Reproduce**
Steps or code to reproduce the behavior, e.g.:
```python
from src.calculator.calculator import Calculator
calc = Calculator()
calc.divide(1, 0)  # raises unexpected error
```

**Expected behavior**
What you expected to happen instead.

**Actual behavior / Error output**
```
Paste the full traceback or error message here.
```

**Environment**
- OS: [e.g. macOS 15, Ubuntu 22.04, Windows 11]
- Python version: `python3 --version`
- `uv` version: `uv --version`
- Module affected: [calculator / logger / notifier]

**Additional context**
Anything else relevant — recent changes, related config, etc.
