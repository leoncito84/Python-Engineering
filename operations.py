a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0
print(a // b)  # 4 integer division, rounded down towards minus infinity
print(a % b)  # 0 modulo: the remainder after integer division

print()
# for i in range(1, a // b):
# #print (i)

# i = 1
# print(i)
# i = 2
# print(i)
# i = 3

print()

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print(((a + b) / 3) - 4 * 12)
print(((a + b) / 3 - 4) * 12)

# c = a + b
# d = a / b
# e = a - 4
# print(e * 12)

c = a + b
d = c / 3
e = d - 4
f = c % 5
print(e * 12)

# OPERATOR PRECEDENCE ACRONYMS
# . #PEDMAS PARENTHESES, Exponents, Multiplication/Division, Addition/Subtraction
# . #BEDMAS Brackets, Exponents, Division/Multiplication, Addition/Subtraction
# . #BODMAS Brackets, Order, Division/Multiplication, Addition/Subtraction
# . #BIDMAS Brackets, Index, Division/Multiplication, Addition/Subtraction


# print(a / (b * a) / b)
# print(a + (b - a) / b)
# print(a * b / (b + a) / b)
