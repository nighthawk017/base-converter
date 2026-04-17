# base-converter

Converts base-10 numbers (integers and decimals) to bases 2–9.

## Installation

```bash
pip install numerical-base-converter
```

## Usage

### As a library

```python
from base_converter import convert_number

convert_number('10', 2)    # '1010'
convert_number('8', 8)     # '10'
convert_number('0.5', 2)   # '0.1'
convert_number('3.14', 8)  # '3.11037...'
```

### As a CLI

```bash
base-converter
# Enter the value to convert: 10
# Enter the target base (2-9): 2
# Result: 1010
```

## API

```python
convert_number(value_str: str, target_base: int) -> str
```
Converts a base-10 number string to the target base. Accepts integers (`'42'`) and decimals (`'3.14'`).

```python
convert_integer_part(value: int, target_base: int) -> str
convert_fractionary_part(value_str: str, target_base: int) -> str
```
Lower-level functions for converting the integer and fractional parts separately.

Raises `ValueError` if `target_base` is outside 2–9 or `value_str` is not a valid number.

## Requirements

Python >= 3.8
