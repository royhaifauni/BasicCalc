# PRD - Calculator Testing Suite

## Overview
The goal of the testing suite is to ensure the reliability and correctness of the Basic Calculator's arithmetic operations. It provides automated verification to prevent regressions during future development.

## Scope
The testing suite covers all core mathematical functions:
- **Addition**: Positive, negative, and zero values.
- **Subtraction**: Positive, negative, and zero results.
- **Multiplication**: Standard products and multiplication by zero.
- **Division**: Standard quotients and floating-point results.
- **Error Handling**: Explicit verification of division-by-zero exceptions.

## Technical Requirements
- **Framework**: Standard Python `assert` statements (minimalist approach) or `pytest` (if scaled).
- **Execution**: Run via `uv` to ensure consistency with the project environment.
- **Environment**: Must run in the same virtual environment as the main application.

## Test Cases
| Feature | Scenario | Expected Outcome |
|---------|----------|------------------|
| Addition | 2 + 3 | 5 |
| Addition | -1 + 1 | 0 |
| Subtraction | 10 - 5 | 5 |
| Subtraction | 0 - 1 | -1 |
| Multiplication | 3 * 4 | 12 |
| Multiplication | 0 * 5 | 0 |
| Division | 10 / 2 | 5.0 |
| Division | 10 / 0 | Raises ValueError("Cannot divide by zero.") |

## Success Criteria
- All automated tests must pass before any code is considered "production-ready."
- Test execution must be possible with a single command: `uv run tests/test_calculator.py`.
