L = [10, 20, 30, 40, 50, 60, 70, 80]

# (i) Add 200 and 300 to L
L.append(200)
L.append(300)
print('Add 200 and 300 to L:',L)

# (ii) Remove 10 and 30 from L
L.remove(10)
L.remove(30)
print('Remove 10 and 30 from L:',L)

# (iii) Sort L in ascending order
L.sort()
print('Sort L in ascending prder:',L)

# (iv) Sort L in descending order
L.sort(reverse=True)
print('Sort L in descending order:',L)

#Print update list L
print('The update list L:',L)