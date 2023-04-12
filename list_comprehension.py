# PROBLEM 1

 # colors =  ["Python", "Yellow", 'red', 'green', 'gray', 'white', 'blue', 'brown','gold']

# newcolor = []
# for i in colors:
#     if 'e' in i:
#         newcolor.append(i)
# print(newcolor)


# newcolor = [i for i in colors if 'e' in i]
# print(newcolor)

# PROBLEM 2
# WRITE A PROGRAM PROGRAM TO GET ODD AND EVEN NUMBER FROM ANOTHER LIST WHICH CONTAIN
# NUMBER FROM 1 TO 20. USING LIST COMPREHENSION.


# newlist = [i for i in range(1, 21) if i%2 != 0]
# newlist1 = [i for i in range(1, 21) if i%2 == 0]
# print("Odd numbers = "+str(newlist))
# print("Even numbers = "+str(newlist1))

# PROBLEM 3
# WRITE A PYTHON PROGRAM TO GET ONLY STUDENTS NAME WITH STARTING CHARACTER
# 'a' FROM A COMPLETE LIST OF STUDENTS. USING LIST COMPREHENSION

list = ['ade', 'bola', 'caro', 'wood', 'alan', 'water', 'faisat','abiodun']

newlist = [i for i in list if i.startswith('a')]
print(newlist)