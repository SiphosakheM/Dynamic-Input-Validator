user_prompt = input("Enter your data here: ")
def validate_input(user_prompt,validators):
    while True:
        for validator in validators:
            if not validator(user_prompt):
                return False
        return True
        
def is_numeric(n):
    for char in n:
        if not char.isdigit():
            return False
    return True

def is_in_range(n):
    num = int(n)
    if num in range(1,101):
        return True
    else:
        return False
    
def no_space(space):
    for char in space:
        if char == " ":
            return False
    return True
        
result = [is_numeric, is_in_range,no_space]
user_data = validate_input(user_prompt,result)
print(f"is the data valid: {user_data}")