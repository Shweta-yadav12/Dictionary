# Login/Signup
# Question 1

# Ek program likhiye jisse ki niche di hui dictionaries ek hi dictionary me aa jaaye jaise ki
#  niche Expected result me diya gaya hain or jisski bhi keys same hai unki values add ho jai.
#   Example :- Input :- Output 

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)

