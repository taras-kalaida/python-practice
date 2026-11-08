from functools import wraps


def check_string(func):
    @wraps(func)
    def wrapper(value):
        if not isinstance(value, str):
            print("Error: value must be a string")
            return

        return func(value)

    return wrapper


@check_string
def print_string(value):
    print(value)


@check_string
def check_case(value):
    if value.isupper():
        print("All letters are uppercase")
    elif value.islower():
        print("All letters are lowercase")
    else:
        print("Mixed case")

@check_string
def uppercase_letters(value):
    return list(map(lambda w: w.upper(), value))
