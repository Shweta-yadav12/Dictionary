# Courses
# Login/Signup
# Question 6

# Ek program likhiye jo dictionary me se duplicate keys hata de. Example :- Input :-
 
  

 
dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3}
s={}
print(dic)
for i in dic:
    s.update({i:dic[i]})
print(s)
