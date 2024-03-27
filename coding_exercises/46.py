# Implement a function that gets a person's name (e.g. john) as a parameter and returns a greeting (e.g. Hi John). '
# Note that the first letter of the person's name should always be uppercase.

def greeting(name):
    name = name.title()
    return f"Hi {name}"
