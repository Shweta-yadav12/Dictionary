# n 13

# Ek code likhiye jo dictionary ki 3 highest value print karaye. Example :-


from collections import Counter

my_dict = {
    'a':50, 
    'b':58,
    'c':56,
    'd':40,
    'e':100, 
    'f':20
    } 

b=[]
k=Counter(my_dict)
high=k.most_common(3)
for i in high:
    b.append(i[0])
print(b)