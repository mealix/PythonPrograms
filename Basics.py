print("Nothing to say")
print('No thing to say')
#print("OK!"+input("Ur Name"))
#print(len(input("Age!")))
print("Hello"[3])
'''num=input("Enter The number")
num1=num[0]
num2=num[1]
num1=int(num1)
num2=int(num2)
print(num1+num2)
#f-string
print(f"Your Number Is {num1}")'''
'''age=int(input("Enter Your Current Age"))
rem_age=90-age
days=rem_age*365
weeks=rem_age*52
months=rem_age*12
print(f"You have {days} days,{weeks} weeks and {months} months left")'''
print("Welcome to tip calculater")
bill=float(input("What was the total bill?"))
tip=int(input("What percentage of tip would you like to give?10,12 or 15?"))
people=int(input("How many people to split the bill?"))
add_tip=bill*(tip/100)
total_bill=bill+add_tip
per_person=total_bill/people

print(f"Each person should pay{round(per_person,2)}")