#logical operators
age = 25
citizen = True
print(age >= 18 and citizen == True)

has_card = False
has_casd = True
print(has_card or has_casd)

is_logged_in = True

print(not is_logged_in)

#atm eligibility checker
balence = 10000
withdraw = 5000

print(withdraw > 0 and withdraw <= balence)

#student scholarship eligibility checker
marks = float(input("Enter marks: "))
attendence = float(input("Enter attendence: "))

eligible = marks >= 85 and attendence >= 75 
print("scholarship Eligible:", eligible) 