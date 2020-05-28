friends=['hamza','ali','adil'] #creating a list of simler data type
print(friends)

random=['apple',22,3.2,"book"] #creating a list of different data type elements
print(random)

if random[1]>5:
    print("your answer in greater then given number")
else:
    print(random[1]-10)

if 3>4:
    print('your answer inncorrect')
elif 3<4:
    if ('h'=='h'):
        print('your answer is correct')
    elif 'h'!='h':

        print("3 cannot be greater then 4")
    print('3 is less then 4')

print(random[1]) #prints the element of list, remember the list index starts from 0

print(len(friends)) #gives the length of the list

friends.append("junaid")
print(friends)

friends.insert(2,'asad') #insert is used to insert a single element at a given index

friends.extend(['a','b','c'])#extends the list by multiple values, if more then one value is to be saved extend is used
print(friends)

print(friends[2]) #prints the element on the second index of list

print(friends.count('ali')) #print the occurence of ali in list

friends.append("ali") #append at end of list
print(friends)

print(friends.index("ali")) #retruns the index of element ali in list
print(random)

random.clear() #clears the whole list
print(random)

random=friends.copy() #by value
print(random)

reference = random #by reference
random.insert(2,"new element")
print(reference)

del reference[1] #delete the value of given index
print(reference)

print(friends)
print(friends.index("ali"))

print("asad" in friends)
print("adil" in friends)

print(friends[2:6])#from index 2 to index 6(2 is included 6 is excluded)

print(friends[0:-1]) #from 0 to (total index-1 from list)

print(friends[-1:-3]) #this will return empty list, because you cannot star getting items from end to start
print(friends)

print(friends[1:8:2]) # [start:stop:steps]

num=[1,2,3,4,5,6,7]
print(num[0:6:2])

print(num[-7:-4])