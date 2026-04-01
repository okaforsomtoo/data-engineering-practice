def greet(name):
    print("Hello, " + name + "!")
greet("Somtoo")
greet("Lagos")
greet("World")

def calculate_tax(salary, tax_rate):
    tax = salary * tax_rate
    return tax
tax_owed = calculate_tax(50000, 0.20)
print(tax_owed)

def describe_person(name, age, city):
    return (name + ' is '+ str(age) + ' years old' + ' and lives in '+ city)
person = describe_person('Lilian', 23, 'Norwich')
print(person)