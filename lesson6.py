try:
    result = 10/0
    print(result)
except:
    print("Something went wrong")

try:
    result = 10/0
except ZeroDivisionError:
    print("You can't divide by zero")

try: 
    number = int("Somtoo")
except ValueError:
    print("That's not a valid number")

def convert_to_number(value):
    try:
        return int(value)
    except ValueError:
        return "Invalid - could not convert"
print(convert_to_number("25"))
print(convert_to_number("Somtoo"))
print(convert_to_number("100"))
print(convert_to_number("abc"))

try:
    result = 10 / 2
    print(result)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("This always runs")