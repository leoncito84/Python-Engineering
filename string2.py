# NEGATIVE INDEXING IN STRINGS
#                  1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot)

# print(parrot[3])
# print(parrot[7])
# print(parrot[8])
# print(parrot[4])
# print(parrot[2])
# print(parrot[0])
# print(parrot[9])

# print()

# print(parrot[-1])
# print(parrot[-14])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-2])
# print(parrot[-13])

# SLICING WITH NEGATIVE NUMBER
#                  1
#        012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6:2])  # NRE
print(parrot[0:6:3])  # Nw
# number = "9,223,373,036,854,775,807" #
number = "9,223;372:036,854,775;807"
print(number[1::4])

# print(parrot[0:6])
# print(parrot[-14:5])
# print(parrot[0:1])
# print(parrot[-13:2])

# print(parrot[0:2]) # Norweg
# print(parrot[-4:2])
