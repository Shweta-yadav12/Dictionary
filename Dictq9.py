#  Question 9

# "MISSISSIPPI" iss word me har letter ki occurrency count karke ek dictionary me store karaye. Jisme
#  letter dictionary ki keys aur occurrency Uss dictionary ki values hongi. Example:- Output :-
 

a="MISSISSIPPI"
h=[]
n={} 
for i in a :
    h.append(i)
    s=h.count(i)
    n.update({i:s})
print(n)