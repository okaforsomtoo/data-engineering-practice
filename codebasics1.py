Month = ['January', 'February', 'March', 'April', 'May', 'June']
expense = [2200, 2350, 2600, 2130, 2000, 1980]

print(expense[1] - expense[0])
total_first_quarter = expense[0]+expense[1] + expense[2]

print(total_first_quarter)

#finding the month with the highest expense

for i in range(len(expense)):
    if expense[i] == 2000:
        print("True")
    else:
        print("not true")
Month[3]
print(Month[3])
expense[3]
print(expense[3])

expense.append(1981)
print("Expenses at the end of June:", expense)

print("Did I spend $2000 in any month?", 2000 in expense)

#print(2200 in expense)

#max_expense = max(expense)
#max_index = expense.index(max_expense)
#print(f"The month with the highest expense is {Month[max_index]} with an expense of {max_expense}")