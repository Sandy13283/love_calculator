A=input("Enter your name: ")
B=input("Enter your Friend name: ")
C= A+B # adding both strings to get a new string
D=C.lower()

# count t in combine name 
T=D.count("t")

# count r in combine name 
R= D.count("r")

# count u in combine name 
U=D.count("u")

# count e in combine name 
E=D.count("e")
true=T+R+U+E
# count l in combine name 
L=D.count("l")
# count o in combine name 
O=D.count("o")
# count v in combine name 
V=D.count("v")
love=L+O+V+E
love_score=str(true)+str(love)
print(f"Your love score is {love_score}%")
