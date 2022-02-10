Mobile_list = ["Samsung",
               "Iphone",
               "Haw",
               "Nokia",
               "Sony",
               "xperiaGoogle"
               ]

another_list = Mobile_list
print(id(Mobile_list))
print(id(another_list))

Mobile_list += ["Samsung"]
print(Mobile_list)

Mobile_list += ["xperiaGoogle"]
print(Mobile_list)

a = b = c = d = e = f = another_list
print(a)

print("Sony")
e.append("Sony")
print(c)
print(d)
