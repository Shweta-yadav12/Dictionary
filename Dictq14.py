#  Question 14

# Ek program likho jo ki dictionaries ki values ko sort(ascending or descending) kar de. Input :- 


dic={'bjender':45,'deepak':60,'param':20,'anjali':30,'roshani':50}
dic2={}
for i in dic:
    s=dic[i]
    for j in dic:
        a=dic[j]
        if s<a:
            dic2[j]=a
for i in dic:
    s=dic[i]
    for j in dic:
        a=dic[j]
        if s>a:
            dic2[j]=a
print(dic2)
