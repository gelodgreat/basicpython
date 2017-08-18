# Sorting Strings
# wtf = ["sda","asdas","asd","sada","adasd","Aasdas","Badsa","CSADA"]
# wtf.sort()
# print wtf
# wtf.sort(key=str.lower)
# print wtf
# wtf.sort(key=str.lower,reverse=True)
# print wtf
# wtf_New = sorted(wtf,key=str.lower,reverse=True)
# print wtf_New

# Sorting Numbers and Calculating
# int_Items = [123, 32.21, 312.21, 1, 2, 342.43]
# print sum(int_Items)
# total = sum(int_Items)
# average = total / (len(int_Items)*1.0)
# print average

items = ["Mic", "Phone", 322.21, 1231.213, "Angelo", "Bag", "Android Dev", 233]

str_items = []
num_items = []

# for i in items:
#     if (isinstance(i, float)or isinstance(i, int)):
#         num_items.append(i)
#     elif isinstance(i, str):
#         str_items.append(i)
#     else:
#         pass

# print (str_items)
# print (num_items)

# Funtion that parse numbers and string


def parse_lists(abc):
    str_list_items = []
    num_list_items = []
    for i in items:
        if (isinstance(i, float)or isinstance(i, int)):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass
    return num_list_items, str_list_items


print (parse_lists(items))

# Function that totals the numbers in the list


def geloSum(a, b):
    c = a + b
    return c


print geloSum(100, 2)


def my_Sum(my_num_list):
    total = 0
    for i in my_num_list:
        if (isinstance(i, float) or isinstance(i, int)):
            total += i
    return total


print my_Sum(items)


def count_nums(my_num_list):
    total = 0
    for i in my_num_list:
        if (isinstance(i, float) or isinstance(i, int)):
            total += 1
    return total


print count_nums(items)


def my_Avg(my_num_list):
    the_sum = my_Sum(my_num_list)
    # num_of_items = len(my_num_list)
    num_of_items = count_nums(my_num_list)
    return the_sum / (num_of_items * 1.0)


print my_Avg(items)

# Drills
# Combine the 2 function in 1 function


def practice(num_list_items):
    totalNums = 0
    totalComputed = 0
    listx = []
    for ix in num_list_items:
        if (isinstance(ix, float) or isinstance(ix, int)):
            totalNums += 1
            listx.append(ix)
    for i in listx:
        totalComputed += i

    return totalComputed


print practice(items)
