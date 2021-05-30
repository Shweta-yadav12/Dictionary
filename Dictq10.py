# Ek dictionary ki value ke sabhi items ko count kijiye jo ki ek list me hai. Input :- Output :-


b={
    "alex":["sub1","sub2","sub3"],
    "david":["sub1","sub2"]
}

l=[]
for i in b:
    j=len(b[i])
    l.append(j)
print("count",sum(l))


