Basic_Salary=input("Amount of salary: ")
Basic_Salary=int(Basic_Salary)
HRA=0.1*Basic_Salary
print("HRA: ",HRA)
TA=0.05*Basic_Salary
print("TA: ",TA)
Total=Basic_Salary+HRA+TA
print("Total: ",Total)
Tax=0.02*Total
print("Tax: ",Tax)
Net=Total-Tax
print("Net Salary ",Net)
