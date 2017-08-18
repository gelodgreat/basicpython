# List
listx = ["asdas", 2]
print listx
# append add to list
listx.append("asd")
print listx
# Pop removing from arraylist
listx.pop()
print listx
print len(listx)
print len("asd")
print listx[0]
listx = ["asd", 2, "asd", 1]
listx.pop(0)
print listx

# Dictionary
a_dict = {
    "1st String": " String",
    "another": "another String"
}
print a_dict
# Changing value in dictionary
a_dict["abs"] = "A new string"
print a_dict
# Putting list to a dictionary
a_dict['abs'] = listx
print a_dict

b_dict = {
    "Second Dictionary": a_dict,
    "Another From Secomd": "Second Data"
}
print b_dict

# tuple python
tup = ("abc", "abc")
print tup

tup = (
    ("abc", "abc"),
    ("abc", "haha")
)
print tup

tup += ("yetAnother", 123)
print tup
