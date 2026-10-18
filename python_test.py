#Challenge 1: Create a list of 5 cities and print only the cities that have more than 5 characters in their name.

cities = ['Nnewi', 'Enugu', 'Onitsha', 'Awka', 'Owerri']
for city in cities:
    if len(city) > 5:
        print(city)

#Challenge 2 Write a function called calculate_bmi that takes weight_kg and height_m as parameters and returns the BMI. Formula: weight / (height * height). Test it with at least two different values.

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m * height_m)
    return bmi

# Test the function
print(calculate_bmi(86, 1.80))
print(calculate_bmi(70, 1.60))

#Challenge 3:Create a dictionary of 4 employees with their salaries. Loop through it and print each employee’s name and whether their salary is above or below £40,000.

dic = {'Somtoo':50000, 'David':30000, 'Ngozi':40000, 'Ekene':35000}
for name, salary in dic.items():  
    if salary >= 40000:
        print(name + "'s salary is above £40,000")
    else:
        print(name + "'s salary is not above £40,000") 

#Challenge 4: Write a function that reads cities.txt and returns how many lines are in the file.

def line_count(filepath):
    with open(filepath, 'r') as file: 
        return len(file.readlines())

print(line_count('cities.txt'))

#Challenge 5: Create a Pandas DataFrame from a dictionary of your choice with at least 3 columns and 4 rows. Filter it to show only rows where one of the numeric columns is above a value you choose. 
import pandas as pd

data = {
    'Name': ['Emeka', 'Obinna', 'Ebuka', 'Chinenye'],
    'Age' : [25, 30, 22, 28],
    'Profession' : ['Data Engineer', 'Investment banker','Nurse', 'Copywriter']
}
df = pd.DataFrame(data)
df_filter = df[df['Age'] > 22]
print(df_filter)