
# x = input("Price: ")

# if x < 100:
#     print("Cheap")
# else:
#     print("Expensive")


def sum(x, y):
    z = x + y
    return z


x = input("Num1: ")
y = input("Num2: ")
z = sum(x, y)

if z < 100:
    print("Cheap it's only {}".format(z))
elif z == 100:
    print ("Mid Range it's only {}".format(z))
else:
    print("Expensive it's price is {}".format(z))
