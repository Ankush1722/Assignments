D = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

# (i) Add new entry in D; key=6 and value is "Six"
D[6] = "six"

# (ii) Remove key=2 from D
del D[2]

# (iii) Check if key=6 is present in D.
if 6 in D:
    print("Key 6 is present in D")
else:
    print("Key 6 is not present in D")

# (iv) Count the number of elements present in D
count = len(D)
print("Number of elements in D:", count)

# (v) Add all the values present in D
values=(list(D.values()))
ans='';
for i in values:
    ans=ans+i
print('Sum of the values in D:',ans)

