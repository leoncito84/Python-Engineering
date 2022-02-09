Mobile_list = ["Samsung", "Iphone", "Haw", "Nokia", "Sony", "xperiaGoogle"]
for item in Mobile_list:
    print("buy" + item)

# Mobile_list= ["Samsung", "Iphone", "Haw", "Nokia", "Sony", "xperiaGoogle"]
# for item in Mobile_list:
# if item !== "spam":
# print("buy" + item)


for item in Mobile_list:
    if item == "spam":
        continue
print("buy" + item)
