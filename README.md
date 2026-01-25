# Project 01: Dynamic Input Validator

Overview

This project creates a modular and reusable input validation system using higher-order functions in Python. Validation rules are provided as callable functions, enabling flexible and scalable input checks before processing the data.

Key Concepts Used

Higher-order functions (functions as arguments)  
Clean, single-responsibility validation rules  
Defensive programming  
Boolean predicate logic  

Features

Supports multiple validation rules applied one after another  
Easily extendable by adding new validator functions  
Prevents invalid input such as:  
- Non-numeric values  
- Numbers outside the range 1 to 100  
- Inputs containing spaces  

How It Works

User input is collected.  
A list of validator functions is given to a central validation handler.  
Each validator checks the input and returns True or False.  
The input is accepted only if all validation rules pass.  

Example Validators

Numeric validation  
Range validation (1 to 100)  
Whitespace detection  

Usage

Run the script and enter a value when prompted.  
The program will indicate whether the input is valid based on the applied rules.