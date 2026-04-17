# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Converts base-10 numbers (integers and fractional) to bases 2–9. Package name: `numerical-base-converter-nighthawk017`.

## Commands

```bash
# Install in editable mode (run once)
pip install -e .

# Run tests
pytest

# Run a single test
pytest tests/test_converter.py::test_answer

# Run converter directly
python src/converter.py
```

## Architecture

Single module: `src/converter.py`. Three public functions compose the conversion pipeline:

- `convert_integer_part(value, target_base)` — repeated modulo/divide loop, result reversed
- `convert_fractionary_part(value_str, target_base)` — repeated multiply loop, extracts leading digit each iteration
- `convert_number(value_str, target_base)` — validates input, splits on `.`, delegates to the two functions above

Private helpers `_get_integer_part` / `_get_fractionary_part` split a string on `.`.

`main()` exists for manual runs but has a hardcoded test value and commented-out `input()` calls — it is not a real CLI.

## Notes

- Target base must be 2–9 (enforced in `convert_number`, raises `ValueError`)
- Fractional input accepted as string (e.g. `"3.14"`); integer-only input skips the fractional path
- Tests in `tests/test_converter.py` import via `from src import converter`
