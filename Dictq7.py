# Ek list lijiye aur uske andar dictionaries me keys and values likhiye jaisa ki niche dikhaya
#  gaya hai (Sample Data) aur uske baad saare unique values ko ek list me print karaye. Example :- Input


#    ["2","7",'9','5','1']
a=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
b=[] 
for i in a :
    for j in i :
        b.append(i[j])
print(b)