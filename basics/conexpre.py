list = [1, 2, 3]
for i in list:
    if(i**2) % 3 == 0:
        print "Your Number is 9"
        print i

for i in list:
    if i == 2:
        print "It's two"
    elif i == 1:
        print "Something Different"
    else:
        print(i)

list_d = ["Justin", "Apple", "Food", 3231, "Another", 12321]
list_e = []
for i in list_d:
    if isinstance(i, int):
        list_e.append(i)
print(list_e)


x = 0
print list_d[x + 1]
for item in list_d:
    print(list_d[x])
    x += 1  # x = x+1

x = 0
list_d = ["Justin", "Apple", "Food", 3231, "Another", 12321]
list_e = []
for item in list_d:
    if isinstance(item, int):
        list_e.append(item)
        list_d.pop(x)
    x += 1
print list_d
print list_e
