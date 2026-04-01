temperature = 15

if temperature > 30:
    print("It's hot outside")
elif temperature > 20:
    print("It's warm outside")
else:
    print("It's cold outside")

def check_salary(salary):
    if salary > 60000:
        return "Higher earner"
    elif salary > 30000:
        return "Middle earner"
    else:
        return "Low earner"

print(check_salary(75000))
print(check_salary(45000))
print(check_salary(20000))


def check_data_quality(value):
    if value > 0:
        return "Valid"
    elif value == 0:
        return "Zero Value"
    else:
        return "Invalid"
print(check_data_quality(10))
print(check_data_quality(-1))
print(check_data_quality(0))