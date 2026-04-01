# with open("test.txt", "w") as file:
    #file.write("Hello, this is my first file!")
# print("File written successfully")

# with open("test.txt", "r") as file:
    #content = file.read()
#print(content)

with open("cities.txt", "w") as file:
    file.write("London\n")
    file.write("Lagos\n")
    file.write("New York\n")
    file.write("Paris\n")

print("File written successfully")

with open ("cities.txt","r") as file:
    for line in file:
        print(line.strip())

with open("cities.txt", "a") as file:
    file.write("Tokyo\n")
    file.write("Berlin\n")
print('cities added')