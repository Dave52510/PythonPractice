first_name = 'David'
last_name = 'Pruitt'
full_name = first_name + " " + last_name #apend strings

x = 2
y = 4 ** 2 #this means 4^2 so it's 16
area = x * y
msg = "The area is:"

print("User:", full_name)
print(msg,area) #output multiple messages

print('\n \tPython newline and tab') #\n is newline and \t is tab
print('\n')

#ints and floats to strings
date = 5
msg = "Today is the " + str(5) + "th of January!" #how to use numbers and floats as strings
print(msg)

#Lists
data = ['bike', 'car', 4]
print(data)
print(data[0].title(),data[2])#lists can contain both strings and ints at the same time! BUT NOT RECOMMENED
print(data[-1],"\n") #gets the last item
data[0] = 'child'
data.append('Daria') #add list item
print(data)
data.insert(1,'David') #insert element into list
print(data)
del data[3] #remove element from list
print(data)

popped = data.pop(2)
print(popped) #removed and set to a value

#data.sort() #sorts the list
print(sorted(data)) #temp sort

data.reverse()
print(data)

leng = len(data)
print(leng) #gets the length

for thing in data: #this auto gets evey bit of data and puts it to thing for easy output
    print(thing)

print("Hello world!")

