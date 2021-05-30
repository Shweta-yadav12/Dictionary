#  Question 4

# Ek program likhiye jo ki nested dictionary me se first key or value ko remove kare. Example
#  :- Input :- Output :


dic={
    1:"navgurukul",
    2:'in',
       3:{
           'a':'welcome',
           'b':'to',
           'c':'darmshala'
       }
    }  
del dic[3]['a']  
print(dic)   