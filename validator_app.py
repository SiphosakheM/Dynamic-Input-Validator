def validate_input(user_input, validators):
    for validator in validators:
        if not validator(user_input):
            return False
    return True


def is_numeric(value):
    return value.isdigit()


def is_in_range(value):
    try:
        num = int(value)
        return 1 <= num <= 100
    except ValueError:
        return False


def no_space(value):
    return " " not in value


user_input = input("Enter your data here: ")
validators = [is_numeric, is_in_range, no_space]

is_valid = validate_input(user_input, validators)
print(f"Is the data valid: {is_valid}")
