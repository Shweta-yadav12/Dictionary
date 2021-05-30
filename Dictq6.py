
# Courses
# Login/Signup
# Question 6

# Q-7. Niche diye gye code snippet ki output kya hoga?
 
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print (len(crates["box"])) 



#  Question 6

# Ek program likhiye jo dictionary me se duplicate keys hata de. Example :- Input :-
 
d={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
}
s={}
print(d) 
for i in d:
    s.update({i:d[i]})
print(s)


#  {“ball”:”red”,”bat”:4,”wickets”:8}
