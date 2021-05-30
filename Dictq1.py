



# dict={“name”:”Raju”, “marks”:56}
# print

# if input is “name” then output will be “exist”

# If input is “class” then output will be “not exists”.


 
car ={
    "brand":  "ford",
    "model":  "mustang",
    "year":  1964
}
num=input("enter the key:")
if num in car:
    print("Yes, keys in the car dictionary.")

else:
    print("No, key dictionary mai nahi hai.") 
    
    
# Ek program likhiye jisse ki agar di hui key pehle se dictionary me exist karti ho toh 
# “exists “ print kare aur agar nahi karti ho toh “not exists” print kare. Example :-



l={"name":"ankita","age":16,"jack":{1:2,6:7,98:"ram"}}
print(l)
if "name" in dict (l):
    print("yes")
else:
    print("no")