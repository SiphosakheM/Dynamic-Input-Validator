user_prompt = input("Enter your data here: ")
def validate_input(user_prompt,validators):
    while True:
        if validators(user_prompt):
            return True
        else:
            return False
        
def is_numeric(n):
    for n in user_prompt:
        if n.isdigit():
            return True
    return False

def is_in_range(n):
    num = int(n)
    if num in range(1,101):
        return True
    else:
        return False
    
def no_space(space):
    for space in user_prompt:
        if space != " ":
            return True
        else:
            return False
        
result = [is_numeric, is_in_range,no_space]
user_data = validate_input(user_prompt,result)
print(f"is the data valid: {user_data}")