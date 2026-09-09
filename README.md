# Technology Template

A modern, OS-agnostic Python project template featuring comprehensive test coverage, continuous integration with CircleCI, and dependency management with [uv](https://github.com/astral-sh/uv). It includes ready-made configuration for static type checking, linting/formatting, and automated testing across unit, integration, and end-to-end suites.

## Use Case
Replace the package files(src) in this repository with your own package files, do the same for tests. Make sure to write unit, integration and end to end tests otherwise they would need to be toggled off in the circle ci. Also remember to use your own CircleCI status badge down here for the build status. Please report any bugs if they come up.

### Circle CI Status Badge
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/happyc0der/Template-Repository-Python/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/happyc0der/Template-Repository-Python/tree/main)

## Prerequisites

You only need two things installed, regardless of operating system:

* [Git](https://git-scm.com/)
* [uv](https://docs.astral.sh/uv/)

You do **not** need Python installed beforehand. `uv` detects a compatible Python on your system automatically, or downloads a managed interpreter that satisfies this project's `requires-python` constraint if one isn't found.

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
   This creates `.venv`, resolves and installs runtime and development dependencies (`mypy`, `ruff`, `nose2`, `coverage`, `pre-commit`), and editable-installs the project itself. Every command below runs through `uv run`, so you never need to manually activate `.venv`.

## Project Structure

```
src/
  calculator/     # calculator implementation
  logger/         # logging implementation
  notifier/       # notifier implementation
tests/
  unit/           # unit tests for all three modules
  integration/    # cross-module integration tests
  e2e/            # end-to-end tests
```

Source and tests are kept fully separate, following standard Python packaging conventions — no test code lives inside `src/`.

## Development Tools

### Static Analysis
```bash
uv run mypy src tests
uv run ruff check .
```

Auto-format code:
```bash
uv run ruff format .
```

### Testing

Run each suite:
```bash
uv run nose2 -v -s tests/unit/
uv run nose2 -v -s tests/integration/
uv run nose2 -v -s tests/e2e/
```

Run everything at once:
```bash
uv run nose2
```

#### Running Tests With Coverage

This mirrors what CI does:
```bash
COVERAGE_FILE=.coverage.unit uv run nose2 -v -s tests/unit/ --with-coverage --coverage=src
COVERAGE_FILE=.coverage.integration uv run nose2 -s tests/integration/ --with-coverage
COVERAGE_FILE=.coverage.e2e uv run nose2 -s tests/e2e/ --with-coverage

uv run coverage combine .coverage.unit .coverage.integration .coverage.e2e
uv run coverage report --fail-under=70
uv run coverage xml -o coverage-reports/coverage.xml
uv run coverage html -d coverage-reports/html
```

> **Note (Windows PowerShell):** `COVERAGE_FILE=... command` syntax is bash/zsh-only. On PowerShell: `$env:COVERAGE_FILE=".coverage.unit"; uv run nose2 ...`

### Coverage Reports

Open `coverage-reports/html/index.html` in your browser after running the commands above.

## Continuous Integration

CircleCI, on every push:
- Installs dependencies with `uv sync`
- Runs static analysis (`mypy`, `ruff`)
- Executes unit, integration, and end-to-end test suites
- Combines coverage and enforces a 70% minimum threshold
- Publishes test results and coverage reports as CI artifacts

## Contributing

1. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```

2. Install the pre-commit hooks (already included via `uv sync`):
   ```bash
   uv run pre-commit install
   ```

3. Make your changes and commit:
   ```bash
   git add .
   git commit -m "Your descriptive commit message"
   ```
   Pre-commit hooks automatically format (`ruff format`), lint (`ruff check`), type-check (`mypy`), and run the unit test suite before allowing the commit.

4. Push and open a pull request:
   ```bash
   git push origin feature-name
   ```

## License

Licensed under the Apache License 2.0 — see [LICENSE](LICENSE).

## Additional Resources

- [uv Documentation](https://docs.astral.sh/uv/)
- [CircleCI Documentation](https://circleci.com/docs/)
- [nose2 Documentation](https://docs.nose2.io/en/latest/)
