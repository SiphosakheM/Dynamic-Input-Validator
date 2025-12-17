# Project 01: Dynamic Input Validator

## Overview
This project creates a strong input validation system using higher-order functions. It lets developers send a list of functional rules to a single input handler, which ensures data integrity before the rest of the program runs.

## Technical Specs
- **Higher-Order Functions:** Passing functions as arguments in a list.
- **Looping:** Infinite `while` loops with conditional `break` or `return` points.
- **Predicate Logic:** Writing small, single-responsibility functions that return Booleans.

## Features
- Multi-stage validation logic.
- Real-time error feedback for specific failed rules.
- Reusable across different data types (Strings, Ints).

## Usage
Run the script and follow the prompts. The system will reject any input that contains spaces, isn’t a number, or is outside the 1-100 range.
