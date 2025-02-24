# gas
Google Apps Script
# Unique Code Generator for Google Sheets

This Google Apps Script generates unique codes (e.g., "ORD-001", "ORD-002") in a Google Sheets spreadsheet and automatically adds them to a specified column when a new row is edited. It’s useful for tracking orders, requests, or any items requiring a unique identifier.

## Features
- Generates sequential codes with a customizable prefix (default: "ORD-").
- Automatically adds a new code to the next row when any cell (except the code column) is edited.
- Formats numbers with leading zeros (e.g., "001" instead of "1").
- Works seamlessly with Google Sheets' `onEdit` trigger.

## How It Works
1. The script checks the last used code in column A (configurable).
2. If the sheet is empty, it starts with "ORD-001".
3. For each new row, it increments the number (e.g., from "ORD-001" to "ORD-002") and writes it to the next available row in column A.
4. The `onEdit` trigger ensures the code runs whenever a user modifies the sheet (outside of column A).

## Installation
1. Open your Google Sheet.
2. Go to `Extensions > Apps Script`.
3. Copy and paste the script from above into the editor.
4. Save the script with a name (e.g., "UniqueCodeGenerator").
5. Reload your Google Sheet — the script will run automatically when you edit the sheet.

## Customization
- **Prefix**: Change `"ORD-"` in the `newCode` variable to any prefix you prefer (e.g., "TASK-", "ID-").
- **Column**: Adjust `codeColumn` to use a different column (e.g., `2` for column B).
- **Number Format**: Modify `("000" + newNumber).slice(-3)` to change the number of digits (e.g., `("00" + newNumber).slice(-2)` for "01").

## Usage
- Start adding data to your sheet (e.g., in columns B, C, etc.).
- A unique code will automatically appear in column A for each new row.

## Notes
- The script avoids overwriting existing codes by checking the last row.
- If you manually edit a code in column A, the script won’t interfere unless another column is edited.

## License
This project is licensed under the MIT License — feel free to use and modify it as needed!
