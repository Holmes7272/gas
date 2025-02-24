# Password Generator

A simple Python script to generate random passwords with customizable options and basic strength evaluation.

## Features
- Generate passwords of any specified length.
- Choose whether to include letters (a-z, A-Z), digits (0-9), and special characters (!@#$%^&* etc.).
- Basic password strength evaluation based on length and character variety:
  - **Strong**: 12+ characters with letters, digits, and special characters.
  - **Medium**: 8+ characters with at least letters and digits.
  - **Weak**: Anything less secure than the above.
- Error handling for invalid inputs (e.g., negative length or no character types selected).

## Requirements
- Python 3.x (no external libraries required, uses only the standard `random` and `string` modules).
