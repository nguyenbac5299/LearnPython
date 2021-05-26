li = [1, 2.0, 'a', 'b', True]
li[0] #access item in list

# list[start:stop:stepOver] like string

li[0:4:2]
# list is mutable
li[0]=2
print(li)

# copy vs modify
li1=li # if li1 change => li even change

li1=li[:] # li1 change => li not change


