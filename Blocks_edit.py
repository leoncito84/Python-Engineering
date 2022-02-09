for i in range(1, 13):
 print("No. {} square is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
print("*" * 80)

name = input("Please enter your name:")
age = input("How are old you, {0}?".format(name))
print(age)

name = input("Please can you give me an answer this surname")
age = input("How are old you, {0}?".format(name))
postcode = input("What is your postcode,")
print(age)
print(postcode)

name = input("Please enter your name middle")
age = input("How old she is your daughter, {0}?".format(name))
employer = input("What is your job title")
martial = input("Are you married or single")
print(age)
print(employer)
print(martial)

country = input("What is your dream country")
name = input("Please enter your name")
age = input("How old are you, {0}?".format(name))
feetHeight = input("How is your tall height")
gender = input("Are you male or female?".format(name))
print(age)
print(feetHeight)

name = input("Please enter your name:")
age = int(input("How are old you, {0}?".format(name)))
print(age)

if age >= 18:
 print("You are old enough to vote")
 print("Please put an X in the box")
else:
 print("Please come back in {0} years ".format(18 - age))

if age < 18:
 print("Please come back in {0} years ".format(18 - age))
elif age == 900:
 print("Sorry, Yoda you die in return of the Jedi")
else:
 print("You are old enough to vote")
print("Please put an X in the box")
