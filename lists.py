#Working with lists
#List functions to add elements==> append(), insert()
#List functions to remove elements ==> remove(), pop()
#other list functions==> sort(), reverse()

myList = [] #An empty list

#Adding Items 
myList.append("Grant")
myList.insert(0,"Aidan")
myList[1] = "Lucin"
myList.append("Simphiwe")
myList.append("Nkosinathi")

#Remove Items
#myList.pop()
#myList.remove()

#Iterating through the list
for x in myList:
    if x=="Lucin":
        print("Lucin is in class")
        continue
    print(x) 



length = len(myList)
print(myList[0])
