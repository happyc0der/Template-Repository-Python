# Technology Template

A modern, OS-agnostic Python project template featuring comprehensive test coverage, continuous integration with CircleCI, and dependency management with [uv](https://github.com/astral-sh/uv). It includes ready-made configuration for static type checking, linting/formatting, and automated testing across unit, integration, and end-to-end suites.

## Prerequisites

You only need two things installed, regardless of operating system:

* [Git](https://git-scm.com/)
* [uv](https://docs.astral.sh/uv/)

You do **not** need Python installed beforehand. `uv` detects a compatible Python on your system automatically, or downloads a managed interpreter that satisfies this project's `requires-python` constraint if one isn't found — no manual Python install, no `pyenv`, no version conflicts.

## Project Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install `uv` (macOS/Linux):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   On Windows (PowerShell):
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. Install dependencies and create the virtual environment:
   ```bash
   uv sync
   ```
   This single command creates `.venv`, resolves and installs runtime and development dependencies (`mypy`, `ruff`, `nose2`, `coverage`, `pre-commit`), and editable-installs the project itself. You don't need to manually activate `.venv` — every command below is run through `uv run`, which finds it automatically.

## Project Structure

```
src/
  calculator/   # calculator module + unit tests (src/calculator/test/)
  logger/       # logging module + unit tests (src/logger/test/)
  notifier/     # notifier module + unit tests (src/notifier/test/)
tests/
  integration/  # integration tests
  e2e/          # end-to-end tests
```

## Development Tools

### Static Analysis

Run type checking and linting:
```bash
uv run mypy src tests
uv run ruff check .
```

Auto-format code:
```bash
uv run ruff format .
```

### Testing

#### Running Individual Test Suites
```bash
uv run nose2 -v -s src/calculator/test/
uv run nose2 -v -s src/logger/test/
uv run nose2 -v -s src/notifier/test/
uv run nose2 -v -s tests/integration/
uv run nose2 -v -s tests/e2e/
```

Run everything at once:
```bash
uv run nose2
```

#### Running Tests With Coverage

This mirrors what CI does, split per-suite so coverage files can be combined afterward:
```bash
COVERAGE_FILE=.coverage.calculator uv run nose2 -v -s src/calculator/test/ --with-coverage --coverage=src.calculator
COVERAGE_FILE=.coverage.logger uv run nose2 -v -s src/logger/test/ --with-coverage --coverage=src.logger
COVERAGE_FILE=.coverage.notifier uv run nose2 -v -s src/notifier/test/ --with-coverage --coverage=src.notifier
COVERAGE_FILE=.coverage.integration uv run nose2 -s tests/integration/ --with-coverage
COVERAGE_FILE=.coverage.e2e uv run nose2 -s tests/e2e/ --with-coverage

uv run coverage combine .coverage.calculator .coverage.logger .coverage.notifier .coverage.integration .coverage.e2e
uv run coverage report --fail-under=70
uv run coverage xml -o coverage-reports/coverage.xml
uv run coverage html -d coverage-reports/html
```

> **Note (Windows PowerShell):** `COVERAGE_FILE=... command` syntax is bash/zsh-only. On PowerShell, set the variable first: `$env:COVERAGE_FILE=".coverage.calculator"; uv run nose2 ...`

### Coverage Reports

After running the commands above, open `coverage-reports/html/index.html` in your browser to view the full HTML coverage report.

## Continuous Integration

This project uses CircleCI to, on every push:
- Install dependencies with `uv sync`
- Run static analysis (`mypy`, `ruff`)
- Execute unit, integration, and end-to-end test suites
- Combine and enforce a minimum coverage threshold (70%)
- Publish test results and coverage reports as CI artifacts

## Contributing

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```

2. Install the pre-commit hooks (already included via `uv sync`, no separate `pip install` needed):
   ```bash
   uv run pre-commit install
   ```

3. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Your descriptive commit message"
   ```
   The pre-commit hooks will automatically:
   - Format your code with `ruff format`
   - Check for linting issues with `ruff check`
   - Verify type annotations with `mypy`
   - Run unit tests to ensure everything still passes

   If any hook fails, the commit is blocked until you fix the reported issues and re-commit.

4. Push your changes and open a pull request:
   ```bash
   git push origin feature-name
   ```

## License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.

## Additional Resources

- [uv Documentation](https://docs.astral.sh/uv/)
- [CircleCI Documentation](https://circleci.com/docs/)
- [nose2 Documentation](https://docs.nose2.io/en/latest/)
