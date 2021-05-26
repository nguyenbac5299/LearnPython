# matrix
matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [5, 8, 9]
]
matrix[0][1]
matrix[0][1]

# list method
basket = [1, 2, 3, 4, 5]
# adding
new_list = basket.append(100)
print(basket)
print(new_list)  # result:none because it is modifyed in a place
basket.insert(4, 100)
basket.extend([100, 101])

# removing
value = basket.pop()  # remove the end of list and return a value in index
basket.pop(0)  # remove the index of list
basket.remove(2)  # remove a value
# basket.clear()

# index
basket.index(5)  # result:0 return index of value
basket.index(1, 1, 3)  # if not found=>error
# the nifty way is
basket = [1, 1, 2, 2, 2, 3, 4, 5]

print(1 in basket)
print('my' in 'hi my name is A')

print(basket.count(2))

# sort
basket.sort()  # it is a method
sorted(basket)  # it is a function
print(basket.sort())  # none
print(sorted(basket))  # list but not modify in place

new_basket = basket.copy();
basket.reverse()

# common list patterns
basket[:]  # copy
basket[::-1]  # reverse but create a new list

hun = list(range(1, 100))  # 1-> 99

sentence = ' '
sentence = sentence.join('hi', 'my', 'name', 'is', 'bac')
# or
sentence = ' '.join('hi', 'my', 'name', 'is', 'bac')

print(sentence)

# list unpacking

a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)

