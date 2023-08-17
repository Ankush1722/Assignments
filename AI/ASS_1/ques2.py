# Input the basic salary
basic_salary = float (input("“Enter the basic salary: "))

# Calculate HRA and DA based on the given conditions
if basic_salary <= 10000:
    hra = 0.2 * basic_salary # HRA is 20% of the basic salary
    da = 0.8 * basic_salary # DA is 80% of the basic salary
elif basic_salary <= 20000:
    hra = 0.25 * basic_salary # HRA is 25% of the basic salary
    da = 0.9 * basic_salary # DA is 90% of the basic salary
else:
    hra = 0.3 * basic_salary # HRA is 30% of the basic salary
    da = 0.95 * basic_salary # DA is 95% of the basic salary

# Calculate gross salary by adding basic salary, HRA, and DA
gross_salary = basic_salary + hra + da

# print the gross salary
print("Gross Salary:", gross_salary)
