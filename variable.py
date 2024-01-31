
variable_name = input("Enter variable:\n")

keyword_kwlist = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break',
                  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
                  'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
                  'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'yield']

if variable_name.isidentifier() and variable_name not in keyword_kwlist and variable_name.islower():
    print(f"{variable_name} is a valid variable name.")
elif variable_name == '_':
    print(f"{variable_name} is a valid variable name.")
else:
    print(f"{variable_name} is not a valid variable name.")
